class Animal:
    def __init__(self, legs: int = 4) -> None:
        self.number_of_legs = legs

    def set_number_of_legs(self, legs):
        self.number_of_legs = legs

    @staticmethod
    def breathe():
        print("Animal is breathing")

bear = Animal()
print(bear.number_of_legs)
bear.breathe()