#!/bin/bash

# AI Workplace Productivity Assistant - Setup & Run Script
# This script sets up and runs the entire application (web + API)

set -e

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     🤖 AI WORKPLACE PRODUCTIVITY ASSISTANT - SETUP 🤖         ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python installation
echo -e "${BLUE}[1/5]${NC} Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}⚠️  Python3 not found. Please install Python 3.8 or higher.${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✓${NC} Found: $PYTHON_VERSION"
echo ""

# Create virtual environment
echo -e "${BLUE}[2/5]${NC} Setting up virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓${NC} Virtual environment created"
else
    echo -e "${GREEN}✓${NC} Virtual environment already exists"
fi

# Activate virtual environment
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate

echo -e "${GREEN}✓${NC} Virtual environment activated"
echo ""

# Install dependencies
echo -e "${BLUE}[3/5]${NC} Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r api/requirements.txt
echo -e "${GREEN}✓${NC} Dependencies installed"
echo ""

# Create logs directory
echo -e "${BLUE}[4/5]${NC} Setting up logging..."
mkdir -p logs
touch logs/api.log
touch logs/app.log
echo -e "${GREEN}✓${NC} Logging configured"
echo ""

# Check and create .env files
echo -e "${BLUE}[5/5]${NC} Checking configuration files..."
if [ ! -f "api/.env" ]; then
    echo -e "${YELLOW}⚠️  Creating api/.env from template...${NC}"
    cp api/.env.example api/.env
    echo -e "${YELLOW}⚠️  Please update api/.env with your OPENAI_API_KEY${NC}"
fi
echo -e "${GREEN}✓${NC} Configuration ready"
echo ""

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                    ✅ SETUP COMPLETE                          ║"
echo "║                                                                ║"
echo "║  To start the application:                                    ║"
echo "║                                                                ║"
echo "║  1. API Server (Terminal 1):                                  ║"
echo "║     source venv/bin/activate                                  ║"
echo "║     python api/server.py                                      ║"
echo "║                                                                ║"
echo "║  2. Web App (Terminal 2):                                     ║"
echo "║     Open web-app/index.html in your browser                   ║"
echo "║     Or use: python -m http.server 8000                        ║"
echo "║                                                                ║"
echo "║  Documentation:                                               ║"
echo "║  - README.md: Project overview                                ║"
echo "║  - GETTING_STARTED.md: Detailed setup guide                   ║"
echo "║  - PROMPT_ENGINEERING_GUIDE.md: Prompt best practices         ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
