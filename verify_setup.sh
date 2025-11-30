#!/bin/bash

# PEM Electrolyzer Coating Research Project
# Setup Verification Script
#
# This script verifies that all components are properly installed and configured.

set -e  # Exit on error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
PASSED=0
FAILED=0
WARNINGS=0

echo "========================================"
echo "PEM Electrolyzer Coating Research"
echo "Setup Verification"
echo "========================================"
echo ""

# Function to print success
check_pass() {
    echo -e "${GREEN}✓${NC} $1"
    ((PASSED++))
}

# Function to print failure
check_fail() {
    echo -e "${RED}✗${NC} $1"
    ((FAILED++))
}

# Function to print warning
check_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
    ((WARNINGS++))
}

# 1. Check Python version
echo "Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

    if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 10 ]; then
        check_pass "Python $PYTHON_VERSION found"
    else
        check_fail "Python 3.10+ required (found $PYTHON_VERSION)"
    fi
else
    check_fail "Python 3 not found"
fi
echo ""

# 2. Check directory structure
echo "Checking directory structure..."
DIRS=(
    "data"
    "data/materials_project"
    "data/literature"
    "data/properties"
    "notebooks"
    "src"
    "src/data_collection"
    "src/ml_models"
    "src/screening"
    "src/analysis"
    "docs"
    "models"
    "results"
)

for dir in "${DIRS[@]}"; do
    if [ -d "$dir" ]; then
        check_pass "$dir/"
    else
        check_fail "$dir/ not found"
    fi
done
echo ""

# 3. Check key files
echo "Checking key files..."
FILES=(
    "README.md"
    "PROJECT_SUMMARY.md"
    "EXECUTION_SUMMARY.md"
    "requirements.txt"
    "src/__init__.py"
    "src/data_collection/__init__.py"
    "src/data_collection/materials_project_collector.py"
    "src/data_collection/literature_database.py"
    "notebooks/01_data_collection.ipynb"
    "docs/setup.md"
    "docs/RESEARCH_PROMPT.md"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        check_pass "$file"
    else
        check_fail "$file not found"
    fi
done
echo ""

# 4. Check environment variables
echo "Checking environment variables..."
if [ -z "$MP_API_KEY" ]; then
    check_warn "MP_API_KEY not set (required for Materials Project data collection)"
    echo "  → Set with: export MP_API_KEY='your_key_here'"
    echo "  → Get key at: https://materialsproject.org/api"
else
    check_pass "MP_API_KEY is set"
fi
echo ""

# 5. Check Python packages (if in virtual environment)
echo "Checking Python packages..."
PACKAGES=(
    "numpy"
    "pandas"
    "scipy"
    "sklearn"
    "matplotlib"
    "seaborn"
    "jupyter"
    "pymatgen"
    "mp_api"
)

for package in "${PACKAGES[@]}"; do
    if python3 -c "import $package" 2>/dev/null; then
        check_pass "$package"
    else
        check_warn "$package not installed"
        echo "  → Install with: pip install -r requirements.txt"
    fi
done
echo ""

# 6. Check if in virtual environment (recommended but not required)
echo "Checking virtual environment..."
if [ -n "$VIRTUAL_ENV" ] || [ -n "$CONDA_DEFAULT_ENV" ]; then
    if [ -n "$VIRTUAL_ENV" ]; then
        check_pass "Virtual environment active: $VIRTUAL_ENV"
    else
        check_pass "Conda environment active: $CONDA_DEFAULT_ENV"
    fi
else
    check_warn "Not in a virtual environment (recommended but optional)"
    echo "  → Create with: python3 -m venv venv"
    echo "  → Activate with: source venv/bin/activate"
fi
echo ""

# 7. Test Python module imports
echo "Testing Python module imports..."
if python3 -c "from src.data_collection.materials_project_collector import MaterialsProjectCollector" 2>/dev/null; then
    check_pass "Materials Project collector importable"
else
    check_warn "Cannot import Materials Project collector (may need to install dependencies)"
fi

if python3 -c "from src.data_collection.literature_database import LiteratureDatabase" 2>/dev/null; then
    check_pass "Literature database importable"
else
    check_warn "Cannot import Literature database (may need to install dependencies)"
fi
echo ""

# 8. Check Jupyter installation
echo "Checking Jupyter..."
if command -v jupyter &> /dev/null; then
    JUPYTER_VERSION=$(jupyter --version 2>&1 | head -n1)
    check_pass "Jupyter installed ($JUPYTER_VERSION)"
else
    check_warn "Jupyter not found"
    echo "  → Install with: pip install jupyter"
fi
echo ""

# 9. Check git configuration
echo "Checking Git..."
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version 2>&1 | awk '{print $3}')
    check_pass "Git installed (version $GIT_VERSION)"

    # Check if we're in a git repository
    if git rev-parse --git-dir > /dev/null 2>&1; then
        check_pass "Git repository initialized"

        # Check current branch
        CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
        echo "  Current branch: $CURRENT_BRANCH"
    else
        check_warn "Not a git repository"
    fi
else
    check_warn "Git not installed"
fi
echo ""

# Summary
echo "========================================"
echo "VERIFICATION SUMMARY"
echo "========================================"
echo -e "${GREEN}Passed:${NC} $PASSED"
echo -e "${YELLOW}Warnings:${NC} $WARNINGS"
echo -e "${RED}Failed:${NC} $FAILED"
echo ""

if [ $FAILED -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✓ ALL CHECKS PASSED!${NC}"
    echo ""
    echo "Your setup is complete and ready to use."
    echo ""
    echo "Next steps:"
    echo "1. Set Materials Project API key (if not already set):"
    echo "   export MP_API_KEY='your_key_here'"
    echo ""
    echo "2. Collect Materials Project data:"
    echo "   cd src/data_collection"
    echo "   python materials_project_collector.py"
    echo ""
    echo "3. Open analysis notebook:"
    echo "   jupyter notebook notebooks/01_data_collection.ipynb"
    echo ""
    echo "See EXECUTION_SUMMARY.md for detailed instructions."

elif [ $FAILED -eq 0 ]; then
    echo -e "${YELLOW}⚠ SETUP MOSTLY COMPLETE (with warnings)${NC}"
    echo ""
    echo "Your basic setup is complete, but some optional components"
    echo "are missing. Review warnings above."
    echo ""
    echo "Critical next step:"
    if [ -z "$MP_API_KEY" ]; then
        echo "1. Set Materials Project API key:"
        echo "   export MP_API_KEY='your_key_here'"
        echo "   Get key at: https://materialsproject.org/api"
        echo ""
    fi
    if python3 -c "import mp_api" 2>/dev/null; then
        :
    else
        echo "2. Install Python dependencies:"
        echo "   pip install -r requirements.txt"
        echo ""
    fi
    echo "See EXECUTION_SUMMARY.md for detailed instructions."

else
    echo -e "${RED}✗ SETUP INCOMPLETE${NC}"
    echo ""
    echo "Some critical components are missing. Review failures above."
    echo ""
    echo "Common fixes:"
    echo "1. Install Python dependencies:"
    echo "   pip install -r requirements.txt"
    echo ""
    echo "2. Set Materials Project API key:"
    echo "   export MP_API_KEY='your_key_here'"
    echo ""
    echo "3. See docs/setup.md for complete setup instructions"

    exit 1
fi

echo "========================================"
