 # Das ist BuildTools v2 von ClayTech ©2025
try:
    try:    
        import os
        import sqlite3
        import pickle
    except Exception as e:
        print("Critical error occurred while importing modules. Please reinstall BuildTools.")

    class SqlSave:
        def __init__(self, db="default"):
            
            self.appdata_path = os.environ.get('APPDATA')
            self.db_dir = os.path.join(self.appdata_path, 'BuildTools', 'data')
            self.db_path = os.path.join(self.db_dir, f'{db}.db')

            os.makedirs(self.db_dir, exist_ok=True)

            self._init_db()
        
        def _init_db(self):
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS saved_data (
                    id TEXT PRIMARY KEY,
                    data BLOB
                )
            ''')
            conn.commit()
            conn.close()
        
        def save(self, data, id):
            
            # Serialisiere die Daten
            serialized_data = pickle.dumps(data)
            
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO saved_data (id, data) VALUES (?, ?)
                ''', (id, serialized_data))
                conn.commit()
                conn.close()
                return True
            except Exception as e:
                return False
        
        def load(self, id):
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT data FROM saved_data WHERE id = ?', (id,))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return pickle.loads(result[0])
            return None
        
        def delete(self, id):
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM saved_data WHERE id = ?', (id,))
            conn.commit()
            conn.close()

        def update(self, id, data):
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE saved_data SET data = ? WHERE id = ?
            ''', (pickle.dumps(data), id))
            conn.commit()
            conn.close()
            
        def search(self, db, id):
            db_path = os.path.join(self.db_dir, f'{db}.db')
            if not os.path.exists(db_path):
                return False

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT 1 FROM saved_data WHERE id = ?', (id,))
            result = cursor.fetchone()
            conn.close()
            
            return result is not None
        
        def clear(self, db):
            db_path = os.path.join(self.db_dir, f'{db}.db')
            if os.path.exists(db_path):
                os.remove(db_path)
                return True
            return False
        
except Exception as e:
    print("Critical error occurred, please check your installation and dependencies.")