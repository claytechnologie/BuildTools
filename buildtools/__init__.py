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
from .filewriter import FileWriter

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
    "FileWriter"
]