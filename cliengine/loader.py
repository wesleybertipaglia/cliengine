import importlib
import os
import pkgutil
import inspect
from cliengine.command import Command
from cliengine.registry import register_command

def load_commands_from(package="tools"):
    """Autoloads all Command implementations from the given package."""
    package_path = os.path.join(os.getcwd(), package.replace(".", "/"))

    id = 1

    for _, module_name, _ in pkgutil.iter_modules([package_path]):
        full_module = f"{package}.{module_name}"
        try:
            module = importlib.import_module(full_module)

            for _, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Command) and obj is not Command:
                    instance = obj()
                    register_command(str(id), instance)
                    id += 1
        except Exception as e:
            print(f"❌ Failed to load module '{full_module}': {e}")
