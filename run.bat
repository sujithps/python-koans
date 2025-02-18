@echo off
setlocal EnableDelayedExpansion

:: Color codes
set "GREEN=0A"
set "RED=0C"
set "YELLOW=0E"
set "BLUE=0B"
set "WHITE=0F"

:: Set test directory
set "TEST_DIR=basics"

:: Clear screen
cls
title Python Test Runner

:: Check if basics directory exists
if not exist "%TEST_DIR%" (
    color %RED%
    echo Error: '%TEST_DIR%' directory not found!
    echo Please make sure the directory exists and contains test files.
    pause
    exit /b 1
)

:: Print header
color %BLUE%
echo Running Python Tests from '%TEST_DIR%' folder
echo ============================================
echo.

:: List test files
color %YELLOW%
cd %TEST_DIR%

:: Run each test file
for %%f in (test_about*.py) do (
    :: Print current test file in blue
    color %BLUE%
    echo Running: %%f
    echo ------------------------

    :: Run the test with python -m to handle imports correctly
    python -m unittest -v %%f

    :: Check if test failed
    if errorlevel 1 (
        color %RED%
        echo.
        echo [X] Tests failed in %%f. Stopping execution.
        echo.
        cd ..
        pause
        exit /b 1
    ) else (
        color %GREEN%
        echo.
        echo [√] All tests passed in %%f
        echo.
    )
)

:: Return to original directory
cd ..

:: Print success message
color %GREEN%
echo [√] All test files completed successfully!
echo.

:: Reset color
color %WHITE%

:: Pause to see results
pause
exit /b 0