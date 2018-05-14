# Python 3.6.5
import os
import inspect
import importlib
from command import Command

class CommandHandler:
    def __init__(self, client, config):
        # The discord client
        self.client = client
        # The bot's command prefix
        self.prefix = config['Discord']['prefix']
        # A dictionary storing all the bot's registered commands
        self.commands = dict()

    async def handle(self, message):
        """Checks if messages are commands, and runs them if they are."""
        # Don't respond to bot messages
        if message.author.bot: return
        # Check the incoming message for a prefix
        elif message.content[:len(self.prefix)] != self.prefix: return
        else:
            # Get the command part of the message
            command = message.content.split()[0][len(self.prefix):]
            # Split all other parts of the message into a list
            args = message.content.split()[1:]
            # Check if the command is registered and if it is, run it
            if command in self.commands:
                await self.commands[command].run(message, args)

    def register_command(self, command):
        """Registers a command to the bot, so it can be run in future."""
        # Check if the command being passed is actually a command
        if not issubclass(command, Command):
            print('Invalid command; not added.')
            return
        else:
            # Instance the command object from its class
            cmd = command(self.client)
            # Check if the command has a name
            if cmd.name == None:
                print(f'Command not added; missing name.')
                return
            # Check if the command has already been added
            if cmd.name in self.commands:
                print(f'Command {cmd.name} not added; it already exists.')
                return
            else:
                # Add the command
                self.commands[cmd.name] = cmd
                print(f'Loaded command {cmd.name} successfully.')

    def register_commands(self, commands):
        """Allows a list of commands to be added a lot easier."""
        for command in commands:
            self.register_command(command)

    def register_commands_in_dir(self, dir):
        """Registers all the commands contained below a specified directory."""
        # Get all the files below the directory
        for root, dirs, files in os.walk(f'{dir}'):
            for filename in files:
                # Filter out "*.pyc" files
                if filename[-1] != 'c':
                    # The name of the file, minus ".py"
                    name = filename[:-3]
                    # Gets everything exported by this module
                    members = inspect.getmembers(importlib.import_module(name))
                    for member in members:
                        # Get the member that is a class and has the same name as the file
                        if inspect.isclass(member[1]) and member[1].__name__.lower() == name.lower():
                            # ...And register it as a command
                            self.register_command(member[1])
