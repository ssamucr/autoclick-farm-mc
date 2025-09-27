# 🖱️ AutoClicker Ssamucr

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://github.com/ssamucr/autoclicker-ssamucr)

Un **AutoClicker** avanzado con interfaz gráfica para Windows que permite automatizar clics, pulsaciones de teclas y movimientos del mouse de forma inteligente y segura.

## ✨ Características Principales

### 🖱️ **AutoClicker Pro (GUI)**
- **Clics automáticos** cada 1-2 segundos (intervalo aleatorio)
- **Barra espaciadora** cada 10 clics (mantenida 500ms)
- **Clic derecho** cada 10 clics (mantenido 2 segundos)
- **Interfaz gráfica intuitiva** con controles visuales
- **Configuración de tiempo** personalizable
- **Progreso en tiempo real** con barra visual
- **Failsafe integrado** (mouse en esquinas para detener)

### 🎮 **Anti-AFK para Minecraft**
- **Movimientos automáticos** (W, A, S, D)
- **Saltos aleatorios** con barra espaciadora
- **Ataques ocasionales** con clic izquierdo
- **Movimiento de cámara** realista
- **Patrones complejos** para evitar detección
- **Frecuencia configurable** (1-2 minutos)

### 🔧 **Versiones Disponibles**
- **Script con GUI** (`autoclick_gui.py`) - Interfaz gráfica completa
- **Script consola** (`autoclick.py`) - Versión ligera por consola
- **Anti-AFK** (`anti-afk.py`) - Especializado para juegos
- **Ejecutable Windows** (`AutoClicker_Ssamucr.exe`) - Sin dependencias

## 🚀 Instalación y Uso

### Método 1: Ejecutable (Recomendado)
1. **Descarga** el ejecutable desde [Releases](../../releases)
2. **Ejecuta** `AutoClicker_Ssamucr.exe`
3. **¡No requiere Python ni instalación!**

### Método 2: Desde Código Fuente
1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/ssamucr/autoclicker-ssamucr.git
   cd autoclicker-ssamucr
   ```

2. **Instala dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   # Interfaz gráfica
   python autoclick_gui.py
   
   # Versión consola
   python autoclick.py
   
   # Anti-AFK para Minecraft
   python anti-afk.py
   ```

### Método 3: Crear tu Propio Ejecutable
1. **Instala PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Usa el script automático:**
   ```bash
   python crear_ejecutable.py
   ```

3. **O manualmente:**
   ```bash
   pyinstaller --onefile --windowed --name "AutoClicker_Ssamucr" autoclick_gui.py
   ```

## 📋 Requisitos del Sistema

- **Sistema Operativo:** Windows 10/11
- **Python:** 3.8+ (solo para versión de código fuente)
- **RAM:** 50MB mínimo
- **Espacio:** 15MB para ejecutable, 5MB para código fuente

### 🔗 Dependencias (Para Código Fuente)
- `pyautogui>=0.9.54` - Automatización de GUI
- `pyinstaller>=6.10.0` - Creación de ejecutables

## 🎯 Cómo Usar

### **AutoClicker GUI:**
1. **Abre** `AutoClicker_Ssamucr.exe` o ejecuta `python autoclick_gui.py`
2. **Configura** la duración en minutos
3. **Posiciona** el cursor donde quieres hacer clic
4. **Presiona** "Iniciar AutoClicker"
5. **Para detener:** Botón "Detener" o mueve el mouse a una esquina

### **Anti-AFK Minecraft:**
1. **Abre Minecraft** y entra al servidor/mundo
2. **Ejecuta** `python anti-afk.py`
3. **Configura** la duración deseada
4. **Colócate** en un lugar seguro en el juego
5. **El script** realizará acciones cada 1-2 minutos automáticamente

## ⚠️ Advertencias Importantes

