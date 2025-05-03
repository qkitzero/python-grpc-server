class User:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def update(self, name: str):
        self.name = name
