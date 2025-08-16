from cliengine.loader import load_commands_from
from cliengine.runner import run_cli
from command_type import CommandType

load_commands_from("tools")

run_cli(
    app_name="My CLI Tool",
    description="A powerful command-line utility.",
    types=list(CommandType)
)