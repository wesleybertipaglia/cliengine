from cliengine.command import Command
from command_type import CommandType

class FileCompressorCommand(Command):
    def name(self):
        return "File Compressor"

    def type(self):
        return CommandType.FILE

    def run(self):
        print("Running File Compressor...")