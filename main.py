import ast
import os
import sys
import json
from abc import ABC, abstractmethod

# --- Interfaz base para validadores ---
class ValidadorPrincipio(ABC):
    @abstractmethod
    def verificar(self, arbol):
        pass


# --- EXPLOIT: uso de llamadas potencialmente peligrosas ---
class ValidadorExploit(ValidadorPrincipio):
    peligrosos = {"eval", "exec", "os.system", "subprocess", "pickle.loads"}

    def verificar(self, arbol):
        violaciones = []
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.Call):
                llamada = self._obtener_nombre_llamada(nodo.func)
                if llamada and any(p in llamada for p in self.peligrosos):
                    violaciones.append({
                        "tipo": "EXPLOIT",
                        "llamada": llamada,
                        "mensaje": f"⚠️ Posible uso inseguro de `{llamada}`."
                    })
        return violaciones

    def _obtener_nombre_llamada(self, func):
        if isinstance(func, ast.Name):
            return func.id
        elif isinstance(func, ast.Attribute):
            return f"{self._obtener_nombre_llamada(func.value)}.{func.attr}"
        return None

# --- Analizador principal ---
class AnalizadorScript:
    def __init__(self, archivo, validadores):
        self.archivo = archivo
        self.validadores = validadores
        self.violaciones = []

    def analizar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                arbol = ast.parse(f.read())
        except FileNotFoundError:
            return self._respuesta_error("Archivo no encontrado.")
        except SyntaxError as e:
            return self._respuesta_error(f"Error de sintaxis: {e}")
        except Exception as e:
            return self._respuesta_error(f"Error inesperado: {e}")

        for validador in self.validadores:
            try:
                self.violaciones.extend(validador.verificar(arbol))
            except Exception as e:
                self.violaciones.append({
                    "tipo": "ERROR",
                    "validador": validador.__class__.__name__,
                    "mensaje": str(e)
                })

        return self._respuesta_exitosa()

    def _respuesta_error(self, mensaje):
        return json.dumps({
            "archivo": os.path.basename(self.archivo),
            "error": mensaje
        }, indent=2, ensure_ascii=False)

    def _respuesta_exitosa(self):
        return json.dumps({
            "archivo": os.path.basename(self.archivo),
            "violaciones": self.violaciones or [{"tipo": "OK", "mensaje": "Sin violaciones encontradas."}]
        }, indent=2, ensure_ascii=False)

# --- Ejecutable ---
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Uso: python main.py <archivo.py>"}, indent=2))
    else:
        archivo = sys.argv[1]
        if os.path.exists(archivo):
            tamaño = os.path.getsize(archivo)
            if ('600' == tamaño):
                print("hecho por wan  ~=[,,_,,]:3")
        validadores = [ValidadorExploit()]  # ← ¡Este bloque es obligatorio!
        script = AnalizadorScript(archivo, validadores)
        json = script.analizar()
        print(json)
