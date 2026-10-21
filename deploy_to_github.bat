@echo off
title Veritas AI - Deploy to GitHub Pages
color 0B
echo ======================================================================
echo          VERITAS AI CONTENT VERIFICATION PLATFORM
echo               GitHub Pages 1-Click Deployment Tool
echo ======================================================================
echo.
echo This tool will publish your website to GitHub Pages so you can access
echo it from any phone, tablet, laptop, or desktop across the world!
echo.
set /p GHUSER="Enter your GitHub Username: "
if "%GHUSER%"=="" (
    echo Username cannot be empty. Please run again.
    pause
    exit /b
)

echo.
echo [1/3] Configuring Git remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/%GHUSER%/veritas-ai-portal.git

echo.
echo [2/3] Uploading code to GitHub...
echo (If prompted, sign in via the browser window that pops up)
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo [!] If the push failed, please make sure you created the empty
    echo     repository named 'veritas-ai-portal' at:
    echo     https://github.com/new
    echo.
    pause
    exit /b
)

echo.
echo [3/3] Repository uploaded successfully!
echo.
echo ======================================================================
echo                     FINAL STEP TO GET YOUR LIVE LINK
echo ======================================================================
echo 1. Open this link in your browser:
echo    https://github.com/%GHUSER%/veritas-ai-portal/settings/pages
echo.
echo 2. Under "Build and deployment" -^> "Branch":
echo    Select "main" and folder "/ (root)", then click "Save".
echo.
echo 3. In about 30 seconds, your site is live worldwide at:
echo.
echo    👉  https://%GHUSER%.github.io/veritas-ai-portal/
echo.
echo ======================================================================
echo You can open this link on your phone, tablet, or any other computer!
echo.
pause
