class Seed:
    def __init__(self, name):
        self.name = name
        self.state = "dormant"  # dormant → active

    def activate(self):
        self.state = "active"

    def __repr__(self):
        return f"<Seed {self.name}: {self.state}>"