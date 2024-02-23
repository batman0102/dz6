
class Hello:
    def __init__(self, str):
        self.str = str

class MyHello(Hello):
    def greet(self):
        return "Hello, " + self.str + "!"
