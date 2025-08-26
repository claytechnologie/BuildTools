try:
    import os
    from .statemachine import StateMachine
    state = StateMachine("filewriter")
    
    class FileWriter:

      # FileWriter für einfache Datei Operationen

        def __init__(self):
            self.file = None
            self.state = state


        def set_file(self, filepath):
            self.file = filepath
            
        def create_file(self, name):
            self.file = name
            # Nur Verzeichnis erstellen, wenn tatsächlich ein Pfad vorhanden ist
            directory = os.path.dirname(name)
            if directory:  # Nur wenn directory nicht leer ist
                os.makedirs(directory, exist_ok=True)
            
            # Datei erstellen, falls sie nicht existiert
            if not os.path.exists(self.file):
                with open(self.file, 'w') as f:
                    f.write("")
            
        
        def create(self):
            if os.path.exists(self.file):
                pass
            else:
                with open(self.file, 'w') as f:
                    f.write("")

        def locate_file(self):
            self.state.add_state("file_location", "Keine")
            directory = os.path.dirname(self.file)
            if directory:  # Nur wenn directory nicht leer ist
                try:
                    os.makedirs(directory, exist_ok=True)
                    self.state.update("file_location", "Gefunden")
                except:
                    self.state.update("file_location", "Nicht Gefunden")
            else:
                # Datei im aktuellen Verzeichnis
                self.state.update("file_location", "Gefunden")
                
        def write(self):
            with open(self.file, 'a') as f:
                f.write(self.state.get_state("file_content", ""))
                self.state.update("file_written", "Ja")
        
        def read(self):
            with open(self.file, 'r') as f:
                return f.read()

        def locate_line(self, name):
            target = name
            with open(self.file, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if target in line:
                    return i
            return -1

        def locate(self, name):
            target = name
            with open(self.file, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if target in line:
                    return i
            return -1

        
        def read_line(self, line):
            with open(self.file, 'r') as f:
                lines = f.readlines()
            return lines[line] if line < len(lines) else None

        def write_line(self, line, content):
            # Datei lesen oder leere Liste wenn Datei nicht existiert
            if os.path.exists(self.file):
                with open(self.file, 'r') as f:
                    lines = f.readlines()
            else:
                lines = []
            
            # Liste erweitern falls nötig
            while len(lines) <= line:
                lines.append("\n")
            
            # Zeile setzen
            lines[line] = content + "\n"
            
            # Datei schreiben
            with open(self.file, 'w') as f:
                f.writelines(lines)

        def clear(self):
            os.remove(self.file)
        
        def clear_line(self, line):
            with open(self.file, 'r') as f:
                lines = f.readlines()
            with open(self.file, 'w') as f:
                for i, l in enumerate(lines):
                    if i != line:
                        f.write(l)

        def get_line(self, line):
            with open(self.file, 'r') as f:
                lines = f.readlines()
            return lines[line] if line < len(lines) else None

    state.clear()
    
    class FileEditor(FileWriter):

      # FileEditor für CustomFile Operations

        def __init__(self):
            super().__init__()
            import os
            from ai import AILogic
            self.AI = AILogic()
            self.apikey = os.getenv("OpenAI_API")

        def modify(self, target, line=None, content=None):
           self.AI.operations.file_modify(self.file, target, line, content)

        def get(self, target):
            pass
            
except Exception:
    print("Critical error occurred, please check your installation and dependencies.")