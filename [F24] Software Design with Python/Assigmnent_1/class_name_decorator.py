def decorator(Source):
    class Wrapper(Source):
        def __init__(self):
            super().__init__()
            self.name = (Source.__class__.__name__).lower()
            
    return Wrapper