#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BuildTools Sync Script
Automatische Installation/Update von BuildTools aus dem Git-Repository
© 2025 ClayTechnologies
"""

import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path

class BuildToolsSync:
    """Synchronisiert BuildTools mit GitHub Repository"""
    
    def __init__(self):
        self.repo_url = "https://github.com/claytechnologie/BuildTools.git"
        self.package_name = "buildtools"
        self.temp_dir = None
        
    def log(self, message, level="INFO"):
        """Einfaches Logging"""
        colors = {
            "INFO": "\033[92m",    # Grün
            "WARN": "\033[93m",    # Gelb  
            "ERROR": "\033[91m",   # Rot
            "RESET": "\033[0m"     # Reset
        }
        print(f"{colors.get(level, '')}{level}: {message}{colors['RESET']}")
    
    def run_command(self, command, cwd=None):
        """Führt Shell-Kommando aus"""
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                cwd=cwd,
                capture_output=True, 
                text=True, 
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.log(f"Kommando fehlgeschlagen: {e}", "ERROR")
            self.log(f"Output: {e.stdout}", "ERROR")
            self.log(f"Error: {e.stderr}", "ERROR")
            return None
    
    def check_git_installed(self):
        """Prüft ob Git installiert ist"""
        try:
            subprocess.run(["git", "--version"], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.log("Git ist nicht installiert oder nicht im PATH!", "ERROR")
            return False
    
    def check_buildtools_installed(self):
        """Prüft ob BuildTools bereits installiert ist"""
        try:
            import buildtools
            self.log(f"BuildTools v{buildtools.__version__} ist installiert", "INFO")
            return True
        except ImportError:
            self.log("BuildTools ist nicht installiert", "INFO")
            return False
    
    def uninstall_buildtools(self):
        """Deinstalliert vorhandene BuildTools"""
        self.log("Deinstalliere vorhandene BuildTools...", "INFO")
        result = self.run_command("pip uninstall buildtools -y")
        if result is not None:
            self.log("BuildTools deinstalliert", "INFO")
            return True
        return False
    
    def clone_repository(self):
        """Klont das GitHub Repository"""
        self.temp_dir = tempfile.mkdtemp(prefix="buildtools_sync_")
        self.log(f"Klone Repository nach: {self.temp_dir}", "INFO")
        
        result = self.run_command(f"git clone {self.repo_url} .", self.temp_dir)
        if result is not None:
            self.log("Repository erfolgreich geklont", "INFO")
            return True
        return False
    
    def install_from_source(self):
        """Installiert BuildTools aus dem geklonten Repository"""
        self.log("Installiere BuildTools aus Quellcode...", "INFO")
        
        # Wechsle in Repository-Verzeichnis
        setup_py = os.path.join(self.temp_dir, "setup.py")
        if not os.path.exists(setup_py):
            self.log("setup.py nicht gefunden!", "ERROR")
            return False
        
        # Installiere mit pip
        result = self.run_command(f"pip install -e .", self.temp_dir)
        if result is not None:
            self.log("BuildTools erfolgreich installiert!", "INFO")
            return True
        return False
    
    def cleanup(self):
        """Räumt temporäre Dateien auf"""
        if self.temp_dir and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
                self.log("Temporäre Dateien bereinigt", "INFO")
            except Exception as e:
                self.log(f"Fehler beim Bereinigen: {e}", "WARN")
    
    def test_installation(self):
        """Testet die Installation"""
        self.log("Teste BuildTools Installation...", "INFO")
        try:
            # Reload modules um neue Version zu laden
            if 'buildtools' in sys.modules:
                del sys.modules['buildtools']
            
            import buildtools
            buildtools.info()
            
            # Teste Hauptfunktionen
            db = buildtools.SqlSave("test_db")
            db.save(data="test", id="sync_test")
            result = db.load(id="sync_test")
            
            if result == "test":
                self.log("✅ BuildTools funktioniert korrekt!", "INFO")
                db.clear("test_db")  # Cleanup
                return True
            else:
                self.log("❌ BuildTools Test fehlgeschlagen", "ERROR")
                return False
                
        except Exception as e:
            self.log(f"❌ BuildTools Test fehlgeschlagen: {e}", "ERROR")
            return False
    
    def sync(self, force=False):
        """Hauptfunktion: Synchronisiert BuildTools"""
        self.log("🚀 BuildTools Sync gestartet", "INFO")
        self.log("=" * 50, "INFO")
        
        try:
            # 1. Git prüfen
            if not self.check_git_installed():
                return False
            
            # 2. Vorhandene Installation prüfen
            was_installed = self.check_buildtools_installed()
            
            if was_installed and not force:
                response = input("BuildTools ist bereits installiert. Aktualisieren? (j/n): ")
                if response.lower() not in ['j', 'ja', 'y', 'yes']:
                    self.log("Sync abgebrochen", "INFO")
                    return True
            
            # 3. Deinstallieren falls vorhanden
            if was_installed:
                if not self.uninstall_buildtools():
                    self.log("Deinstallation fehlgeschlagen", "ERROR")
                    return False
            
            # 4. Repository klonen
            if not self.clone_repository():
                return False
            
            # 5. Aus Quellcode installieren
            if not self.install_from_source():
                return False
            
            # 6. Installation testen
            if not self.test_installation():
                return False
            
            self.log("=" * 50, "INFO")
            self.log("🎉 BuildTools erfolgreich synchronisiert!", "INFO")
            self.log("Sie können jetzt 'import buildtools' verwenden", "INFO")
            return True
            
        except KeyboardInterrupt:
            self.log("Sync durch Benutzer abgebrochen", "WARN")
            return False
        except Exception as e:
            self.log(f"Unerwarteter Fehler: {e}", "ERROR")
            return False
        finally:
            self.cleanup()

def main():
    """Hauptfunktion für Command-Line Interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="BuildTools Sync Script")
    parser.add_argument(
        "--force", 
        action="store_true", 
        help="Forciert Update ohne Nachfrage"
    )
    parser.add_argument(
        "--version",
        action="store_true", 
        help="Zeigt aktuelle BuildTools Version"
    )
    
    args = parser.parse_args()
    
    if args.version:
        try:
            import buildtools
            print(f"BuildTools v{buildtools.__version__}")
        except ImportError:
            print("BuildTools ist nicht installiert")
        return
    
    # Sync durchführen
    syncer = BuildToolsSync()
    success = syncer.sync(force=args.force)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
