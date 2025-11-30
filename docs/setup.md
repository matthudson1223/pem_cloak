# Setup Guide: PEM Electrolyzer Coating Research Project

Complete installation and configuration instructions for the research infrastructure.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Verification](#verification)
5. [Troubleshooting](#troubleshooting)
6. [Google Cloud Platform Setup](#google-cloud-platform-setup-optional)
7. [Next Steps](#next-steps)

---

## Prerequisites

### Required Software

**Python 3.10 or higher**
```bash
# Check Python version
python3 --version  # Should be 3.10.0 or higher

# If needed, install Python 3.10+
# Ubuntu/Debian:
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip

# macOS (using Homebrew):
brew install python@3.10

# Windows: Download from python.org
```

**Git** (for version control)
```bash
# Check if installed
git --version

# Ubuntu/Debian:
sudo apt install git

# macOS:
brew install git

# Windows: Download from git-scm.com
```

**Jupyter Notebook** (will be installed with dependencies)

### Recommended Software

- **Virtual environment manager** (venv, conda, or virtualenv)
- **Text editor / IDE** (VS Code, PyCharm, Sublime, etc.)
- **Terminal** with bash/zsh support

### System Requirements

- **Disk space:** 2-5 GB (for dependencies and data)
- **RAM:** 4 GB minimum, 8 GB recommended
- **Internet connection:** Required for API access and package installation

---

## Installation

### Step 1: Clone Repository

If you haven't already:

```bash
git clone https://github.com/yourusername/pem-coating-research.git
cd pem-coating-research
```

Or if setting up from an existing directory:
```bash
cd /path/to/pem-coating-research
```

### Step 2: Create Virtual Environment

**Using venv (recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS

# On Windows:
venv\Scripts\activate
```

**Using conda:**
```bash
conda create -n pem-coating python=3.10
conda activate pem-coating
```

**Verify activation:**
```bash
which python  # Should point to venv/bin/python or conda env
```

### Step 3: Upgrade pip

```bash
pip install --upgrade pip setuptools wheel
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

**Installation time:** 5-15 minutes depending on internet speed and system.

**Packages installed:**
- Data science: numpy, pandas, scipy
- Machine learning: scikit-learn, tensorflow, xgboost
- Materials science: pymatgen, mp-api
- Google Cloud: google-cloud-aiplatform, vertexai
- Visualization: matplotlib, seaborn, plotly
- Utilities: tqdm, jupyter, python-dotenv

**Note:** TensorFlow installation may require additional system dependencies on some platforms. See troubleshooting if issues occur.

---

## Configuration

### Materials Project API Key

**Required for data collection from Materials Project.**

#### 1. Get API Key

1. Go to: https://materialsproject.org
2. Click "Sign In" (top right) or "Register"
3. Create account / Log in
4. Navigate to "Dashboard" → "API"
5. Click "Generate API Key" (if you don't have one)
6. Copy your API key (looks like: `abcdefgh123456789`)

#### 2. Set Environment Variable

**Linux / macOS:**
```bash
# For current session only:
export MP_API_KEY="your_api_key_here"

# For persistent configuration (recommended):
echo 'export MP_API_KEY="your_api_key_here"' >> ~/.bashrc  # or ~/.zshrc
source ~/.bashrc  # or source ~/.zshrc

# Verify:
echo $MP_API_KEY
```

**Windows (Command Prompt):**
```cmd
setx MP_API_KEY "your_api_key_here"
# Restart terminal for changes to take effect
```

**Windows (PowerShell):**
```powershell
[System.Environment]::SetEnvironmentVariable('MP_API_KEY', 'your_api_key_here', 'User')
# Restart terminal for changes to take effect
```

#### 3. Alternative: Using .env File

Create a `.env` file in project root:
```bash
echo "MP_API_KEY=your_api_key_here" > .env
```

**Note:** The code will automatically load this file using python-dotenv.

### Google Cloud Platform (Optional - Phase 2)

**Not needed for Phase 1 (data collection).**

For Phase 2 (ML model training), you'll need GCP access. See [Google Cloud Platform Setup](#google-cloud-platform-setup-optional) below.

---

## Verification

### Automated Verification Script

Run the provided verification script:

```bash
chmod +x verify_setup.sh
./verify_setup.sh
```

**Expected output:**
```
========================================
PEM Electrolyzer Coating Research
Setup Verification
========================================

Checking Python version...
✓ Python 3.10.0 found

Checking directory structure...
✓ data/materials_project
✓ data/literature
✓ src/data_collection
✓ notebooks
✓ docs
... (all directories)

Checking key files...
✓ requirements.txt
✓ README.md
✓ src/data_collection/materials_project_collector.py
... (all files)

Checking environment variables...
✓ MP_API_KEY is set

Checking Python packages...
✓ numpy
✓ pandas
✓ mp-api
... (all packages)

========================================
VERIFICATION COMPLETE
All checks passed!
========================================
```

### Manual Verification

**1. Python Packages:**
```bash
python -c "import pandas; import numpy; import mp_api; print('✓ Core packages installed')"
```

**2. Materials Project API:**
```bash
python -c "from mp_api.client import MPRester; import os; api_key = os.getenv('MP_API_KEY'); print('✓ API key configured' if api_key else '✗ API key not set')"
```

**3. Jupyter Notebook:**
```bash
jupyter notebook --version
# Should print version number
```

**4. Project Modules:**
```bash
python -c "from src.data_collection.materials_project_collector import MaterialsProjectCollector; print('✓ Modules importable')"
```

---

## Troubleshooting

### Common Issues

#### 1. "ModuleNotFoundError: No module named 'mp_api'"

**Problem:** Dependencies not installed or wrong Python environment.

**Solution:**
```bash
# Verify virtual environment is activated
which python  # Should show venv path

# Reinstall dependencies
pip install -r requirements.txt

# If still failing, try individual install:
pip install mp-api
```

#### 2. "MP_API_KEY not found"

**Problem:** Environment variable not set.

**Solution:**
```bash
# Set temporarily
export MP_API_KEY="your_key"

# Verify
echo $MP_API_KEY

# For persistence, add to ~/.bashrc
echo 'export MP_API_KEY="your_key"' >> ~/.bashrc
source ~/.bashrc
```

#### 3. TensorFlow Installation Fails

**Problem:** TensorFlow has specific system requirements.

**Solution:**

For **CPU-only version** (sufficient for Phase 1-2):
```bash
pip install tensorflow-cpu
```

For **GPU version** (requires CUDA):
```bash
# Ensure CUDA and cuDNN are installed first
pip install tensorflow
```

**Alternative:** Skip TensorFlow for now (not needed until Phase 2):
```bash
# Remove tensorflow from requirements.txt
# Install remaining packages
```

#### 4. "Permission denied" when running verify_setup.sh

**Problem:** Script not executable.

**Solution:**
```bash
chmod +x verify_setup.sh
./verify_setup.sh
```

#### 5. Import errors with pymatgen

**Problem:** Pymatgen requires system libraries.

**Solution:**

**Ubuntu/Debian:**
```bash
sudo apt install libxcb1 libxrender1 libxext6
pip install pymatgen
```

**macOS:**
```bash
brew install libxcb
pip install pymatgen
```

#### 6. Jupyter kernel not found

**Problem:** Jupyter can't find Python kernel.

**Solution:**
```bash
python -m ipykernel install --user --name=pem-coating
jupyter notebook
# In notebook: Kernel → Change kernel → pem-coating
```

### Package Conflicts

If you encounter version conflicts:

**Option 1: Create fresh environment**
```bash
deactivate  # Exit current venv
rm -rf venv  # Remove old environment
python3 -m venv venv  # Create new environment
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Option 2: Use conda (better dependency resolution)**
```bash
conda create -n pem-coating python=3.10
conda activate pem-coating
pip install -r requirements.txt
```

---

## Google Cloud Platform Setup (Optional)

**Not required for Phase 1 (Months 1-3).**

For Phase 2 ML model training, you'll need GCP access to Vertex AI.

### 1. Create GCP Account

1. Go to: https://cloud.google.com
2. Sign up / Sign in
3. Create new project: "pem-coating-research"

### 2. Enable APIs

```bash
gcloud services enable aiplatform.googleapis.com
gcloud services enable storage.googleapis.com
```

### 3. Install gcloud CLI

**Linux:**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

**macOS:**
```bash
brew install --cask google-cloud-sdk
gcloud init
```

**Windows:**
Download installer from: https://cloud.google.com/sdk/docs/install

### 4. Authenticate

```bash
gcloud auth login
gcloud auth application-default login
gcloud config set project pem-coating-research
```

### 5. Set Project ID

```bash
export GCP_PROJECT_ID="pem-coating-research"
echo 'export GCP_PROJECT_ID="pem-coating-research"' >> ~/.bashrc
```

### 6. Create Storage Bucket

```bash
gsutil mb -l us-central1 gs://pem-coating-data
```

**Note:** Detailed Phase 2 GCP setup will be provided at end of Phase 1.

---

## Next Steps

After successful setup:

### Immediate Actions

1. **Verify setup:**
   ```bash
   ./verify_setup.sh
   ```

2. **Collect Materials Project data:**
   ```bash
   cd src/data_collection
   python materials_project_collector.py
   ```

3. **Open analysis notebook:**
   ```bash
   jupyter notebook notebooks/01_data_collection.ipynb
   ```

### Week 1 Goals

- ✅ Materials Project data collected (100-300 candidates)
- ✅ Literature database expanded (add 5-10 papers)
- ✅ Initial analysis complete

### Documentation to Read

- **EXECUTION_SUMMARY.md** - Quick-start execution guide
- **docs/RESEARCH_PROMPT.md** - Task-by-task research protocol
- **PROJECT_SUMMARY.md** - Detailed status and timeline

---

## Additional Resources

### Documentation
- Materials Project API: https://docs.materialsproject.org
- Pymatgen: https://pymatgen.org
- Vertex AI: https://cloud.google.com/vertex-ai/docs

### Research Papers
Pre-populated in literature database. See:
```bash
cat data/literature/coating_performance_database.csv
```

### Support
- GitHub Issues: [link to repo]/issues
- Materials Project Forum: https://matsci.org/c/materials-project

---

## Summary Checklist

Before starting data collection, ensure:

- [ ] Python 3.10+ installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Materials Project API key set (`echo $MP_API_KEY`)
- [ ] Verification script passes (`./verify_setup.sh`)
- [ ] Jupyter notebook launches (`jupyter notebook`)
- [ ] Project modules importable (test in Python)

**If all checked, you're ready to start data collection!**

---

**Setup complete? → See EXECUTION_SUMMARY.md for next steps.**
