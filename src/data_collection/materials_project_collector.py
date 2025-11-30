"""
Materials Project Data Collector for PEM Electrolyzer Coating Candidates

This module interfaces with the Materials Project API to identify and collect
potential coating materials for PEM electrolyzer bipolar plates.

Target coating classes:
- Conductive oxides (Sn-O, In-O, Ir-O, Ti-O, Ru-O, Nb-O, Ta-O)
- Nitrides (Ti-N, Cr-N, Zr-N, Ta-N, V-N, Nb-N, W-N, Mo-N)
- Carbides (Ti-C, W-C, Ta-C, Cr-C, Zr-C, Nb-C, V-C, Mo-C)

Requirements:
- mp-api package (pip install mp-api)
- Materials Project API key (set as environment variable: MP_API_KEY)
"""

import os
import pandas as pd
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import warnings

try:
    from mp_api.client import MPRester
except ImportError:
    raise ImportError(
        "mp-api package not found. Install with: pip install mp-api"
    )


@dataclass
class CoatingCandidate:
    """Data structure for a coating material candidate."""

    material_id: str
    formula: str
    composition: str
    formation_energy_per_atom: float
    energy_above_hull: float
    band_gap: float
    density: float
    crystal_system: str
    space_group: str
    volume: float
    elements: str
    nelements: int
    material_class: str  # oxide, nitride, carbide
    chemical_system: str
    is_stable: bool


