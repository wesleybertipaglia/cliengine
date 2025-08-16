# CLI Engine

A modular and extensible command-line engine for building structured CLI tools with zero boilerplate.

## Features

- **Plug-and-play command architecture**
- **Autoload commands from your `tools/` directory**
- **Support for custom command types defined per project**
- **Minimal setup required per project**
- **Easy to test, extend, and maintain**

## Installation

### Requirements

Make sure Python 3.8+ and `pip` are installed:

```bash
python3 --version
pip --version
```

### Clone the repository

```bash
git clone https://github.com/wesleybertipaglia/cliengine.git
cd cliengine
```

### Install the package in development mode

```bash
pip install -e .
```

This allows you to make changes to the engine while immediately reflecting them in any project using it.

## Usage

### 1. Define your custom command types

Create a file (e.g., `command_types.py`) in your project root to declare your command types:

```python
from enum import Enum, auto

class CommandType(Enum):
    FILE = auto()
    FOLDER = auto()
    ARCHIVE = auto()
```

You can define as many types as needed, using `auto()` for automatic enumeration values.

### 2. Implement your commands using your `CommandType`

Create your commands in the `tools/` folder (or wherever you prefer), importing your own `CommandType` enum:

```python
from cli_engine.command import Command
from command_types import CommandType

class FileCompressorCommand(Command):
    def name(self):
        return "File Compressor"

    def type(self):
        return CommandType.FILE

    def run(self):
        print("Running File Compressor...")
```

### 3. Load commands and run your CLI

In your `main.py`, load commands and pass your `CommandType` list to the runner:

```python
from cli_engine.loader import load_commands_from
from cli_engine.runner import run_cli
from command_types import CommandType

load_commands_from("tools")

run_cli(
    app_name="My CLI Tool",
    description="A powerful command-line utility.",
    types=list(CommandType)
)
```

### 4. Run your CLI app

```bash
python main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
