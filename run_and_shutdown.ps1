# PowerShell script - run_and_shutdown.ps1

# Change directory to Faklutet Audio
Set-Location "D:\Faklutet Audio"
if (-not $?) {
    Write-Error "Error: Could not change directory to 'D:\Faklutet Audio'"
    return
}

# Activate virtual environment
Write-Host "Activating virtual environment..."
.\.venv\Scripts\Activate.ps1
if (-not $?) {
    Write-Error "Error: Could not activate virtual environment."
    return
}
Write-Host "Virtual environment activated."

# Run main_script.py
Write-Host "Running main_script.py..."
python.exe .\main_script.py .\audio\
if ($LASTEXITCODE -ne 0) {
    Write-Error "Error: main_script.py script failed."
    return
}
Write-Host "main_script.py script completed."

# Run clean.py script
Write-Host "Running clean.py script..."
python.exe .\clean.py .\output\
if ($LASTEXITCODE -ne 0) {
    Write-Error "Error: clean.py script failed."
    return
}
Write-Host "clean.py script completed."

# Move output folder
Write-Host "Moving output folder..."
Move-Item -Path "output" -Destination "C:\Users\korisnik\Desktop\WORKSPACE\Faklutet_code" -Force
if (-not $?) {
    Write-Error "Error: Could not move output folder."
    return
}
Write-Host "output folder moved."

# Change directory to WORKSPACE\Faklutet_code
Set-Location "C:\Users\korisnik\Desktop\WORKSPACE\Faklutet_code"
if (-not $?) {
    Write-Error "Error: Could not change directory to 'C:\Users\korisnik\Desktop\WORKSPACE\Faklutet_code'"
    return
}

# Git commands in WORKSPACE\Faklutet_code
Write-Host "Adding Git changes in WORKSPACE..."
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Error "Error: Git add failed in WORKSPACE folder."
    return
}
Write-Host "Committing Git changes in WORKSPACE..."
git commit -m "Auto-commit after processing and moving output folder"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Error: Git commit failed in WORKSPACE folder."
    return
}
Write-Host "Pushing Git changes in WORKSPACE..."
git push
if ($LASTEXITCODE -ne 0) {
    Write-Error "Error: Git push failed in WORKSPACE folder."
    return
}
Write-Host "Git push completed for WORKSPACE."

# Change directory back to D:\Faklutet Audio
Set-Location "D:\Faklutet Audio"
if (-not $?) {
    Write-Error "Error: Could not change directory back to 'D:\Faklutet Audio'"
    return
}

# Git commands in D:\Faklutet Audio (original)
Write-Host "Adding Git changes in Faklutet Audio (original)..."
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Error "Error: Git add failed in Faklutet Audio folder."
    return
}
Write-Host "Committing Git changes in Faklutet Audio (original)..."
git commit -m "Auto-commit before shutdown - work"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Error: Git commit failed in Faklutet Audio folder."
    return
}
Write-Host "Pushing Git changes in Faklutet Audio (original)..."
git push
if ($LASTEXITCODE -ne 0) {
    Write-Error "Error: Git push failed in Faklutet Audio folder."
    return
}
Write-Host "Git push completed for Faklutet Audio."


# Shutdown the system
Write-Host "Shutting down the system..."
shutdown /s /f /t 0

Write-Host "Script execution finished."
#Pause # Keep console open until key is pressed
exit