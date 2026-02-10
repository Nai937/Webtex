@echo off
title Valentine Message Server
echo ========================================
echo   Valentine Message App - Morakot Square
echo ========================================
echo.
echo Starting local server with Node.js...
echo.
echo Admin Panel: http://localhost:8000/index.html
echo Display:     http://localhost:8000/display.html
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.
npx serve -p 8000
pause
