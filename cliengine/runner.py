from cliengine import registry

def run_cli(app_name: str, description: str, types: list, space_length: int = 100):
    """Run the command-line interface for the application."""
    print(f" {app_name} ".center(space_length, "-"))
    print(description)
    print("-" * space_length)

    while True:
        tool_type = choose_tool_type(types)
        if tool_type is None:
            print("\nExiting...")
            break

        commands = registry.get_commands_by_type(tool_type)
        command = choose_tool(commands)
        if command:
            try:
                command.run()
            except Exception as e:
                print(f"\n❌ Error running tool: {e}")
        else:
            print("\n❌ Invalid or cancelled tool.")

def choose_tool_type(types):
    """Prompt the user to choose a tool type."""
    print("\nChoose the type:")
    for i, t in enumerate(types, 1):
        print(f"{i} - {t.name.title()}")
    print("0 - Exit")

    choice = input("\nOption: ").strip()
    if choice == "0":
        return None

    try:
        idx = int(choice) - 1
        return types[idx]
    except:
        print("\n❌ Invalid option.")
        return None

def choose_tool(commands):
    """Prompt the user to choose a tool."""
    if not commands:
        print("\n❌ No tools registered for this type.")
        return None

    print("\nChoose the tool:")
    for key, cmd in sorted(commands.items()):
        print(f"{key} - {cmd.name()}")

    choice = input("\nOption: ").strip()
    if choice == "0":
        return None

    return commands.get(choice)
