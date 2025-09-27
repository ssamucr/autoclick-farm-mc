# 🖱️ AutoClicker Ssamucr - Minecraft Mob Farm

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License]## ⚠️ Advertencias Importantes

- ⚠️ **Revisa las Reglas:** SIEMPRE verifica las reglas del servidor antes de usar
- ⚠️ **Solo Granjas Propias:** Úsalo solo en tus propias granjas, no en áreas ajenas
- ⚠️ **Supervisión:** No dejar funcionando sin supervisión por largos períodos
- ⚠️ **Servidores Públicos:** Muchos servidores prohíben autoclickers - pueden banearte
- ⚠️ **Posición del Cursor:** Verifica que estés apuntando a los mobs correctamente
- ⚠️ **Comida Suficiente:** Asegúrate de tener suficiente comida en el inventario
- ⚠️ **Zona Segura:** Verifica que los mobs no puedan dañarte desde tu posición//img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://github.com/ssamucr/autoclicker-ssamucr)

Un **AutoClicker especializado para farming de mobs en Minecraft** con interfaz gráfica que permite automatizar el proceso de eliminar mobs en granjas, mantener al personaje alimentado y evitar ser expulsado por sistemas anti-AFK.

## ✨ Características Principales

### 🏠 **AutoClicker para Granjas de Mobs (GUI)**
- **Clic izquierdo automático** cada 1-2 segundos (respeta el cooldown de ataque de Minecraft)
- **Alimentación automática** cada 10 ataques con clic derecho (2 segundos mantenido)
- **Sistema anti-AFK** con salto cada 10 ataques (500ms de barra espaciadora)
- **Interfaz gráfica intuitiva** con controles visuales
- **Configuración de tiempo** personalizable para sesiones de farming
- **Progreso en tiempo real** con barra visual y estadísticas
- **Failsafe integrado** (mouse en esquinas para detener inmediatamente)

### 🎮 **Anti-AFK General para Minecraft**
- **Movimientos automáticos** (W, A, S, D) para exploración
- **Saltos aleatorios** con barra espaciadora
- **Ataques ocasionales** con clic izquierdo
- **Movimiento de cámara** realista
- **Patrones complejos** para evitar detección de sistemas anti-AFK
- **Frecuencia configurable** (1-2 minutos) para uso general

### 🔧 **Versiones Disponibles**
- **Script con GUI** (`autoclick_gui.py`) - Interfaz gráfica completa
- **Script consola** (`autoclick.py`) - Versión ligera por consola
- **Anti-AFK** (`anti-afk.py`) - Especializado para juegos
- **Ejecutable Windows** (`AutoClicker_Ssamucr.exe`) - Sin dependencias

## 🏠 Propósito Específico: Farming de Mobs en Minecraft

### 🎯 **¿Cómo Funciona?**
Este AutoClicker está diseñado específicamente para **automatizar granjas de mobs en Minecraft**:

1. **🗳️ Posicionamiento:** Colócate en una zona segura de tu granja donde puedas alcanzar a los mobs
2. **⚔️ Ataque Automático:** El clic izquierdo cada 1-2 segundos respeta el cooldown de combate
3. **🍖 Alimentación:** El clic derecho cada 10 ataques come automáticamente (mantener comida en mano izquierda)
4. **🚀 Anti-AFK:** Los saltos cada 10 ataques evitan la expulsión por inactividad

### 🛠️ **Configuración Recomendada:**
- **Mano derecha:** Espada, hacha o herramienta de combate
- **Mano izquierda:** Comida (pan, bistec cocido, manzanas doradas, etc.)
- **Posición:** Zona segura donde los mobs estén al alcance pero no puedan dañarte
- **Granja:** Funciona con cualquier tipo de granja de mobs (zombies, skeletons, endermen, etc.)

### ⚙️ **Por Qué Estos Intervalos?**
- **1-2 segundos entre ataques:** Respeta el sistema de cooldown de Minecraft para daño máximo
- **Clic derecho por 2 segundos:** Tiempo necesario para comer completamente en Minecraft
- **Salto cada 10 ataques:** Suficiente movimiento para evitar detección anti-AFK sin interferir

## ⚖️ Uso Responsable y Legal

### ✅ **Donde ES Apropiado Usar:**
- **Mundos de un solo jugador** (singleplayer)
- **Servidores privados** con amigos donde esté permitido
- **Servidores públicos** que explícitamente permiten autoclickers
- **Granjas propias** en tu territorio/base

### ❌ **Donde NO Usar:**
- **Servidores PvP** donde dé ventaja injusta
- **Servidores que prohíben autoclickers** en sus reglas
- **Sistemas de economía** donde afecte el balance del juego
- **Áreas públicas** donde moleste a otros jugadores

### 📜 **Importante:**
**Siempre revisa las reglas del servidor antes de usar**. El uso de autoclickers puede estar prohibido en muchos servidores multiplayer. Este proyecto es para uso educativo y en entornos donde esté permitido.

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

### **AutoClicker para Granjas de Mobs:**
1. **Prepara tu granja:** Construye o encuentra una granja de mobs funcional
2. **Posiciónate:** Colócate en una zona segura donde puedas golpear a los mobs
3. **Equipa tu personaje:**
   - Mano derecha: Espada, hacha o herramienta de combate
   - Mano izquierda: Comida (pan, bistec, manzanas, etc.)
4. **Abre** `AutoClicker_Ssamucr.exe` o ejecuta `python autoclick_gui.py`
5. **Configura** el tiempo de farming (recomendado: 30-60 minutos máximo)
6. **Posiciona** el cursor donde aparezcan los mobs
7. **Presiona** "Iniciar AutoClicker"
8. **Para detener:** Botón "Detener" o mueve el mouse a una esquina

### **Anti-AFK General:**
1. **Abre Minecraft** y entra al servidor/mundo
2. **Ejecuta** `python anti-afk.py`
3. **Configura** la duración deseada
4. **Colócate** en un lugar seguro
5. **El script** realizará movimientos cada 1-2 minutos automáticamente

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

## 📊 Funcionalidades Técnicas para Minecraft

### **🎯 Configuraciones Específicas:**
- **Intervalo de ataque:** 1-2 segundos (respeta cooldown de combate de Minecraft)
- **Sistema de alimentación:** Cada 10 ataques para mantener la salud
- **Anti-AFK:** Saltos periódicos para evitar expulsión por inactividad
- **Gestión de hilos:** Ejecución no bloqueante en interfaz gráfica
- **Manejo de errores:** Recuperación automática de errores menores
- **Compatibilidad:** Funciona con todas las versiones de Minecraft

### **⚙️ Optimizaciones para Farming:**
- **Memoria eficiente:** Uso mínimo de recursos del sistema
- **CPU optimizado:** Pausas apropiadas para no afectar el rendimiento de Minecraft
- **Intervalos inteligentes:** Aleatorios para parecer más humano
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