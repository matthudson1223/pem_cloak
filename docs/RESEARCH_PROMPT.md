# Research Execution Protocol

**Purpose:** Systematic task-by-task guidance for PEM electrolyzer coating research

**Target:** Build comprehensive database (computational + experimental) ready for ML training by Month 3

---

## Overview

This document provides detailed execution instructions for 6 key research tasks in Phase 1. Each task includes:
- Clear objectives
- Step-by-step methodology
- Search queries / data sources
- Data extraction checklists
- Success criteria

**Complete these tasks systematically. Quality over speed.**

---

## Task 1: Expand Literature Database (HIGH PRIORITY)

**Objective:** Add 20-25 papers with quantitative coating performance data (target: 25-35 total)

**Timeline:** Weeks 1-8 (3-4 papers per week)

**Current status:** 5 papers pre-populated

### Search Strategy

#### Google Scholar Search Queries

**Primary queries** (use these first):
1. `"PEM electrolyzer" "bipolar plate" "coating" "corrosion"`
2. `"water electrolysis" "titanium nitride" OR "TiN" "contact resistance"`
3. `"proton exchange membrane" "stainless steel" "coating" "durability"`
4. `"PEM water electrolyzer" "protective coating" "performance"`
5. `"hydrogen production" "coating" "corrosion current density"`

**Secondary queries** (for specific material classes):
6. `"Ti4O7" OR "Magneli phase" "water electrolysis"`
7. `"niobium oxide" OR "Nb2O5" "bipolar plate"`
8. `"chromium nitride" OR "CrN" "acidic environment" "electrochemistry"`
9. `"tungsten carbide" OR "WC" "electrolyzer"`
10. `"IrO2" OR "RuO2" "conductive oxide" "PEM"`

**Advanced filters:**
- Years: 2020-2025 (prioritize recent)
- Cited by: >10 citations (indicates impact)
- Keywords to exclude: "alkaline" (we want PEM/acidic only)

#### Alternative Databases

1. **Web of Science** - Filter by topic: "electrolyzer coating"
2. **Scopus** - Advanced search: "(PEM OR proton exchange membrane) AND (coating OR surface treatment) AND (bipolar plate OR current collector)"
3. **ScienceDirect** - Journal filter: Electrochimica Acta, Journal of Power Sources, International Journal of Hydrogen Energy
4. **Materials Project Publications** - https://materialsproject.org/citing-materials-project (find papers using MP data)

### Data Extraction Checklist

For each paper, extract **ALL** of the following (if available):

#### Paper Metadata
- [ ] DOI
- [ ] Authors (Last et al. format)
- [ ] Year
- [ ] Title
- [ ] Journal name

#### Coating Details
- [ ] Material composition (e.g., "TiN", "Nb/Ti dual-layer", "N-doped TiO2")
- [ ] Substrate (e.g., "SS316L", "Ti Grade 1", "SS904L")
- [ ] Thickness (nm) - often in "Experimental Methods"
- [ ] Deposition method (PVD, CVD, thermal spray, electrodeposition, etc.)

#### Performance Metrics (CRITICAL)
- [ ] Corrosion current density (μA/cm²) - from potentiodynamic polarization
- [ ] Contact resistance (mΩ·cm²) - from 4-point probe or stack testing
- [ ] Test duration (hours) - how long was the test run?

#### Test Conditions
- [ ] Electrolyte composition (e.g., "0.5M H2SO4", "1M H2SO4")
- [ ] Temperature (°C) - typically 60-80°C
- [ ] Applied potential (V) - vs. reference electrode
- [ ] Current density (A/cm²) - if under load

#### Degradation Data (if available)
- [ ] Voltage increase rate (μV/hr) - indicates progressive degradation
- [ ] Resistance change (%) - over test duration
- [ ] Visual inspection results (delamination, cracking, discoloration)

