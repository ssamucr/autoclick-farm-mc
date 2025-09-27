import os
import subprocess
import sys

def install_requirements():
    """Instala las dependencias necesarias"""
    print("📦 Instalando dependencias...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError:
        print("❌ Error instalando dependencias")
        return False

def create_executable():
    """Crea el ejecutable con PyInstaller"""
    print("🔧 Compilando ejecutable...")
    
    # Comando PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",           # Un solo archivo
        "--windowed",          # Sin ventana de consola
        "--name", "AutoClicker_Ssamucr",  # Nombre del ejecutable
        "--distpath=dist",     # Carpeta de salida
        "--workpath=build",    # Carpeta temporal
        "--specpath=build",    # Archivos de configuración
        "autoclick_gui.py"     # Archivo principal
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✅ Ejecutable creado exitosamente!")
        print(f"📍 Ubicación: {os.path.abspath('dist/AutoClicker_Ssamucr.exe')}")
        return True
    except subprocess.CalledProcessError:
        print("❌ Error creando el ejecutable")
        return False
    except FileNotFoundError:
        print("❌ PyInstaller no encontrado. Instalando...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            return create_executable()  # Intentar de nuevo
        except subprocess.CalledProcessError:
            print("❌ No se pudo instalar PyInstaller")
            return False

def main():
    print("="*50)
    print("🚀 CREADOR DE EJECUTABLE - AUTOCLICKER SSAMUCR")
    print("="*50)
    print()
    
    # Verificar que existe el archivo principal
    if not os.path.exists("autoclick_gui.py"):
        print("❌ Error: No se encuentra autoclick_gui.py")
        input("Presiona Enter para salir...")
        return
    
    # Paso 1: Instalar dependencias
    if not install_requirements():
        input("Presiona Enter para salir...")
        return
    
    print()
    
    # Paso 2: Crear ejecutable
    if not create_executable():
        input("Presiona Enter para salir...")
        return
    
    print()
    print("🎉 ¡PROCESO COMPLETADO!")
    print()
    print("📂 Tu ejecutable está en la carpeta 'dist'")
    print("💾 Puedes copiar AutoClicker_Ssamucr.exe a cualquier PC con Windows")
    print("🔧 No necesitas Python instalado para ejecutarlo")
    
    # Abrir carpeta
    try:
        os.startfile("dist")
        print("📁 Abriendo carpeta de destino...")
    except:
        pass
    
    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()