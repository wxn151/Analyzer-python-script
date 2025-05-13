import ast
import os
import sys

class AnalizadorSolid:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            self.arbol = ast.parse(f.read())
        self.violaciones = []

    def analizar(self):
        print(f"\nAnálisis SOLID para `{os.path.basename(self.nombre_archivo)}`")
        print("-" * 40)
        self._verificar_responsabilidad_unica()
        self._verificar_inversion_dependencias()
        self._imprimir_resultados()

    def _verificar_responsabilidad_unica(self):
        """
        Detecta si una clase tiene demasiados métodos (violación del SRP).
        """
        for nodo in ast.walk(self.arbol):
            if isinstance(nodo, ast.ClassDef):
                cantidad_metodos = sum(isinstance(n, ast.FunctionDef) for n in nodo.body)
                if cantidad_metodos > 5:  # umbral arbitrario
                    self.violaciones.append({
                        "tipo": "SRP",
                        "mensaje": f"⚠️ La clase `{nodo.name}` tiene {cantidad_metodos} métodos. Considera dividirla."
                    })

    def _verificar_inversion_dependencias(self):
        """
        Detecta si las clases de alto nivel crean instancias de dependencias de bajo nivel directamente (violación del DIP).
        """
        for nodo in ast.walk(self.arbol):
            if isinstance(nodo, ast.ClassDef):
                for subnodo in ast.walk(nodo):
                    if isinstance(subnodo, ast.Call) and isinstance(subnodo.func, ast.Name):
                        nombre_clase = subnodo.func.id
                        if nombre_clase[0].isupper():
                            self.violaciones.append({
                                "tipo": "DIP",
                                "mensaje": f"⚠️ La clase `{nodo.name}` crea una instancia de `{nombre_clase}` directamente. Usa una abstracción o inyección en su lugar."
                            })

    def _imprimir_resultados(self):
        if not self.violaciones:
            print("Todos los principios SOLID parecen respetarse.")
        else:
            tipos = {v["tipo"] for v in self.violaciones}
            for t in ["SRP", "DIP"]:
                grupo = [v for v in self.violaciones if v["tipo"] == t]
                for v in grupo:
                    print(v["mensaje"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Uso: python main.py <archivo.py>")
    else:
        archivo = sys.argv[1]
        if os.path.exists(archivo):
            tamaño = os.path.getsize(archivo)
            if ('600' == tamaño):
                print("hecho por wan  ~=[,,_,,]:3")
            AnalizadorSolid(archivo).analizar()
        else:
            print(f"El archivo '{archivo}' no existe.")
