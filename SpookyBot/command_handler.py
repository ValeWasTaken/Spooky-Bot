# Python 3.6.5
import os
import inspect
import importlib
from command import Command


class CommandHandler:
    def __init__(self, client, config):
        self.client = client
        self.prefix = config['Discord']['prefix']
        self.commands = dict()

    async def handle(self, message):
        if message.author.bot: return
        elif message.content[:len(self.prefix)] != self.prefix: return
        else:
            command = message.content.split()[0][len(self.prefix):]
            args = message.content.split()[1:]
            if command in self.commands:
                await self.commands[command].run(message, args)

    def register_command(self, command):
        if not issubclass(command, Command):
            print('Invalid command; not added.')
            return
        else:
            cmd = command(self.client)
            if cmd.name == None:
                print(f'Command not added; missing name.')
                return
            if cmd.name in self.commands:
                print(f'Command {cmd.name} not added; it already exists.')
                return
            else:
                self.commands[cmd.name] = cmd
                print(f'Loaded command {cmd.name} successfully.')

    def register_commands(self, commands):
        for command in commands:
            self.register_command(command)

    def register_commands_in_dir(self, dir):
        for root, dirs, files in os.walk(f'{dir}'):
            for filename in files:
                if filename[-1] != 'c':
                    name = filename[:-3]
                    members = inspect.getmembers(importlib.import_module(name))
                    for member in members:
                        if inspect.isclass(member[1]) and member[1].__name__.lower() == name.lower():
                            self.register_command(member[1])
