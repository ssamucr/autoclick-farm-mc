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