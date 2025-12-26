#!/bin/bash
# Installation script for MarunochiAI

set -e

echo "========================================="
echo "MarunochiAI Installation"
echo "========================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${BLUE}Checking Python version...${NC}"
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $PYTHON_VERSION"

if [[ $(python3 -c "import sys; print(sys.version_info >= (3, 11))") != "True" ]]; then
    echo -e "${YELLOW}Warning: Python 3.11+ recommended${NC}"
fi

# Check Ollama
echo ""
echo -e "${BLUE}Checking Ollama...${NC}"
if command -v ollama &> /dev/null; then
    echo -e "${GREEN}✓ Ollama installed${NC}"
    ollama --version

    # Check if Ollama is running
    if curl -s http://localhost:11434 > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Ollama is running${NC}"
    else
        echo -e "${YELLOW}⚠ Ollama not running. Starting...${NC}"
        brew services start ollama
        sleep 3
    fi
else
    echo -e "${YELLOW}⚠ Ollama not found. Please install first.${NC}"
    echo "Run: brew install ollama"
    exit 1
fi

# Check models
echo ""
echo -e "${BLUE}Checking Qwen2.5-Coder models...${NC}"
MODELS=$(ollama list | grep "qwen2.5-coder" || true)

if echo "$MODELS" | grep -q "7b"; then
    echo -e "${GREEN}✓ Qwen2.5-Coder 7B found${NC}"
else
    echo -e "${YELLOW}⚠ Qwen2.5-Coder 7B not found${NC}"
    read -p "Download now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ollama pull qwen2.5-coder:7b
    fi
fi

if echo "$MODELS" | grep -q "14b"; then
    echo -e "${GREEN}✓ Qwen2.5-Coder 14B found${NC}"
else
    echo -e "${YELLOW}⚠ Qwen2.5-Coder 14B not found${NC}"
    read -p "Download now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ollama pull qwen2.5-coder:14b
    fi
fi

# Install Python dependencies
echo ""
echo -e "${BLUE}Installing Python dependencies...${NC}"
pip install -e .

# Create data directories
echo ""
echo -e "${BLUE}Creating data directories...${NC}"
mkdir -p data/{chroma,logs,training}
mkdir -p models/fine_tuned
echo -e "${GREEN}✓ Directories created${NC}"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo -e "${BLUE}Creating .env file...${NC}"
    cp .env.example .env
    echo -e "${GREEN}✓ .env created (edit as needed)${NC}"
fi

# Test installation
echo ""
echo -e "${BLUE}Testing installation...${NC}"
python3 -c "from marunochithe.core.inference import InferenceEngine; print('✓ Import successful')"

echo ""
echo "========================================="
echo -e "${GREEN}✓ Installation Complete!${NC}"
echo "========================================="
echo ""
echo "Next steps:"
echo "  1. Test CLI: marunochithe chat 'Hello MarunochiAI'"
echo "  2. Start server: marunochithe server"
echo "  3. Read docs: cat README.md"
echo ""
echo -e "${BLUE}Happy coding with MarunochiAI! 🚀${NC}"
