🧪 Python Analyzer
--
This script reads a Python source file (.py) and checks potentially exploitable behaviors, such as eval usage, command execution, or insecure file access.

### 📦 HOW TO USE IT

Place the script you want to analyze in the same folder, then run from the terminal:


```bash
python main.py filename.py

# example with a test file
python main.py dummy.py
```

Returns a JSON with the violations found.
```json
[
  {
    "tipo": "EXPLOIT",
    "mensaje": "🛑 Uso peligroso de `eval()` en línea 19"
  }
]
```

### 📦 ¿CÓMO USARLO?

Coloca el archivo que deseas analizar en la misma carpeta, y ejecuta desde la terminal:

```bash
python main.py archivo.py

# ejemplo con archivo de prueba
python main.py dummy.py
```

#### 🔍 Qué detecta


    Heurísticas para localizar código peligroso, incluyendo:

    - Uso de eval()
    - Uso de exec()
    - Uso de os.system()
    - Uso de open() con rutas arbitrarias

    Cualquier patrón que permita ejecución de comandos arbitrarios o acceso a datos sensibles
