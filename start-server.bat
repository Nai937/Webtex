@echo off
title Valentine Message Server
echo ========================================
echo   Valentine Message App - Morakot Square
echo ========================================
echo.
echo Starting local server...
echo.
echo Admin Panel: http://localhost:8000/index.html
echo Display:     http://localhost:8000/display.html
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.
python -m http.server 8000
pause
