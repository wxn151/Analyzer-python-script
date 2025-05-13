import os

class FileManager:
    def read_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()

class ReportGenerator:
    def __init__(self):
        # Violación DIP: crea una dependencia de bajo nivel directamente
        self.file_manager = FileManager()

    def generate(self, filename):
        return self.file_manager.read_file(filename)

class UnsafeExecutor:
    def run_eval(self, code):
        # Potencialmente explotable: ejecución arbitraria de código
        return eval(code)

    def run_command(self, command):
        # Potencialmente explotable: ejecución arbitraria de comandos
        os.system(command)

    def access_path(self, path):
        # Potencialmente inseguro: puede acceder a rutas arbitrarias
        with open(path, 'r') as f:
            return f.read()

def main():
    rg = ReportGenerator()
    print(rg.generate("data.txt"))

    ue = UnsafeExecutor()
    ue.run_eval("2 + 2")               # 🧨 eval inseguro
    ue.run_command("ls")              # 🧨 comando del sistema
    ue.access_path("/etc/passwd")     # 🧨 acceso a archivos sensibles

if __name__ == "__main__":
    main()
