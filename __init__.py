"""
BuildTools - Professional Development Utilities
© 2025 ClayTechnologies

Ein komplettes Entwicklungspaket für lokale Datenpersistierung,
State-Management und Console-Utilities.
"""

__version__ = "2.0.0"
__author__ = "ClayTechnologies"
__email__ = "info@claytechnologie.com"

# Importiere alle Hauptklassen für einfachen Zugriff
from .sqlsave import SqlSave
from .statemachine import StateMachine, StateEditor, Debugger
from .cons import ConsoleEditor

# Exportiere alle wichtigen Klassen
__all__ = [
    'SqlSave',
    'StateMachine', 
    'StateEditor',
    'Debugger',
    'ConsoleEditor'
]

def version():
    """Gibt die aktuelle BuildTools Version zurück"""
    return __version__

def info():
    """Zeigt BuildTools Informationen"""
    print(f"BuildTools v{__version__}")
    print(f"© 2025 {__author__}")
    print("Professional Development Utilities")
    print("\nVerfügbare Module:")
    print("- SqlSave: Lokale Datenpersistierung")
    print("- StateMachine: State-Management")
    print("- StateEditor: Erweiterte State-Funktionen")
    print("- ConsoleEditor: Console-Utilities")
    print("- Debugger: Debug-Funktionen")
