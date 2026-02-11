@echo off
REM Setup script for Windows
echo ========================================
echo QR Food Ordering System - Setup
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo [1/5] Python detected
echo.

REM Check PostgreSQL
echo [2/5] Please ensure PostgreSQL is installed and running
echo.

REM Create virtual environment
echo [3/5] Creating virtual environment...
if not exist .venv (
    python -m venv .venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)
echo.

REM Activate virtual environment and install dependencies
echo [4/5] Installing dependencies...
call .venv\Scripts\activate.bat
pip install -r requirements.txt
echo.

REM Setup database
echo [5/5] Setting up database...
echo.
echo IMPORTANT: Make sure you have:
echo 1. Created PostgreSQL database 'qr_food_db'
echo 2. Updated .env file with correct credentials
echo.
set /p continue="Continue with database setup? (Y/N): "
if /i "%continue%"=="Y" (
    python setup.py
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the application:
echo 1. Activate virtual environment: .venv\Scripts\activate
echo 2. Run: python app.py
echo.
pause
