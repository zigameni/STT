cd "D:\Faklutet Audio"
.\.venv\Scripts\Activate
python.exe .\main_script.py .\audio\
:: Add Git commands
git add .
git commit -m "Auto-commit before shutdown - work"
git push origin main  :: Change 'main' to your actual branch name
:: Shutdown the system
shutdown /s /f /t 0