class MaterialsProjectCollector:
    """
    Collector for coating material candidates from Materials Project.

    This class provides methods to search for and retrieve potential coating
    materials from the Materials Project database, focusing on conductive
    oxides, nitrides, and carbides suitable for PEM electrolyzer applications.
    """

    # Define chemical systems for each coating class
    CONDUCTIVE_OXIDES = [
        "Sn-O", "In-O", "Ir-O", "Ti-O", "Ru-O", "Nb-O", "Ta-O",
        "In-Sn-O",  # ITO variants
        "Zr-O", "Hf-O"  # Additional candidates
    ]

    NITRIDES = [
        "Ti-N", "Cr-N", "Zr-N", "Ta-N", "V-N", "Nb-N", "W-N", "Mo-N",
        "Al-N", "Hf-N", "Si-N"  # Additional candidates
    ]

    CARBIDES = [
        "Ti-C", "W-C", "Ta-C", "Cr-C", "Zr-C", "Nb-C", "V-C", "Mo-C",
        "Si-C", "Hf-C", "B-C"  # Additional candidates
    ]

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Materials Project collector.

        Args:
            api_key: Materials Project API key. If not provided, will try to
                    read from MP_API_KEY environment variable.

        Raises:
            ValueError: If no API key is provided or found in environment.
        """
        self.api_key = api_key or os.getenv("MP_API_KEY")

        if not self.api_key:
            raise ValueError(
                "Materials Project API key not found. Either:\n"
                "1. Pass api_key parameter to MaterialsProjectCollector()\n"
                "2. Set MP_API_KEY environment variable\n\n"
                "Get your API key at: https://materialsproject.org/api"
            )

        self.candidates: List[CoatingCandidate] = []

    def collect_coating_candidates(
        self,
        stability_threshold: float = 0.1,
        include_oxides: bool = True,
        include_nitrides: bool = True,
        include_carbides: bool = True,
        verbose: bool = True
    ) -> pd.DataFrame:
        """
        Collect coating material candidates from Materials Project.

        Args:
            stability_threshold: Maximum energy above hull (eV/atom) to consider
                               a material stable. Default 0.1 eV/atom.
            include_oxides: Include conductive oxide candidates
            include_nitrides: Include nitride candidates
            include_carbides: Include carbide candidates
            verbose: Print progress information

        Returns:
            DataFrame containing all collected coating candidates
        """
        self.candidates = []

        # Build list of chemical systems to search
        systems_to_search = []
        if include_oxides:
            systems_to_search.extend([(s, "oxide") for s in self.CONDUCTIVE_OXIDES])
        if include_nitrides:
            systems_to_search.extend([(s, "nitride") for s in self.NITRIDES])
        if include_carbides:
            systems_to_search.extend([(s, "carbide") for s in self.CARBIDES])

        if verbose:
            print(f"Searching {len(systems_to_search)} chemical systems...")
            print(f"Stability threshold: {stability_threshold} eV/atom above hull\n")

        # Search each chemical system
        with MPRester(self.api_key) as mpr:
            for chemical_system, material_class in systems_to_search:
                if verbose:
                    print(f"Searching {chemical_system} ({material_class})...", end=" ")

                try:
                    # Query Materials Project
                    docs = mpr.materials.summary.search(
                        chemsys=chemical_system,
                        fields=[
                            "material_id",
                            "formula_pretty",
                            "composition",
                            "formation_energy_per_atom",
                            "energy_above_hull",
                            "band_gap",
                            "density",
                            "symmetry",
                            "volume",
                            "elements",
                            "nelements"
                        ]
                    )

                    # Process results
                    stable_count = 0
                    for doc in docs:
                        # Check stability
                        energy_above_hull = doc.energy_above_hull
                        is_stable = energy_above_hull <= stability_threshold

                        if is_stable:
                            stable_count += 1

                        # Create candidate
                        candidate = CoatingCandidate(
                            material_id=doc.material_id,
                            formula=doc.formula_pretty,
                            composition=str(doc.composition),
                            formation_energy_per_atom=doc.formation_energy_per_atom,
                            energy_above_hull=energy_above_hull,
                            band_gap=doc.band_gap,
                            density=doc.density,
                            crystal_system=doc.symmetry.crystal_system.value,
                            space_group=doc.symmetry.symbol,
                            volume=doc.volume,
                            elements="-".join([str(e) for e in doc.elements]),
                            nelements=doc.nelements,
                            material_class=material_class,
                            chemical_system=chemical_system,
                            is_stable=is_stable
                        )

                        self.candidates.append(candidate)

                    if verbose:
                        print(f"Found {len(docs)} materials ({stable_count} stable)")

                except Exception as e:
                    if verbose:
                        print(f"Error: {str(e)}")
                    warnings.warn(f"Failed to retrieve {chemical_system}: {str(e)}")

        # Convert to DataFrame
        df = self._to_dataframe()

        if verbose:
            print(f"\n{'='*60}")
            print(f"COLLECTION COMPLETE")
            print(f"{'='*60}")
            print(f"Total materials found: {len(df)}")
            print(f"Stable materials (E_hull ≤ {stability_threshold} eV/atom): {df['is_stable'].sum()}")
            print(f"\nBreakdown by class:")
            print(df.groupby('material_class').size())
            print(f"{'='*60}\n")

        return df

    def _to_dataframe(self) -> pd.DataFrame:
        """Convert collected candidates to a pandas DataFrame."""
        if not self.candidates:
            return pd.DataFrame()

        data = [asdict(candidate) for candidate in self.candidates]
        df = pd.DataFrame(data)

        # Sort by energy above hull (most stable first)
        df = df.sort_values('energy_above_hull').reset_index(drop=True)

        return df

    def save_to_csv(
        self,
        filepath: str,
        stable_only: bool = False,
        verbose: bool = True
    ) -> None:
        """
        Save collected candidates to CSV file.

        Args:
            filepath: Path to save CSV file
            stable_only: If True, only save stable materials
            verbose: Print save confirmation
        """
        df = self._to_dataframe()

        if stable_only:
            df = df[df['is_stable']]

        df.to_csv(filepath, index=False)

        if verbose:
            print(f"Saved {len(df)} materials to {filepath}")

    def get_summary_statistics(self) -> Dict:
        """
        Get summary statistics of collected materials.

        Returns:
            Dictionary containing summary statistics
        """
        df = self._to_dataframe()

        if df.empty:
            return {"error": "No materials collected yet"}

        stats = {
            "total_materials": len(df),
            "stable_materials": df['is_stable'].sum(),
            "by_class": df.groupby('material_class').size().to_dict(),
            "avg_formation_energy": df['formation_energy_per_atom'].mean(),
            "avg_band_gap": df['band_gap'].mean(),
            "avg_density": df['density'].mean(),
            "stability_range": {
                "min": df['energy_above_hull'].min(),
                "max": df['energy_above_hull'].max(),
                "mean": df['energy_above_hull'].mean()
            }
        }

        return stats


def main():
    """
    Example usage of MaterialsProjectCollector.

    This function demonstrates how to use the collector to retrieve
    coating candidates and save them to a CSV file.
    """
    print("="*60)
    print("Materials Project Coating Candidate Collector")
    print("="*60)
    print()

    # Initialize collector (will use MP_API_KEY environment variable)
    try:
        collector = MaterialsProjectCollector()
    except ValueError as e:
        print(f"ERROR: {e}")
        return

    # Collect candidates
    print("Collecting coating candidates from Materials Project...")
    print("This may take several minutes depending on API response time.\n")

    df = collector.collect_coating_candidates(
        stability_threshold=0.1,
        include_oxides=True,
        include_nitrides=True,
        include_carbides=True,
        verbose=True
    )

    # Display summary
    print("\nSUMMARY STATISTICS:")
    print("-" * 60)
    stats = collector.get_summary_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")

    # Save to CSV
    output_file = "data/materials_project/coating_candidates.csv"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    collector.save_to_csv(output_file, stable_only=False, verbose=True)

    # Also save stable-only version
    stable_file = "data/materials_project/coating_candidates_stable.csv"
    collector.save_to_csv(stable_file, stable_only=True, verbose=True)

    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    print("1. Review the collected materials in the CSV files")
    print("2. Open notebooks/01_data_collection.ipynb for analysis")
    print("3. Add experimental data to the literature database")
    print("4. Begin property correlation analysis")
    print("="*60)


if __name__ == "__main__":
    main()
