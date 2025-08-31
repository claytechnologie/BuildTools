try:
    import os
    import json
    from .statemachine import StateMachine
    
    class FileWriter:
        def __init__(self, filepath=None):
            self.file = filepath
            self.state = StateMachine("filewriter")

        def set_file(self, filepath):
            self.file = filepath
            
        def create_file(self, name):
            self.file = name
            directory = os.path.dirname(name)
            if directory:
                os.makedirs(directory, exist_ok=True)
            if not os.path.exists(self.file):
                with open(self.file, 'w') as f:
                    f.write("")
        
        def create(self):
            if not self.file:
                return
            if not os.path.exists(self.file):
                directory = os.path.dirname(self.file)
                if directory:
                    os.makedirs(directory, exist_ok=True)
                with open(self.file, 'w') as f:
                    f.write("")

        def write(self, content):
            if not self.file:
                return
            self.create()
            with open(self.file, 'w') as f:
                f.write(content)
        
        def append(self, content):
            if not self.file:
                return
            self.create()
            with open(self.file, 'a') as f:
                f.write(content)
        
        def read(self):
            if not self.file or not os.path.exists(self.file):
                return ""
            with open(self.file, 'r') as f:
                return f.read()

        def locate(self, name):
            if not self.file or not os.path.exists(self.file):
                return -1
            with open(self.file, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if name in line:
                    return i
            return -1

        def locate_line(self, name):
            return self.locate(name)
        
        def read_line(self, line):
            if not os.path.exists(self.file):
                return None
            with open(self.file, 'r') as f:
                lines = f.readlines()
            return lines[line].rstrip('\n') if line < len(lines) else None

        def get_line(self, line):
            return self.read_line(line)

        def write_line(self, line, content):
            if not self.file:
                return
            self.create()
            if os.path.exists(self.file):
                with open(self.file, 'r') as f:
                    lines = f.readlines()
            else:
                lines = []
            
            while len(lines) <= line:
                lines.append("\n")
            
            lines[line] = content + "\n"
            
            with open(self.file, 'w') as f:
                f.writelines(lines)

        def replace_line(self, line, content):
            self.write_line(line, content)

        def delete_line(self, line):
            if not os.path.exists(self.file):
                return
            with open(self.file, 'r') as f:
                lines = f.readlines()
            if line < len(lines):
                lines.pop(line)
                with open(self.file, 'w') as f:
                    f.writelines(lines)

        def clear_line(self, line):
            self.write_line(line, "")

        def clear(self):
            if os.path.exists(self.file):
                os.remove(self.file)
        
        def delete(self):
            self.clear()

        def copy_to(self, target):
            content = self.read()
            target_writer = FileWriter(target)
            target_writer.write(content)

        def move_to(self, target):
            self.copy_to(target)
            self.delete()

        def get_lines(self):
            if not os.path.exists(self.file):
                return []
            with open(self.file, 'r') as f:
                return [line.rstrip('\n') for line in f.readlines()]

        def count_lines(self):
            return len(self.get_lines())

        def exists(self):
            return os.path.exists(self.file) if self.file else False

    class FileEditor(FileWriter):
        def __init__(self, filepath=None):
            super().__init__(filepath)
            try:
                from .ai import AILogic
                self.AI = AILogic()
            except:
                self.AI = None

        def modify(self, target, line=None, content=None):
            if self.AI:
                return self.AI.operations.file_modify(self.file, target, line, content)
            return "AI not available"

        def find_and_replace(self, find_text, replace_text):
            content = self.read()
            new_content = content.replace(find_text, replace_text)
            self.write(new_content)
            return content != new_content

        def insert_at_line(self, line, content):
            lines = self.get_lines()
            lines.insert(line, content)
            self.write('\n'.join(lines))

        def append_line(self, content):
            self.append('\n' + content)

    class Json(FileWriter):
        def __init__(self, filepath=None):
            super().__init__(filepath)
            
        def load_json(self):
            try:
                content = self.read()
                return json.loads(content) if content else {}
            except:
                return {}
                
        def save_json(self, data):
            self.write(json.dumps(data, indent=2))
            
        def get_key(self, key):
            data = self.load_json()
            return data.get(key, None)
            
        def set_key(self, key, value):
            data = self.load_json()
            data[key] = value
            self.save_json(data)
            
        def delete_key(self, key):
            data = self.load_json()
            if key in data:
                del data[key]
                self.save_json(data)
                return True
            return False
            
        def has_key(self, key):
            data = self.load_json()
            return key in data
            
        def get_all_keys(self):
            data = self.load_json()
            return list(data.keys())
            
        def update_dict(self, update_data):
            data = self.load_json()
            data.update(update_data)
            self.save_json(data)
            
        def merge_json(self, other_json_file):
            other_data = Json(other_json_file).load_json()
            self.update_dict(other_data)

except Exception as e:
    print(f"FileWriter error: {e}")