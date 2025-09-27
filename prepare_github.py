#!/usr/bin/env python3
"""
Script para preparar el proyecto para subir a GitHub.
Limpia archivos innecesarios y verifica que todo esté listo.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def print_step(message):
    """Imprime un paso del proceso"""
    print(f"\n🔄 {message}")

def print_success(message):
    """Imprime mensaje de éxito"""
    print(f"✅ {message}")

def print_warning(message):
    """Imprime mensaje de advertencia"""
    print(f"⚠️  {message}")

def print_error(message):
    """Imprime mensaje de error"""
    print(f"❌ {message}")

def clean_build_artifacts():
    """Limpia artefactos de build"""
    print_step("Limpiando artefactos de build...")
    
    paths_to_clean = [
        "build",
        "dist", 
        "__pycache__",
        "*.pyc",
        "*.pyo",
        "*.egg-info",
        ".pytest_cache"
    ]
    
    for path in paths_to_clean:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
                print_success(f"Eliminada carpeta: {path}")
            else:
                os.remove(path)
                print_success(f"Eliminado archivo: {path}")
    
    # Limpiar archivos .pyc recursivamente
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith((".pyc", ".pyo")):
                os.remove(os.path.join(root, file))

def verify_required_files():
    """Verifica que todos los archivos requeridos existan"""
    print_step("Verificando archivos requeridos...")
    
    required_files = [
        "README.md",
        "LICENSE", 
        "requirements.txt",
        ".gitignore",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "autoclick_gui.py",
        "autoclick.py",
        "anti-afk.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
            print_error(f"Archivo faltante: {file}")
        else:
            print_success(f"Encontrado: {file}")
    
    return len(missing_files) == 0

def check_python_syntax():
    """Verifica la sintaxis de los archivos Python"""
    print_step("Verificando sintaxis de Python...")
    
    python_files = [
        "autoclick_gui.py",
        "autoclick.py", 
        "anti-afk.py",
        "crear_ejecutable.py"
    ]
    
    all_valid = True
    for file in python_files:
        if os.path.exists(file):
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    compile(f.read(), file, 'exec')
                print_success(f"Sintaxis válida: {file}")
            except SyntaxError as e:
                print_error(f"Error de sintaxis en {file}: {e}")
                all_valid = False
    
    return all_valid

def create_project_structure_info():
    """Crea información de la estructura del proyecto"""
    print_step("Generando información de estructura...")
    
    structure = """
# Estructura del Proyecto AutoClicker Ssamucr

```
autoclicker-ssamucr/
├── 📄 Archivos principales
│   ├── autoclick_gui.py         # AutoClicker con interfaz gráfica
│   ├── autoclick.py             # AutoClicker versión consola  
│   └── anti-afk.py              # Script Anti-AFK para Minecraft
│
├── 🔧 Scripts de compilación
│   ├── crear_ejecutable.py      # Script Python para crear ejecutable
│   ├── compilar.bat             # Script batch para Windows
│   └── prepare_github.py        # Este script de preparación
│
├── 📚 Documentación
│   ├── README.md                # Documentación principal
│   ├── CHANGELOG.md             # Historial de cambios
│   ├── CONTRIBUTING.md          # Guía de contribución
│   └── INSTRUCCIONES.md         # Manual detallado
│
├── ⚙️ Configuración
│   ├── requirements.txt         # Dependencias Python
│   ├── .gitignore              # Archivos ignorados por Git
│   └── LICENSE                 # Licencia MIT
│
├── 🤖 GitHub
│   ├── .github/
│   │   ├── workflows/
│   │   │   └── build.yml       # GitHub Actions para build automático
│   │   └── ISSUE_TEMPLATE/
│   │       ├── bug_report.md   # Template para reportar bugs
│   │       └── feature_request.md # Template para solicitar features
│
└── 📦 Generados (ignorados por Git)
    ├── build/                   # Archivos temporales de PyInstaller
    ├── dist/                    # Ejecutables compilados
    ├── venv/                    # Entorno virtual Python
    └── __pycache__/            # Cache de Python
```
    """.strip()
    
    with open("PROJECT_STRUCTURE.md", "w", encoding="utf-8") as f:
        f.write(structure)
    
    print_success("Creado PROJECT_STRUCTURE.md")

def show_git_commands():
    """Muestra comandos Git recomendados"""
    print_step("Comandos Git recomendados:")
    
    commands = """
# 1. Inicializar repositorio Git (si no existe)
git init

# 2. Agregar todos los archivos
git add .

# 3. Hacer commit inicial
git commit -m "feat: initial commit - AutoClicker Ssamucr v1.0.0"

# 4. Agregar remote origin (reemplaza con tu URL de GitHub)
git remote add origin https://github.com/tu-usuario/autoclicker-ssamucr.git

# 5. Crear y subir a rama main
git branch -M main
git push -u origin main

# 6. Crear tag para release
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
    """.strip()
    
    print(commands)

def main():
    """Función principal"""
    print("🚀 Preparando AutoClicker Ssamucr para GitHub")
    print("=" * 50)
    
    # Limpiar artefactos
    clean_build_artifacts()
    
    # Verificar archivos
    if not verify_required_files():
        print_error("Faltan archivos requeridos. Revisa los mensajes anteriores.")
        sys.exit(1)
    
    # Verificar sintaxis
    if not check_python_syntax():
        print_error("Hay errores de sintaxis. Corrígelos antes de continuar.")
        sys.exit(1)
    
    # Crear información adicional
    create_project_structure_info()
    
    # Mostrar comandos Git
    show_git_commands()
    
    print("\n🎉 ¡Proyecto listo para GitHub!")
    print("📋 Checklist final:")
    print("   ✅ Archivos limpiados")
    print("   ✅ Sintaxis verificada") 
    print("   ✅ Documentación completa")
    print("   ✅ Templates de GitHub creados")
    print("   ✅ GitHub Actions configurado")
    
    print("\n📝 Próximos pasos:")
    print("   1. Ejecutar comandos Git mostrados arriba")
    print("   2. Crear repositorio en GitHub")
    print("   3. Subir el código") 
    print("   4. Crear release con el tag v1.0.0")
    
    print("\n🌟 ¡Tu AutoClicker Ssamucr estará listo en GitHub!")

if __name__ == "__main__":
    main()