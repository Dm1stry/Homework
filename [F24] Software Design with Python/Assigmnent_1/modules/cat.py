from imodule import IModule
from class_name_decorator import decorator

@decorator
class Cat(IModule):
    def __init__(self):
        super().__init__()
        self.commands["cat"] = lambda file: print(open(file).read())
        
    
    def on_load(self):
        print("module cat loaded")

content = Cat()