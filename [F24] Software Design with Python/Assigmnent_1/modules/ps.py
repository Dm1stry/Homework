from imodule import IModule
import psutil
from class_name_decorator import decorator

@decorator
class Ps(IModule):
    def __init__(self):
        super().__init__()
        self.commands["ps"] = self.on_call_ps
        
    
    def on_load(self):
        print("module ps loaded")
        
        
    def on_call_ps(self, arg=None):
        for proc in psutil.process_iter():
            try:
                # Get process name & pid from process object.
                processName = proc.name()
                processID = proc.pid
                print(processName , ' ::: ', processID)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            
content = Ps()