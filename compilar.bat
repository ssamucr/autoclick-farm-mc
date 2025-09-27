@echo off
echo ===================================
echo    COMPILADOR AUTOCLICKER SSAMUCR
echo ===================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor instala Python desde python.org
    pause
    exit /b 1
)

echo [1/4] Verificando Python... OK
echo.

REM Instalar dependencias
echo [2/4] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo.

REM Crear directorio de salida si no existe
if not exist "dist" mkdir dist

echo [3/4] Compilando con PyInstaller...
echo Esto puede tomar varios minutos...
echo.

REM Comando PyInstaller con opciones optimizadas
pyinstaller ^
    --onefile ^
    --windowed ^
    --name "AutoClicker_Ssamucr" ^
    --icon=icon.ico ^
    --add-data "requirements.txt;." ^
    --hidden-import=tkinter ^
    --hidden-import=pyautogui ^
    --distpath=dist ^
    --workpath=build ^
    --specpath=build ^
    autoclick_gui.py

if errorlevel 1 (
    echo ERROR: La compilación falló
    pause
    exit /b 1
)

echo.
echo [4/4] Compilación completada!
echo.
echo ===================================
echo        COMPILACION EXITOSA
echo ===================================
echo.
echo El ejecutable se encuentra en:
echo   %cd%\dist\AutoClicker_Ssamucr.exe
echo.
echo Tamaño del archivo:
for %%A in (dist\AutoClicker_Ssamucr.exe) do echo   %%~zA bytes
echo.
echo Puedes copiar este archivo .exe a cualquier computadora
echo con Windows y ejecutarlo sin necesidad de Python.
echo.
echo ¡Presiona cualquier tecla para abrir la carpeta!
pause >nul

REM Abrir la carpeta con el ejecutable
start explorer dist

echo.
echo ¡Listo! El AutoClicker Ssamucr está compilado.
pause