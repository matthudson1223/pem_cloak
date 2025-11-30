# PEM Electrolyzer Coating Research Project

**AI-Driven Materials Discovery for Breakthrough Protective Coatings**

## Mission

Develop earth-abundant, cost-effective protective coatings for PEM (Proton Exchange Membrane) electrolyzer bipolar plates that achieve 80,000+ hour operational lifetime, enabling economically viable green hydrogen production.

## The Problem

PEM electrolyzers are critical for green hydrogen production, but current systems fail prematurely due to bipolar plate corrosion and membrane degradation:

**Current Performance Gap:**
- **Current stack lifetime:** 30,000-60,000 hours (actual)
- **Required stack lifetime:** 80,000-100,000 hours (commercial target)
- **Performance gap:** 20,000-50,000 hours of lost operational life

**Economic Impact:**
- Each premature stack replacement costs **$800k-1M per MW**
- Adds **$0.30-0.45/kg to levelized cost of hydrogen (LCOH)**
- Prevents hydrogen from reaching **$2/kg DOE target** for grid parity
- **Total addressable market:** $5-8B annually by 2030

**Technical Challenges:**

1. **Bipolar Plate Corrosion (25-35% of failures)**
   - Stainless steel or titanium plates corrode in acidic environment (pH ~0.3)
   - Operating conditions: 60-80°C, 1.8-2.2V potential
   - Metal ions (Fe, Cr, Ni) leach into electrolyte

2. **Membrane Degradation (40-50% of failures)**
   - Metal ions migrate to membrane, catalyze radical formation
   - Radicals attack polymer chains (Nafion), causing thinning
   - Leads to pinhole formation, crossover, and catastrophic failure

**Current Solutions (Inadequate):**
- **Solid titanium + precious metal coatings (Pt/Au):** Excellent performance but cost-prohibitive (~$100-150k/MW)
- **Coated stainless steel (Ti/Nb, nitrides, carbides):** Lower cost but insufficient durability (1,000-3,000 hour validation vs. 80,000 hour requirement)

## Our Solution: AI-Driven Materials Discovery

Use systematic computational and machine learning approaches to identify earth-abundant coating compositions that meet all requirements:

**Target Performance:**
- ✅ Corrosion resistance: <1 μA/cm² corrosion current
- ✅ Electrical conductivity: <10 mΩ·cm² contact resistance
- ✅ Ion barrier effectiveness: <0.1 μg/cm²/day metal ion release
- ✅ Operational lifetime: 80,000+ hours
- ✅ Cost: <$10/m² (vs. current $30-100/m²)

**Why AI/ML Approach:**
- Screen **200-300 candidates** vs. traditional **5-10 candidates** (20-60x more)
- **3x faster iteration cycles** through accelerated testing + ML extrapolation
- Predict 80,000-hour performance from 2,000-hour tests
- **Cost optimization built-in** from the start, not an afterthought
- Learn from ALL successes AND failures systematically

## Project Phases

### Phase 1: Materials Screening & Database Building (Months 1-3)

**Objectives:**
- Collect 200-300 coating candidates from Materials Project API
- Extract experimental data from 25-35 recent papers (2020-2025)
- Build combined database: computational + experimental properties
- Identify performance targets and gaps

**Deliverables:**
- Materials Project database: 100-300 candidates (oxides, nitrides, carbides)
- Literature database: 25-35 papers with quantitative performance metrics
- Gap analysis: Missing data, failure mechanisms, cost benchmarks
- Property correlation analysis: Which features predict performance

### Phase 2: ML Model Development & Optimization (Months 4-6)

**Objectives:**
- Fine-tune property prediction models on Google Vertex AI / Gemini
- Multi-objective optimization: performance + cost + manufacturability
- Rank top 20 coating candidates for experimental validation
- Design accelerated test protocols

**Deliverables:**
- Trained ML models for corrosion resistance, conductivity, degradation prediction
- Pareto frontier: performance vs. cost trade-offs
- Top 20 candidates with predicted 80,000-hour lifetime
- Experimental validation protocol (500-hour screening, 2,000-hour validation)

### Phase 3: Experimental Validation (Months 7-18)

**Objectives:**
- Partner with university labs for coating deposition
- Rapid screening: 15-20 coatings at 500 hours
- Extended validation: 5-7 down-selected coatings at 2,000 hours
- Single-cell electrolyzer testing: 2-3 top candidates
- ML-based lifetime extrapolation to 80,000 hours

**Budget:** $50,000 over 18-24 months
- Rapid screening (500h): ~$15k
- Extended validation (2,000h): ~$15k
- Single-cell testing: ~$12k
- Materials/deposition: ~$8k

## Technology Stack

**Materials Science:**
- Materials Project API (mp-api) - Computational materials database
- Pymatgen - Materials analysis and property prediction

**Machine Learning:**
- Google Vertex AI / Gemini - Model training and fine-tuning
- TensorFlow / XGBoost - Property prediction models
- Scikit-learn - Data preprocessing and baseline models

**Data Science:**
- Python 3.10+
- Pandas, NumPy, SciPy - Data manipulation and analysis
- Matplotlib, Seaborn, Plotly - Visualization