- ⚠️ **Uso Responsable:** Solo usar donde esté permitido
- ⚠️ **Juegos Online:** Algunos servidores pueden detectar y banear bots
- ⚠️ **Posición del Mouse:** Verifica la posición antes de iniciar
- ⚠️ **Supervisión:** No dejar funcionando sin supervisión por largos períodos
- ⚠️ **Failsafe:** Siempre mantén activado el failsafe (habilitado por defecto)

## 🛡️ Seguridad y Failsafe

### **Métodos de Detención de Emergencia:**
- **Mouse en Esquinas:** Mueve el cursor a cualquier esquina de la pantalla
- **Botón Detener:** En la interfaz gráfica
- **Ctrl+C:** En versiones de consola
- **Cerrar Ventana:** Botón X o Alt+F4

### **Antivirus:**
Algunos antivirus pueden detectar falsamente el ejecutable debido a:
- Uso de automatización de GUI (`pyautogui`)
- Empaquetado con PyInstaller

**Solución:** Agregar excepción en el antivirus para la carpeta del proyecto.

## 📁 Estructura del Proyecto

```
autoclicker-ssamucr/
├── README.md                 # Este archivo
├── LICENSE                   # Licencia MIT
├── requirements.txt          # Dependencias Python
├── .gitignore               # Archivos ignorados por Git
├── CHANGELOG.md             # Historial de cambios
├── INSTRUCCIONES.md         # Manual detallado
├── 
├── autoclick_gui.py         # AutoClicker con interfaz gráfica
├── autoclick.py             # AutoClicker versión consola
├── anti-afk.py              # Script Anti-AFK para Minecraft
├── 
├── crear_ejecutable.py      # Script para crear ejecutable
├── compilar.bat             # Compilación automática (Windows)
├── 
└── dist/                    # Ejecutables compilados
    └── AutoClicker_Ssamucr.exe
```

## 🔧 Desarrollo y Contribución

### **Configurar Entorno de Desarrollo:**
```bash
# Clonar repositorio
git clone https://github.com/ssamucr/autoclicker-ssamucr.git
cd autoclicker-ssamucr

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
.\venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### **Contribuir:**
1. Fork del repositorio
2. Crear rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crear Pull Request

## 📊 Funcionalidades Técnicas

### **Configuraciones Avanzadas:**
- **Intervalos aleatorios:** 1-2 segundos entre clics para parecer humano
- **Múltiples acciones:** Combina clics, teclas y movimientos
- **Gestión de hilos:** Ejecución no bloqueante en interfaz gráfica
- **Manejo de errores:** Recuperación automática de errores menores
- **Multiplataforma base:** Código adaptable a otros sistemas operativos

### **Optimizaciones:**
- **Memoria eficiente:** Uso mínimo de recursos del sistema
- **CPU optimizado:** Pausas apropiadas para no sobrecargar el sistema
- **Compilación optimizada:** Ejecutable de tamaño reducido con PyInstaller

## 🆘 Solución de Problemas

### **Errores Comunes:**

**"Python no encontrado"**
- Instala Python desde [python.org](https://python.org)
- Asegúrate de marcar "Add to PATH"

**"PyInstaller no encontrado"**
- Ejecuta: `pip install pyinstaller`

**"Permisos denegados"**
- Ejecuta como Administrador
- Verifica permisos de escritura en la carpeta

**"El ejecutable es muy grande"**
- Es normal (~13-15 MB), contiene Python completo
- Considera usar la versión de código fuente para menor espacio

## 📞 Soporte

- **Issues:** [GitHub Issues](../../issues)
- **Documentación:** [Wiki del Proyecto](../../wiki)
- **Releases:** [Descargas](../../releases)

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ve el archivo [LICENSE](LICENSE) para más detalles.

## 🌟 Agradecimientos

- **PyAutoGUI:** Por la excelente biblioteca de automatización
- **PyInstaller:** Por hacer posible la creación de ejecutables
- **Comunidad Python:** Por las herramientas y conocimiento compartido

---

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub**

**🐛 Reporta bugs o solicita features en [Issues](../../issues)**

**🤝 Las contribuciones son bienvenidas - ve [CONTRIBUTING.md](CONTRIBUTING.md)**