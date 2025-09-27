# Changelog

Todos los cambios importantes de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-09-27

### ✨ Agregado
- **AutoClicker GUI** - Interfaz gráfica completa con tkinter
- **AutoClicker Consola** - Versión ligera para línea de comandos
- **Anti-AFK Minecraft** - Script especializado para evitar AFK en juegos
- **Compilador automático** - Scripts para crear ejecutables con PyInstaller
- **Failsafe integrado** - Detención de emergencia moviendo mouse a esquinas
- **Intervalos aleatorios** - Clics cada 1-2 segundos para parecer humano
- **Acciones múltiples** - Combina clics, barra espaciadora y clic derecho
- **Configuración de tiempo** - Duración personalizable
- **Progreso visual** - Barra de progreso y estadísticas en tiempo real

### 🛠️ Características Técnicas
- **Gestión de hilos** - Ejecución no bloqueante en GUI
- **Manejo robusto de errores** - Recuperación automática
- **Compilación optimizada** - Ejecutable de ~13MB con PyInstaller
- **Multiplataforma base** - Código adaptable a otros OS

### 📝 Funcionalidades Específicas

#### AutoClicker GUI (`autoclick_gui.py`)
- Interfaz gráfica intuitiva con controles visuales
- Configuración de duración en minutos
- Visualización de posición del mouse
- Progreso con barra visual y tiempo restante
- Botones de inicio/parada
- Información de seguridad integrada
- Manejo de cierre de ventana mejorado

#### AutoClicker Consola (`autoclick.py`)
- Versión ligera por línea de comandos
- Duración fija de 30 minutos (8 horas en código)
- Countdown de 3 segundos antes de iniciar
- Estadísticas de progreso cada 10 clics

#### Anti-AFK Minecraft (`anti-afk.py`)
- Movimientos automáticos (W, A, S, D)
- Saltos aleatorios con barra espaciadora
- Ataques ocasionales con clic izquierdo
- Movimiento de cámara realista
- Patrones de movimiento complejos
- Frecuencia configurable (1-2 minutos)
- Duración personalizable

### 🔧 Scripts de Compilación
- `crear_ejecutable.py` - Script automático Python
- `compilar.bat` - Script por lotes para Windows
- Detección automática de dependencias
- Configuración optimizada de PyInstaller

### ⚡ Optimizaciones
- **Memoria eficiente** - Uso mínimo de recursos
- **CPU optimizado** - Pausas apropiadas
- **Intervalos inteligentes** - Aleatorización para evitar detección
- **Compilación limpia** - Exclusión de archivos innecesarios

### 🛡️ Seguridad
- Failsafe habilitado por defecto
- Múltiples métodos de detención
- Confirmación antes de cierre durante ejecución
- Manejo seguro de hilos y procesos

### 📚 Documentación
- README.md completo
- Instrucciones detalladas de instalación
- Guías de uso para cada componente
- Solución de problemas comunes
- Documentación de desarrollo

### 🔄 Acciones Automáticas
- **Clic izquierdo** cada 1-2 segundos
- **Barra espaciadora** cada 10 clics (500ms presionada)
- **Clic derecho** cada 10 clics (2 segundos presionado)
- **Movimientos de mouse** para Anti-AFK
- **Combinaciones de teclas** para juegos

---

## [Próximas Versiones] - Planificado

### 🚀 Por Implementar
- [ ] **Soporte multiplataforma** - Linux y macOS
- [ ] **Configuraciones avanzadas** - Intervalos personalizables
- [ ] **Profiles/Perfiles** - Configuraciones guardadas
- [ ] **Hotkeys globales** - Controles desde cualquier ventana
- [ ] **Logging detallado** - Archivos de registro
- [ ] **Interfaz mejorada** - Temas y personalización
- [ ] **Auto-updater** - Actualizaciones automáticas
- [ ] **Detección de ventana** - Auto-enfoque en aplicaciones específicas

### 🔮 Ideas Futuras
- **Plugin system** - Extensiones personalizadas
- **Grabación de macros** - Reproducir secuencias complejas
- **Integración con juegos** - APIs específicas por juego
- **Modo stealth** - Evitar detección avanzada
- **Estadísticas extendidas** - Reportes detallados
- **Backup de configuraciones** - Sincronización en la nube

---

## 📋 Notas de Versión

### Compatibilidad
- **Python:** 3.8+ requerido
- **OS:** Windows 10/11 principalmente
- **Dependencias:** pyautogui, pyinstaller

### Problemas Conocidos
- Algunos antivirus pueden detectar falsamente el ejecutable
- Alt+F4 puede tener limitaciones en ciertas configuraciones de Windows
- Rendimiento puede variar según el hardware del sistema

### Créditos
- **PyAutoGUI** por la excelente biblioteca de automatización
- **PyInstaller** por facilitar la creación de ejecutables
- **Comunidad Python** por herramientas y recursos

---

*Para reportar bugs o solicitar features, visita [GitHub Issues](../../issues)*