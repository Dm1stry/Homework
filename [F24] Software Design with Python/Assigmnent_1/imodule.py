from abc import ABCMeta, abstractmethod, abstractproperty

class IModule(metaclass=ABCMeta):
    
    name = None
    
    def __init__(self):
        self.commands = dict()
        self.on_load()
        pass
    
    @abstractmethod
    def on_load(self):
        """Method that executed on load """
        pass
    
    def execute(self, command):
        cmd_and_args = command.split()
        cmd = cmd_and_args[0].lower()
        args = cmd_and_args[1:]
        if cmd in self.commands.keys():
            self.commands[cmd](*args)
        