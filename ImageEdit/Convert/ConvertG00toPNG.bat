@echo off
echo starting to convert g00 to png...
vaconv  -f png -d "png" "g00"/*.g00
echo finish!
PAUSE