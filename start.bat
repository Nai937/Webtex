@echo off
title Valentine Message App
echo ========================================
echo   Valentine Message App - Morakot Square
echo ========================================
echo.
echo Starting Admin Panel...
start "" "index.html"
echo.
echo Starting Display Screen...
timeout /t 2 >nul
start "" "display.html"
echo.
echo ========================================
echo   App started successfully!
echo   - Admin Panel: index.html
echo   - Display: display.html
echo ========================================
echo.
pause
