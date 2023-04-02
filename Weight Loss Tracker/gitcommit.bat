@echo off
:TOP
cd "D:/Skills/Python/Projects/Weight Loss Tracker"
git stage .
git commit -m "Update"
git push origin master
goto :TOP
