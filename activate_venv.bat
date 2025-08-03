@echo off
REM Activate the virtual environment 

SET VENV_PATH=venv\Scripts\activate

IF EXIST %VENV_PATH%.bat (
    CALL %VENV_PATH%.bat
) ELSE IF EXIST %VENV_PATH%.ps1 (
    powershell -ExecutionPolicy Bypass -File %VENV_PATH%.ps1
) ELSE (
    echo ❌ Virtual environment not found or activation script missing.
    exit /b 1
)

echo ✅ Virtual environment activated.
echo "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned"
