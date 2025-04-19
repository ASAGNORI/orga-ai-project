#!/bin/bash

# Cores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}Running all tests...${NC}\n"

# Frontend Tests
echo -e "${GREEN}Running Frontend Tests...${NC}"
cd frontend
npm run test
npm run test:e2e
cd ..

# Backend Tests
echo -e "\n${GREEN}Running Backend Tests...${NC}"
cd backend
pytest tests/ -v --cov=app --cov-report=term-missing

# Check exit codes
if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}All tests passed successfully!${NC}"
    exit 0
else
    echo -e "\n${RED}Some tests failed!${NC}"
    exit 1
fi 