import os

modules_dir = "modules"
modules_files = [f[:-3] for f in os.listdir(modules_dir) if os.path.isfile(os.path.join(modules_dir, f)) and f.endswith(".py")]

cls = []


for module_file in modules_files:
    cls.append(__import__(modules_dir + "." + module_file, globals(), locals(), ['content'], 0).content)

while True:
    inp = input("$ ")
    for c in cls:
        try:
            c.execute(inp)
        except Exception as e:
            print(e)
        