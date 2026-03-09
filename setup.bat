@echo off
setlocal
if not exist "C:\tools" (
    mkdir "C:\tools"
)else(echo exist C:\tools)
if exist "img.exe"(
    move /y "img.exe" "C:\tools"
)else(echo not found img.exe or idk)

setx PATH "%PATH%;C:\tools"
echo done