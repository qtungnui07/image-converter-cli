@echo off
setlocal
if not exist "C:\tools" (
    mkdir "C:\tools"
) else (
    echo C:\tools already exists
)
if exist "%~dp0img.exe" (
    move /y "%~dp0img.exe" "C:\tools\img.exe"
) else (
    echo img.exe not found
)
echo %PATH% | find /i "C:\tools" >nul
if errorlevel 1 (
    setx PATH "%PATH%;C:\tools"
    echo Added C:\tools to PATH
) else (
    echo PATH already contains C:\tools
)
echo Done
pause