**Cloud Infrastructure:**
- Google Cloud Platform (GCP) - Model training and deployment
- Cloud Storage - Data and model versioning

## Repository Structure

```
pem-coating-research/
├── README.md                          # This file
├── PROJECT_SUMMARY.md                 # Detailed status tracking
├── EXECUTION_SUMMARY.md              # Quick-start launch guide
├── requirements.txt                  # Python dependencies
├── verify_setup.sh                   # Setup verification script
│
├── data/
│   ├── materials_project/            # Computational materials data
│   ├── literature/                   # Experimental coating performance
│   └── properties/                   # ML predictions
│
├── notebooks/
│   └── 01_data_collection.ipynb     # Initial analysis workflow
│
├── src/
│   ├── data_collection/
│   │   ├── materials_project_collector.py    # Materials Project API
│   │   └── literature_database.py            # Literature data management
│   ├── ml_models/                    # Property prediction models
│   ├── screening/                    # Optimization algorithms
│   └── analysis/                     # Analysis tools
│
├── docs/
│   ├── setup.md                      # Installation & configuration
│   └── RESEARCH_PROMPT.md           # Detailed research execution protocol
│
├── models/                           # Trained ML models
└── results/                          # Outputs, plots, reports
```

## Quick Start

### 1. Installation

```bash
# Clone repository
git clone https://github.com/yourusername/pem-coating-research.git
cd pem-coating-research

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Get a Materials Project API key: https://materialsproject.org/api

```bash
# Set API key
export MP_API_KEY="your_api_key_here"

# Optional: Add to ~/.bashrc or ~/.zshrc for persistence
echo 'export MP_API_KEY="your_api_key_here"' >> ~/.bashrc
```

### 3. Verify Setup

```bash
chmod +x verify_setup.sh
./verify_setup.sh
```

### 4. Collect Data

```bash
# Option 1: Run collector directly
cd src/data_collection
python materials_project_collector.py

# Option 2: Use Jupyter notebook (recommended)
jupyter notebook notebooks/01_data_collection.ipynb
```

## Success Metrics

### Phase 1 (Months 1-3):
- ✅ 100-300 Materials Project candidates collected
- ✅ 25-35 papers in literature database with complete metrics
- ✅ Property correlation analysis complete
- ✅ Research gaps identified
- ✅ Database ready for ML training

### Phase 2 (Months 4-6):
- ✅ ML models trained with >0.85 R² for property prediction
- ✅ Top 20 candidates identified with predicted 80k+ hour lifetime
- ✅ Cost targets met: <$10/m² for top 10 candidates
- ✅ Experimental validation protocol finalized

### Phase 3 (Months 7-18):
- ✅ 15-20 coatings screened at 500 hours
- ✅ 5-7 candidates validated at 2,000 hours
- ✅ 2-3 candidates showing >80,000 hour projected lifetime
- ✅ Cost target achieved: <$10/m²
- ✅ Patent applications filed for top candidates

### Ultimate Success:
- ✅ Coating achieving 80,000+ hours in real electrolyzer stack
- ✅ Reducing LCOH by $0.30-0.45/kg
- ✅ Commercial adoption by electrolyzer manufacturers
- ✅ Contributing to <$2/kg green hydrogen target

## Documentation

- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Detailed status tracking and phase goals
- **[EXECUTION_SUMMARY.md](EXECUTION_SUMMARY.md)** - Quick-start execution guide
- **[docs/setup.md](docs/setup.md)** - Complete installation and configuration guide
- **[docs/RESEARCH_PROMPT.md](docs/RESEARCH_PROMPT.md)** - Task-by-task research protocol

## Key Features

1. **Materials Project Integration** - Automated collection of 100-300 coating candidates
2. **Literature Database** - Structured experimental data from 25-35 papers
3. **Performance Benchmarking** - Compare all coatings against DOE/industry targets
4. **Gap Analysis** - Identify missing data and research opportunities
5. **ML-Ready Data** - Clean, structured data for property prediction models
6. **Cost Optimization** - Economic analysis built into every evaluation

## Why This Approach Will Work

**Systematic, Not Ad-Hoc:**
- Comprehensive database captures ALL available knowledge
- Machine learning identifies patterns humans miss
- Multi-objective optimization balances performance AND cost

**Accelerated Discovery:**
- 20-60x more candidates screened than traditional approaches
- ML extrapolation reduces test time from 80,000 → 2,000 hours
- Iterative refinement based on ALL results (successes + failures)

**Commercially Viable:**
- Cost constraints built-in from day 1
- Focus on earth-abundant materials
- Scalable deposition methods (PVD, CVD, thermal spray)

**Proven Methodology:**
- Similar to successful AI-driven materials discovery (batteries, catalysts, photovoltaics)
- Combines computational screening + experimental validation
- Leverages Google's state-of-the-art Vertex AI infrastructure

## Contributing

This is currently a solo research project. If you're interested in contributing or collaborating, please reach out.

## License

[Specify license - e.g., MIT, Apache 2.0, or proprietary]

## Contact

[Your contact information]

---

**Let's solve the green hydrogen durability challenge and accelerate the clean energy transition.**
