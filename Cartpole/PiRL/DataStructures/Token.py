class Token:
    def __init__(self, name: str):
        self.name = name

    @property
    def str(self):
        return str(self)

    def __str__(self):
        return repr(self)
    
    def __eq__(self, o: object) -> bool:
        return o.name == self.name
    
class NonTerminal(Token):
    def __init__(self, name: str, text = ""):
        super().__init__(name)
        self.text = text

    def __repr__(self):
        return f"NonTerminal({self.name})"

class Terminal(Token):
    def __repr__(self):
        return f"Terminal({self.name})"
    