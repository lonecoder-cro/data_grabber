@echo off
title "Building DataGrabber"
cls

set name="data_grabber"

pyinstaller  --noconfirm --clean %name%.spec

rmdir /s /q build
rmdir /s /q dist\%name%

pause