#### Ion Leaching (VERY IMPORTANT for membrane degradation)
- [ ] Fe release rate (μg/cm²/day)
- [ ] Cr release rate (μg/cm²/day)
- [ ] Ni release rate (μg/cm²/day)
- [ ] Measured by ICP-MS, ICP-OES, or similar

#### Economics & Scalability
- [ ] Cost estimate ($/m²) - may need to calculate from materials + process
- [ ] Scalability notes (industrial maturity, equipment availability)

#### Assessment
- [ ] Success rating (1-5 scale, your judgment)
  - 5 = Excellent (meets all targets)
  - 4 = Good (meets most targets, minor issues)
  - 3 = Moderate (some targets met, significant gaps)
  - 2 = Poor (few targets met)
  - 1 = Failure (does not meet targets)
- [ ] Failure mode description (if degraded/failed)
- [ ] Additional notes (anything important not captured above)

### How to Add Papers to Database

#### Method 1: Python Script

```python
from src.data_collection.literature_database import LiteratureDatabase, CoatingPerformanceData

# Load existing database
db = LiteratureDatabase()

# Add new entry
db.add_entry(CoatingPerformanceData(
    doi="10.1016/j.ijhydene.2024.xxxxx",
    authors="Smith, Jones, et al.",
    year=2024,
    title="Novel coating for PEM electrolyzers",
    journal="International Journal of Hydrogen Energy",

    # Coating details
    material="Your coating name",
    substrate="SS316L",
    thickness_nm=500.0,
    deposition_method="PVD",

    # Performance metrics
    corrosion_current_uA_cm2=0.5,
    contact_resistance_mOhm_cm2=8.0,
    test_duration_hours=3000.0,

    # Test conditions
    electrolyte="0.5M H2SO4",
    temperature_C=80.0,
    potential_V=1.8,

    # Degradation
    voltage_increase_uV_hr=3.2,

    # Ion leaching (if available)
    fe_release_ug_cm2_day=0.1,
    cr_release_ug_cm2_day=0.05,

    # Economics
    cost_estimate_dollar_m2=12.0,
    scalability_notes="PVD is established process",

    # Assessment
    success_rating=4,
    failure_mode="Minor edge delamination after 3000h",
    notes="Promising candidate, needs longer validation",
    data_quality="high"
))

# Save
db.save_to_csv('../data/literature/coating_performance_database.csv')
print(f"Total papers: {len(db.entries)}")
```

#### Method 2: Edit CSV Directly

1. Open `data/literature/coating_performance_database.csv` in Excel / LibreOffice
2. Add row with all data
3. Save (ensure proper formatting)

**Important:** Use consistent units and formats!

### Quality Standards

**High-quality papers must have:**
- ✅ Quantitative performance data (not just "good" or "improved")
- ✅ Complete test conditions documented
- ✅ Test duration ≥500 hours (preferably ≥1,000 hours)
- ✅ Peer-reviewed journal publication

**Acceptable but lower priority:**
- Conference papers with preliminary data
- Patents with test data
- Technical reports from national labs

**Exclude:**
- Papers with only qualitative results
- Alkaline electrolyzer studies (different environment)
- Fuel cell studies (different conditions)
- Papers with incomplete/missing data

### Success Criteria

**Week 2:** 10-15 papers total (5-10 added)
**Week 4:** 15-20 papers total
**Week 8:** 25-35 papers total

**Target distribution:**
- Oxides: 8-12 papers
- Nitrides: 8-12 papers
- Carbides: 5-8 papers
- Mixed/multilayer: 4-6 papers

---

## Task 2: Failure Mechanism Analysis

**Objective:** Understand WHY coatings fail before 80,000 hours

**Timeline:** Weeks 3-6 (parallel with Task 1)

### Key Questions to Answer

1. **Why do Ti/Nb coatings fail?**
   - Mechanism: H2 embrittlement? Delamination? Defect propagation?
   - Time scale: When does degradation start?
   - Critical factors: Thickness? Substrate adhesion? Defect density?

