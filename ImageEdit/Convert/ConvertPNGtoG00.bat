@echo off
cls
echo starting to convert png to g00...
vaconv -d "g00" "png"/*.png "png"/*.xml
echo finish!
PAUSE