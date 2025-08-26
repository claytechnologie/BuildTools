#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BuildTools Setup Script
© 2025 ClayTechnologies
"""

from setuptools import setup, find_packages
import os

# Read README for long description
long_description = """
# BuildTools - Professional Development Utilities

Ein komplettes Python-Entwicklungspaket für lokale Datenpersistierung, 
State-Management und Console-Utilities.

## Features

- **SqlSave**: Lokale SQLite-basierte Datenpersistierung
- **StateMachine**: Professionelles State-Management mit Triggern
- **StateEditor**: Erweiterte State-Funktionen mit Timer und Events
- **ConsoleEditor**: Rich-basierte Console-Utilities
- **AILogic**: OpenAI API Integration

## Installation

```bash
pip install buildtools
```

## Quick Start

```python
import buildtools

# Daten speichern
db = buildtools.SqlSave()
db.save(data="Hello World", id="greeting")

# State Management
state = buildtools.StateMachine("MyApp")
state.add_state("running", "True")

# Console Output
console = buildtools.ConsoleEditor()
console.success("BuildTools loaded!")
```

## Anforderungen

- Python 3.7+
- rich
- openai (optional, für AILogic)
"""

setup(
    name="buildtools",
    version="2.0.0",
    author="ClayTechnologies",
    author_email="info@claytechnologie.com",
    description="Professional Development Utilities für Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/claytechnologie/BuildTools",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rich>=10.0.0",
    ],
    extras_require={
        "ai": ["openai>=1.0.0"],
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
            "mypy",
        ],
    },
    entry_points={
        "console_scripts": [
            "buildtools-info=buildtools:info",
            "buildtools-version=buildtools:version",
        ],
    },
    keywords="database state-management console utilities development tools",
    project_urls={
        "Bug Reports": "https://github.com/claytechnologie/BuildTools/issues",
        "Source": "https://github.com/claytechnologie/BuildTools",
        "Documentation": "https://github.com/claytechnologie/BuildTools/wiki",
    },
    include_package_data=True,
    zip_safe=False,
)
