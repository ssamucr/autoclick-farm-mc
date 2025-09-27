# 🚀 AutoClicker Pro - Crear Ejecutable de Windows

## 📋 Pasos para crear tu ejecutable .exe

### Método 1: Script Automático (Recomendado)

1. **Abrir PowerShell o CMD** en la carpeta del proyecto
2. **Ejecutar el script automático:**
   ```bash
   python crear_ejecutable.py
   ```
3. **¡Listo!** El ejecutable estará en la carpeta `dist/`

### Método 2: Script por lotes (Windows)

1. **Hacer doble clic** en `compilar.bat`
2. **Esperar** a que termine la compilación
3. **El ejecutable** aparecerá en la carpeta `dist/`

### Método 3: Manual

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Crear ejecutable:**
   ```bash
   pyinstaller --onefile --windowed --name "AutoClicker_Pro" autoclick_gui.py
   ```

## 📁 Estructura de archivos

```
autoclick-python/
├── autoclick.py          # Script original (consola)
├── autoclick_gui.py      # Versión con interfaz gráfica
├── anti-afk.py          # Script anti-AFK para Minecraft
├── requirements.txt      # Dependencias Python
├── compilar.bat         # Script de compilación (Windows)
├── crear_ejecutable.py  # Script automático Python
├── INSTRUCCIONES.md     # Este archivo
└── dist/                # Carpeta con el ejecutable final
    └── AutoClicker_Pro.exe
```

## ✨ Características del ejecutable

- ✅ **Archivo único**: No necesita instalación
- ✅ **Portable**: Copia y ejecuta en cualquier PC Windows
- ✅ **Sin Python**: No requiere Python instalado
- ✅ **Interfaz gráfica**: Fácil de usar
- ✅ **Todas las funciones**: Igual que el script original

## 🎮 Funciones incluidas

### AutoClicker Pro (GUI)
- 🖱️ **Clics automáticos** cada 1-2 segundos
- ⌨️ **Barra espaciadora** cada 10 clics (500ms)
- 🖱️ **Clic derecho** cada 10 clics (2 segundos)
- ⏱️ **Duración configurable**
- 📊 **Progreso en tiempo real**
- 🛑 **Botones de control** (Iniciar/Detener)
- ⚠️ **Failsafe**: Mover mouse a esquina para detener

## 🔧 Solución de problemas

### Error: "Python no encontrado"
- Instala Python desde [python.org](https://python.org)
- Asegúrate de marcar "Add to PATH" durante la instalación

### Error: "PyInstaller no encontrado"
- Ejecuta: `pip install pyinstaller`

### Error: "No se puede crear el ejecutable"
- Verifica que tienes permisos de escritura en la carpeta
- Cierra cualquier antivirus que pueda bloquear la compilación

### El ejecutable es muy grande
- Es normal, contiene Python completo (~20-50 MB)
- Para reducir tamaño, usa `--exclude-module` con módulos innecesarios

## 📱 Uso del ejecutable

1. **Ejecuta** `AutoClicker_Pro.exe`
2. **Configura** el tiempo deseado
3. **Posiciona** el cursor donde quieres hacer clic
4. **Presiona** "Iniciar AutoClicker"
5. **Mueve el mouse a una esquina** para detener de emergencia

## ⚠️ Advertencias importantes

- ⚠️ **Uso responsable**: Solo usar donde esté permitido
- ⚠️ **Juegos**: Algunos juegos pueden detectar y banear por uso de bots
- ⚠️ **Posición**: Verifica la posición del mouse antes de iniciar
- ⚠️ **Duración**: No usar por períodos excesivamente largos

## 🛡️ Antivirus

Algunos antivirus pueden detectar falsamente el ejecutable como malware debido a:
- Uso de `pyautogui` (simula acciones del usuario)
- Empaquetado con PyInstaller

**Solución**: Agregar excepción en el antivirus para la carpeta del proyecto.

## 📞 Soporte

Si tienes problemas:
1. Revisa que todos los archivos estén en su lugar
2. Verifica que Python esté correctamente instalado
3. Ejecuta los comandos paso a paso manualmente
4. Comprueba los permisos de la carpeta

¡Disfruta tu AutoClicker Pro! 🎉