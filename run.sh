#!/bin/bash

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Print header
echo -e "${BOLD}${BLUE}Running Python Tests${NC}"
echo -e "${BLUE}====================${NC}\n"

# Run each test
for test_file in basics/test_about*.py; do
    echo -e "${BOLD}${BLUE}Running: $test_file${NC}"
    echo -e "${BLUE}------------------------${NC}"

    # Run the Python test runner with the colored output
    python3 colored_runner.py "$test_file"

    # Check exit status
    if [ $? -ne 0 ]; then
        echo -e "\n${RED}${BOLD}❌ Tests failed in $test_file. Stopping execution.${NC}"
        exit 1
    fi

    echo -e "${GREEN}${BOLD}✓ All tests passed in $test_file${NC}\n"
done

echo -e "${GREEN}${BOLD}✓ All test files completed successfully!${NC}"