2. **Why do nitride coatings (TiN, CrN) degrade?**
   - Pinhole formation and corrosion through defects?
   - Oxidation in acidic environment?
   - H2 uptake and lattice damage?

3. **What causes sudden failures vs. gradual degradation?**
   - Catastrophic: Delamination, spalling
   - Gradual: Resistance increase, ion leaching increase

4. **How do defects propagate?**
   - Crack growth mechanisms
   - Corrosion spreading from pinholes
   - Stress-induced failures

### Research Approach

#### Literature Review

Search for:
- "coating failure mechanism electrolyzer"
- "hydrogen embrittlement nitride coating"
- "delamination bipolar plate coating"
- "corrosion initiation PEM"

#### Analysis of Existing Database

For each coating in database, document:
```python
# Run analysis on literature database
db = LiteratureDatabase()
df = db.to_dataframe()

# Group by failure mode
failure_modes = df['failure_mode'].value_counts()
print("Common failure modes:")
print(failure_modes)

# Correlate failure mode with material class
df.groupby(['material_class', 'failure_mode']).size()
```

#### Key Findings to Document

Create document: `results/failure_mechanism_analysis.md`

Structure:
```markdown
# Failure Mechanism Analysis

## Summary of Common Failures

1. **Delamination** (X% of failures)
   - Material classes affected: ...
   - Root causes: ...
   - Mitigation strategies: ...

2. **H2 Embrittlement** (Y% of failures)
   - ...

## Material-Specific Failure Modes

### Nitrides (TiN, CrN, etc.)
- Primary failure: ...
- Secondary: ...
- Time to failure: ...

### Oxides
- ...

### Carbides
- ...

## Critical Insights for ML Model

- Features to track: ...
- Failure prediction indicators: ...
```

### Success Criteria

- [ ] Documented 5-7 major failure mechanisms
- [ ] Identified material class-specific vulnerabilities
- [ ] Understood time-dependent degradation patterns
- [ ] Listed failure prediction indicators for ML

---

## Task 3: Coating Design Space Mapping

**Objective:** Map the parameter space for coating design

**Timeline:** Weeks 4-7

### Parameters to Investigate

#### 1. Single-Layer vs. Multilayer

**Questions:**
- Do multilayer coatings outperform single layers?
- Optimal layer count: 2, 3, or more?
- Which material combinations work best?

**Search:** "multilayer coating electrolyzer", "dual-layer Nb/Ti"

**Document findings:**
```python
# In notebook or script
multilayer_coatings = db.query(material="multilayer")  # Adjust query
single_layer = db.query(...)  # Adjust to filter single layers

# Compare performance
print("Multilayer avg corrosion:", multilayer_coatings['corrosion_current_uA_cm2'].mean())
print("Single layer avg corrosion:", single_layer['corrosion_current_uA_cm2'].mean())
```

#### 2. Coating Thickness Optimization

**Questions:**
- Optimal thickness range?
- Too thin: Pinholes, incomplete coverage
- Too thick: Cost, stress, cracking

**Extract thickness data:**
```python
import matplotlib.pyplot as plt

# Plot thickness vs. performance
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

df.plot.scatter(x='thickness_nm', y='corrosion_current_uA_cm2', ax=axes[0])
axes[0].set_title('Thickness vs. Corrosion')

df.plot.scatter(x='thickness_nm', y='contact_resistance_mOhm_cm2', ax=axes[1])
axes[1].set_title('Thickness vs. Resistance')

plt.tight_layout()
plt.savefig('../results/thickness_optimization.png')
```

**Optimal range to document:**
- Nitrides: XXX-YYY nm
- Oxides: XXX-YYY nm
- Carbides: XXX-YYY nm

#### 3. Anode vs. Cathode Requirements

**Key differences:**
- Anode (oxygen evolution): Higher potential (1.8-2.2V), more oxidizing, harsher
- Cathode (hydrogen evolution): Lower potential (0-0.1V), H2 embrittlement risk

