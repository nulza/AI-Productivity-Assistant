@echo off
REM AI Workplace Productivity Assistant - Setup & Run Script (Windows)

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║     🤖 AI WORKPLACE PRODUCTIVITY ASSISTANT - SETUP 🤖         ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check Python installation
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Python not found. Please install Python 3.8 or higher.
    pause
    exit /b 1
)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✓ Found: Python %PYTHON_VERSION%
echo.

REM Create virtual environment
echo [2/5] Setting up virtual environment...
if not exist "venv" (
    python -m venv venv
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat
echo ✓ Virtual environment activated
echo.

REM Install dependencies
echo [3/5] Installing dependencies...
python -m pip install -q --upgrade pip
pip install -q -r api\requirements.txt
echo ✓ Dependencies installed
echo.

REM Create logs directory
echo [4/5] Setting up logging...
if not exist "logs" mkdir logs
if not exist "logs\api.log" type nul > logs\api.log
if not exist "logs\app.log" type nul > logs\app.log
echo ✓ Logging configured
echo.

REM Check and create .env files
echo [5/5] Checking configuration files...
if not exist "api\.env" (
    echo ⚠️  Creating api\.env from template...
    copy api\.env.example api\.env
    echo ⚠️  Please update api\.env with your OPENAI_API_KEY
)
echo ✓ Configuration ready
echo.

echo ╔════════════════════════════════════════════════════════════════╗
echo ║                    ✅ SETUP COMPLETE                          ║
echo ║                                                                ║
echo ║  To start the application:                                    ║
echo ║                                                                ║
echo ║  1. API Server (Command Prompt 1):                            ║
echo ║     venv\Scripts\activate                                     ║
echo ║     python api\server.py                                      ║
echo ║                                                                ║
echo ║  2. Web App (Command Prompt 2):                               ║
echo ║     Open web-app\index.html in your browser                   ║
echo ║     Or use: python -m http.server 8000                        ║
echo ║                                                                ║
echo ║  Documentation:                                               ║
echo ║  - README.md: Project overview                                ║
echo ║  - GETTING_STARTED.md: Detailed setup guide                   ║
echo ║  - PROMPT_ENGINEERING_GUIDE.md: Prompt best practices         ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
pause
