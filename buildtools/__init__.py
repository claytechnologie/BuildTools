"""
BuildTools v2.0.0 - Professional Python Development Tools
© 2025 ClayTech

A comprehensive library for local data persistence, state management, 
and console output with modern design.
"""

__version__ = "2.0.0"
__author__ = "ClayTech"
__email__ = "contact@claytech.dev"

# Import main classes for easy access
from .sqlsave import SqlSave
from .statemachine import StateMachine, StateEditor, Debugger
from .cons import ConsoleEditor
from .filewriter import FileWriter, FileEditor, Json
from .gipeo import Gipeo, OLED_SSD1306, EventQueue, Event, esp32

try:
    from .ai import AILogic
except ImportError:
    # AI module is optional (requires openai package)
    AILogic = None

__all__ = [
    "SqlSave",
    "StateMachine", 
    "StateEditor",
    "Debugger",
    "ConsoleEditor",
    "AILogic",
    "FileWriter",
    "FileEditor",
    "Json",
    "Gipeo",
    "OLED_SSD1306",
    "EventQueue",
    "Event",
    "esp32",
    "MetaStream"
]

def info():
    """Show BuildTools information"""
    print(f"""
BuildTools v{__version__}
© 2025 {__author__}

A comprehensive Python development toolkit for:
• Local data persistence (SqlSave)
• State management (StateMachine, StateEditor)
• Console utilities (ConsoleEditor)  
• File operations (FileWriter, FileEditor, Json)
• Hardware integration (Gipeo, OLED_SSD1306)
• AI integration (AILogic)

Documentation: https://github.com/claytechnologie/BuildTools
""")

def version():
    """Show BuildTools version"""
    print(f"BuildTools v{__version__}")