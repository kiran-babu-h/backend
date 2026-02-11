#!/bin/bash
# Setup script for Linux/Mac

echo "========================================"
echo "QR Food Ordering System - Setup"
echo "========================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[1/5] Python detected: $(python3 --version)"
echo ""

# Check PostgreSQL
echo "[2/5] Please ensure PostgreSQL is installed and running"
echo ""

# Create virtual environment
echo "[3/5] Creating virtual environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "Virtual environment created"
else
    echo "Virtual environment already exists"
fi
echo ""

# Activate virtual environment and install dependencies
echo "[4/5] Installing dependencies..."
source .venv/bin/activate
pip install -r requirements.txt
echo ""

# Setup database
echo "[5/5] Setting up database..."
echo ""
echo "IMPORTANT: Make sure you have:"
echo "1. Created PostgreSQL database 'qr_food_db'"
echo "2. Updated .env file with correct credentials"
echo ""
read -p "Continue with database setup? (Y/N): " continue
if [ "$continue" = "Y" ] || [ "$continue" = "y" ]; then
    python setup.py
fi

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To start the application:"
echo "1. Activate virtual environment: source .venv/bin/activate"
echo "2. Run: python app.py"
echo ""
