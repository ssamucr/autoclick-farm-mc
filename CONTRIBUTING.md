# Contribuir a AutoClicker Ssamucr

¡Gracias por tu interés en contribuir! 🎉

## 🚀 Formas de Contribuir

### 🐛 Reportar Bugs
- Usa el [template de bug report](../../issues/new?template=bug_report.md)
- Incluye pasos para reproducir el problema
- Agrega capturas de pantalla si es relevante
- Especifica tu versión de Windows y Python

### ✨ Solicitar Features
- Usa el [template de feature request](../../issues/new?template=feature_request.md)
- Describe claramente la funcionalidad deseada
- Explica por qué sería útil
- Proporciona ejemplos de uso

### 🔧 Contribuir Código

#### Configurar Entorno de Desarrollo
```bash
# 1. Fork y clonar el repositorio
git clone https://github.com/tu-usuario/autoclicker-ssamucr.git
cd autoclicker-ssamucr

# 2. Crear entorno virtual
python -m venv venv
.\venv\Scripts\activate  # Windows
# o
source venv/bin/activate  # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar dependencias de desarrollo (opcional)
pip install black flake8 pytest
```

#### Flujo de Trabajo
1. **Crear una rama** para tu feature:
   ```bash
   git checkout -b feature/nueva-caracteristica
   ```

2. **Hacer cambios** siguiendo las convenciones del proyecto

3. **Testear** tus cambios:
   ```bash
   python autoclick_gui.py  # Probar GUI
   python autoclick.py      # Probar consola
   python anti-afk.py       # Probar anti-AFK
   ```

4. **Commit** con mensajes descriptivos:
   ```bash
   git add .
   git commit -m "feat: agregar nueva característica X"
   ```

5. **Push** y crear **Pull Request**:
   ```bash
   git push origin feature/nueva-caracteristica
   ```

## 📋 Estándares de Código

### 🐍 Estilo Python
- **PEP 8** para formateo
- **Docstrings** para funciones y clases
- **Type hints** cuando sea posible
- **Nombres descriptivos** para variables y funciones

### 📝 Ejemplo de Función
```python
def calculate_click_interval(min_seconds: float, max_seconds: float) -> float:
    """
    Calcula un intervalo aleatorio entre clics.
    
    Args:
        min_seconds: Tiempo mínimo entre clics
        max_seconds: Tiempo máximo entre clics
        
    Returns:
        float: Intervalo aleatorio en segundos
    """
    return random.uniform(min_seconds, max_seconds)
```

### 🔧 Estructura de Commit Messages
```
tipo(alcance): descripción corta

Descripción más detallada si es necesaria

- feat: nueva característica
- fix: corrección de bug
- docs: cambios en documentación
- style: formateo, sin cambios de código
- refactor: refactoring de código
- test: agregar o actualizar tests
- chore: tareas de mantenimiento
```

## 🧪 Testing

### Probar Manualmente
- ✅ GUI funciona correctamente
- ✅ Botones responden apropiadamente
- ✅ Failsafe funciona (mouse en esquinas)
- ✅ Cierre de aplicación funciona
- ✅ Anti-AFK realiza movimientos diversos
- ✅ Scripts de compilación funcionan

### Tests Automatizados (Futuro)
```python
# Ejemplo de test que se puede agregar
def test_click_interval():
    interval = calculate_click_interval(1.0, 2.0)
    assert 1.0 <= interval <= 2.0
```

## 📂 Estructura del Proyecto

```
autoclicker-ssamucr/
├── 📄 archivos principales
│   ├── autoclick_gui.py      # GUI principal
│   ├── autoclick.py          # Versión consola  
│   └── anti-afk.py           # Anti-AFK Minecraft
├── 🔧 scripts de build
│   ├── crear_ejecutable.py   # Compilador Python
│   └── compilar.bat          # Compilador batch
├── 📚 documentación
│   ├── README.md
│   ├── CHANGELOG.md
│   ├── INSTRUCCIONES.md
│   └── CONTRIBUTING.md       # Este archivo
├── ⚙️ configuración
│   ├── requirements.txt      # Dependencias
│   ├── .gitignore           # Git ignore
│   └── LICENSE              # Licencia MIT
└── 📦 build artifacts
    ├── build/               # Archivos temporales
    ├── dist/                # Ejecutables
    └── venv/                # Entorno virtual
```

## 🎯 Áreas que Necesitan Contribución

### 🚀 Alta Prioridad
- [ ] **Tests automatizados** - Unit tests con pytest
- [ ] **Soporte multiplataforma** - Linux y macOS
- [ ] **Documentación API** - Docstrings completos
- [ ] **Manejo de errores** - Casos edge mejorados

### 🔧 Media Prioridad  
- [ ] **Configuraciones avanzadas** - Intervalos personalizables
- [ ] **Logging detallado** - Sistema de logs
- [ ] **Interfaz mejorada** - Mejor UX/UI
- [ ] **Perfiles de usuario** - Configuraciones guardadas

### 💡 Ideas Futuras
- [ ] **Plugin system** - Arquitectura extensible
- [ ] **Grabación de macros** - Reproducir secuencias
- [ ] **Integración específica** - APIs de juegos
- [ ] **Auto-updater** - Sistema de actualizaciones

## 🤝 Proceso de Review

### ✅ Checklist para Pull Requests
- [ ] El código sigue las convenciones de estilo
- [ ] Se incluyen docstrings donde corresponde
- [ ] Los cambios están documentados en CHANGELOG.md
- [ ] Se probó manualmente en Windows
- [ ] No rompe funcionalidad existente
- [ ] El título del PR es descriptivo

### 📋 Información a Incluir en PR
- **Descripción** clara de los cambios
- **Capturas** de pantalla si aplica
- **Testing** realizado
- **Impacto** en usuarios existentes
- **Breaking changes** si los hay

## 🆘 Necesitas Ayuda?

### 💬 Canales de Comunicación
- **GitHub Issues** para bugs y features
- **GitHub Discussions** para preguntas generales
- **Pull Requests** para contribuciones de código

### 📖 Recursos Útiles
- [Documentación PyAutoGUI](https://pyautogui.readthedocs.io/)
- [Guía PyInstaller](https://pyinstaller.readthedocs.io/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

## 🌟 Reconocimiento

Todos los contribuidores serán reconocidos en:
- 📄 **README.md** - Sección de agradecimientos
- 📝 **CHANGELOG.md** - Créditos por versión
- 🏆 **Contributors** - GitHub contributors page

---

**¡Gracias por ayudar a mejorar AutoClicker Ssamucr!** 🎉

*Tu contribución, sin importar su tamaño, es valiosa para la comunidad.*