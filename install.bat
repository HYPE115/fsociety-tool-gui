@echo off
title Installation des prérequis - Security Toolkit
color 0A

echo ==========================================
echo  Installation des prérequis sous Windows
echo ==========================================
echo.

:: Vérification de Python
echo [*] Vérification de Python...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] Python n'est pas installé. Téléchargez-le sur https://www.python.org/downloads/
    pause
    exit /b
) else (
    echo [OK] Python est installé.
)

:: Installation de pip
echo [*] Mise à jour de pip...
python -m ensurepip --upgrade >nul 2>&1
python -m pip install --upgrade pip >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] Une erreur est survenue lors de la mise à jour de pip.
    pause
    exit /b
) else (
    echo [OK] Pip est à jour.
)

:: Installation du module Colorama
echo [*] Installation du module Colorama...
python -m pip install colorama >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] Une erreur est survenue lors de l'installation de Colorama.
    pause
    exit /b
) else (
    echo [OK] Colorama a été installé avec succès.
)

:: Installation des outils externes
echo [*] Installation des outils externes requis...

:: Vérification et installation de Nmap
where nmap >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [*] Téléchargement de Nmap...
    powershell -Command "Start-BitsTransfer -Source https://nmap.org/dist/nmap-7.94-setup.exe -Destination nmap-setup.exe"
    echo [*] Installation de Nmap...
    start /wait nmap-setup.exe /S
    del nmap-setup.exe
    echo [OK] Nmap installé avec succès.
) else (
    echo [OK] Nmap est déjà installé.
)

:: Vérification et installation de Nikto
where nikto >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [*] Téléchargement de Nikto...
    git clone https://github.com/sullo/nikto
    setx PATH "%cd%\nikto-master"
    del nikto.zip
    echo [OK] Nikto installé avec succès.
) else (
    echo [OK] Nikto est déjà installé.
)

:: Vérification et installation de Gobuster
where gobuster >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [*] Téléchargement de Gobuster...
    git clone https://github.com/OJ/gobuster
        echo [OK] Gobuster installé avec succès.
    ) else (
        echo [!] Échec du téléchargement de Gobuster.
    )
) else (
    echo [OK] Gobuster est déjà installé.
)

:: Vérification et installation de Hydra
where hydra >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] Hydra n'est pas disponible en natif sous Windows.
    echo [!] Vous devez utiliser WSL (Windows Subsystem for Linux) ou une machine virtuelle pour utiliser Hydra.
) else (
    echo [OK] Hydra est déjà installé.
)

echo.
echo ==========================================
echo  Installation terminée !
echo  Lancez le script principal avec : 
echo    python security_toolkit.py
echo ==========================================
pause