**Questions:**
- Do we need different coatings for anode vs. cathode?
- Which side is more critical?

**Literature search:** "anode coating electrolyzer", "cathode bipolar plate"

#### 4. Substrate Material Impact

**Compare:**
- SS316L (most common, low cost)
- SS904L (higher Ni, better corrosion resistance, moderate cost)
- Ti Grade 1/2 (excellent corrosion resistance, expensive)

**Analysis:**
```python
substrate_performance = df.groupby('substrate').agg({
    'corrosion_current_uA_cm2': 'mean',
    'contact_resistance_mOhm_cm2': 'mean',
    'cost_estimate_dollar_m2': 'mean'
})
print(substrate_performance)
```

### Deliverable

Create: `results/coating_design_space.md`

Include:
- Optimal thickness ranges by material class
- Single vs. multilayer performance comparison
- Substrate recommendations
- Anode vs. cathode coating requirements
- Design guidelines for ML optimization

---

## Task 4: Cost Analysis

**Objective:** Understand cost drivers and identify economically viable approaches

**Timeline:** Weeks 5-8

### Cost Components to Analyze

#### 1. Material Costs

**Earth-abundant vs. precious metals:**
- Ti, Nb, Ta, W, Cr: $X/kg
- Ir, Ru, Pt, Au: $Y/kg (orders of magnitude higher)

**Calculate coating material cost:**
```
Material cost ($/m²) = (Thickness in meters) × (Density in kg/m³) × (Material price in $/kg)

Example for TiN:
Thickness: 500 nm = 500 × 10^-9 m
Density of TiN: ~5,200 kg/m³
Ti price: ~$15/kg, N2 gas: negligible

Material cost = 500e-9 × 5200 × 15 = $0.039/m²

>>> Material cost is negligible! Deposition dominates.
```

#### 2. Deposition Method Costs

Research typical costs:

**PVD (Physical Vapor Deposition):**
- Capital cost: $500k-2M per system
- Operating cost: ~$5-15/m² depending on batch size
- Throughput: 10-50 m²/hr
- Industry maturity: Very high (established)

**CVD (Chemical Vapor Deposition):**
- Capital cost: $300k-1.5M
- Operating cost: ~$8-20/m²
- Throughput: 5-30 m²/hr
- Industry maturity: High

**Thermal Spray:**
- Capital cost: $100k-500k
- Operating cost: ~$3-10/m²
- Throughput: 20-100 m²/hr
- Industry maturity: Very high (lowest cost for thick coatings)

**Electrodeposition:**
- Capital cost: $50k-300k
- Operating cost: ~$2-8/m²
- Throughput: High (batch processing)
- Industry maturity: Very high (but limited materials)

#### 3. Total Cost Calculation

For each paper in database, estimate:
```
Total cost ($/m²) = Material cost + Deposition cost + Substrate cost

Substrate costs:
- SS316L: ~$5-10/m² (1mm thick plate)
- SS904L: ~$15-25/m²
- Ti Grade 1: ~$50-100/m²
```

**Add to database:**
```python
# Calculate total costs
df['total_cost_estimate'] = (
    df['cost_estimate_dollar_m2'] +  # Coating cost
    df['substrate'].map({'SS316L': 7.5, 'SS904L': 20, 'Ti Grade 1': 75, ...})
)

# Identify cost-effective candidates
cost_effective = df[
    (df['total_cost_estimate'] < 10) &  # Under target
    (df['meets_all_targets'] == True)  # Meets performance
]
```

### Economic Analysis Deliverables

Create: `results/cost_analysis.md`

Include:
- Cost breakdown by material class
- Deposition method comparison
- Performance vs. cost Pareto frontier plot
- Identification of cost bottlenecks
- Recommendations for cost reduction strategies

---

## Task 5: Accelerated Testing Protocols

