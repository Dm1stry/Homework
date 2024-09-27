from imodule import IModule
from class_name_decorator import decorator

@decorator
class Echo(IModule):
    def __init__(self):
        super().__init__()
        self.commands["echo"] = lambda arg: print(arg)
        #print("Echo init called")
        
    
    def on_load(self):
        print("module echo loaded")
        
content = Echo()