from typing import Dict, List, Any
from cliengine import command

_COMMANDS: Dict[Any, Dict[str, command.Command]] = {}

def register_command(key: str, cmd: command.Command):
    tool_type = cmd.type()

    if tool_type not in _COMMANDS:
        _COMMANDS[tool_type] = {}
    _COMMANDS[tool_type][key] = cmd

def get_commands_by_type(tool_type: Any) -> Dict[str, command.Command]:
    return _COMMANDS.get(tool_type, {})

def get_all_commands() -> List[command.Command]:
    all_commands = []
    for cmds in _COMMANDS.values():
        all_commands.extend(cmds.values())
    return all_commands