**Objective:** Understand how to predict 80,000-hour lifetime from shorter tests

**Timeline:** Weeks 6-9

### Key Questions

1. **What accelerated test conditions are used?**
   - Higher temperature? (80°C → 90°C)
   - Higher potential? (1.8V → 2.2V)
   - Higher current density?
   - More aggressive electrolyte? (0.5M → 1M H2SO4)

2. **What degradation metrics indicate long-term failure?**
   - Voltage increase rate (μV/hr) - correlates with resistance growth
   - Ion leaching rate - indicates barrier breakdown
   - Surface roughness increase - coating degradation
   - Defect density growth - from SEM imaging

3. **How to extrapolate short-term to long-term?**
   - Linear degradation model
   - Accelerated life testing (Arrhenius, Eyring models)
   - ML-based extrapolation (what we'll build in Phase 2)

### Literature Review

**Search:**
- "accelerated stability test electrolyzer"
- "lifetime prediction PEM"
- "degradation model coating"
- "Arrhenius electrochemical"

### Degradation Signatures to Track

For ML extrapolation, identify early indicators:

**From literature database:**
```python
# Coatings with >1000 hour tests
long_tests = df[df['test_duration_hours'] > 1000]

# Analyze degradation rates
long_tests['degradation_rate'] = (
    long_tests['voltage_increase_uV_hr'] *
    long_tests['test_duration_hours'] / 1000
)

# Which coatings show linear vs. accelerating degradation?
```

### Deliverable

Create: `results/accelerated_testing_protocol.md`

Include:
- Summary of accelerated test conditions from literature
- Degradation signatures for failure prediction
- Proposed 500-hour rapid screening protocol
- Proposed 2,000-hour validation protocol
- Metrics to track for ML-based lifetime extrapolation

---

## Task 6: Property Correlations (ML Feature Engineering)

**Objective:** Identify which Materials Project properties predict coating performance

**Timeline:** Weeks 8-12

### Correlation Analysis

#### 1. Merge Databases

```python
import pandas as pd

# Load Materials Project data
mp_data = pd.read_csv('../data/materials_project/coating_candidates_stable.csv')

# Load literature data
lit_data = pd.read_csv('../data/literature/coating_performance_database.csv')

# Match materials (will require manual mapping)
# Example: "TiN" in literature → "TiN" formula in MP
# Create mapping dictionary
formula_map = {
    'TiN': 'TiN',
    'CrN': 'CrN',
    'Ti4O7': 'Ti4O7',
    # ... complete for all materials
}

# Merge (this is simplified, actual implementation may be more complex)
lit_data['formula'] = lit_data['material'].map(formula_map)
merged = lit_data.merge(mp_data, on='formula', how='left')
```

#### 2. Correlation Matrix

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Select relevant columns
features = [
    'formation_energy_per_atom',
    'energy_above_hull',
    'band_gap',
    'density',
    # ... other MP properties
]

targets = [
    'corrosion_current_uA_cm2',
    'contact_resistance_mOhm_cm2',
    'test_duration_hours'
]

# Compute correlations
correlation_matrix = merged[features + targets].corr()

# Visualize
plt.figure(figsize=(12, 10))
sns.heatmap(
    correlation_matrix.loc[features, targets],
    annot=True,
    cmap='RdBu_r',
    center=0,
    vmin=-1,
    vmax=1
)
plt.title('Materials Project Features vs. Experimental Performance')
plt.tight_layout()
plt.savefig('../results/property_correlations.png')
plt.show()
```

#### 3. Identify Predictive Features

**Strong correlations (|r| > 0.5) indicate:**
- Band gap → Conductivity (expected: lower band gap = better conductivity)
- Formation energy → Stability under acidic conditions
- Density → Corrosion resistance (denser = fewer pathways for ions)

**Document findings:**
```markdown
# Property Correlation Analysis

## Strong Predictors of Corrosion Resistance

1. **Band gap** (r = -0.65): Lower band gap correlates with lower corrosion current
2. **Density** (r = -0.58): Higher density correlates with better protection
3. ...

## Strong Predictors of Contact Resistance

1. **Band gap** (r = 0.72): Lower band gap = lower contact resistance
2. ...

## Features for ML Model

Based on correlation analysis, prioritize:
- Band gap (electronic conductivity proxy)
- Formation energy (thermodynamic stability)
- Density (barrier effectiveness)
- Crystal system (structural properties)
- ...
```

### Feature Engineering

**Create derived features:**
```python
# Examples
merged['stability_metric'] = -merged['formation_energy_per_atom']
merged['conductivity_proxy'] = 1 / (merged['band_gap'] + 0.01)  # Avoid division by zero
merged['barrier_metric'] = merged['density'] * merged['thickness_nm']
```

### Deliverable

Create: `results/ml_feature_engineering.md`

Include:
- Correlation matrix and heatmap
- List of top 10 predictive features
- Feature engineering strategies
- Recommended feature set for ML models
- Notes on data quality and missing values

---

## Tracking Progress

### Weekly Checklist

**Week 1:**
- [ ] Materials Project data collected (100-300 candidates)
- [ ] 3-5 papers added to literature database (total: 8-10)

**Week 2:**
- [ ] 3-5 papers added (total: 11-15)
- [ ] Initial failure mechanism review

**Week 3:**
- [ ] 3-5 papers added (total: 14-20)
- [ ] Coating design space exploration started

**Week 4:**
- [ ] 3-5 papers added (total: 17-25)
- [ ] Cost analysis started

**Week 5-6:**
- [ ] Literature target reached (25-35 papers)
- [ ] Failure mechanism analysis complete
- [ ] Cost analysis complete

**Week 7-8:**
- [ ] Coating design space documented
- [ ] Accelerated testing protocols reviewed

**Week 9-12:**
- [ ] Property correlation analysis complete
- [ ] ML feature engineering complete
- [ ] All Phase 1 deliverables ready

---

## Final Deliverables (End of Month 3)

### Data
- ✅ `data/materials_project/coating_candidates.csv` - 100-300 candidates
- ✅ `data/literature/coating_performance_database.csv` - 25-35 papers

### Analysis Documents
- ✅ `results/failure_mechanism_analysis.md`
- ✅ `results/coating_design_space.md`
- ✅ `results/cost_analysis.md`
- ✅ `results/accelerated_testing_protocol.md`
- ✅ `results/ml_feature_engineering.md`

### Visualizations
- ✅ Performance vs. cost Pareto frontier
- ✅ Property correlation heatmap
- ✅ Thickness optimization plots
- ✅ Materials by class distributions

### Summary Report
- ✅ `results/phase1_summary_report.md` - Comprehensive summary for Phase 2 planning

---

## Quality Standards

### Data Quality
- Every metric properly documented with units
- Test conditions recorded for all data points
- Missing data explicitly marked (not left blank)
- Sources cited (DOI always included)

### Analysis Quality
- All conclusions supported by data
- Correlations quantified (not just "appears to")
- Limitations acknowledged
- Alternative interpretations considered

### Documentation Quality
- Clear, structured markdown
- Figures with captions
- Code commented and reproducible
- References to source papers

---

## Getting Help

**Stuck on a task?**
1. Review the relevant notebook section
2. Check example implementations in `src/data_collection/`
3. Consult Materials Project documentation: https://docs.materialsproject.org
4. Search for similar analyses in published papers

**Questions about data?**
- Check data/literature/coating_performance_database.csv for examples
- Review CoatingPerformanceData class definition
- Consult electrochemistry textbooks for metric definitions

**Technical issues?**
- See docs/setup.md for troubleshooting
- Verify environment: `./verify_setup.sh`

---

**This protocol ensures systematic, high-quality data collection and analysis. Follow it carefully, and you'll have an ML-ready database by Month 3.**
