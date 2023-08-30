class Cat:
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return "🐈🐈"

    def __repr__(self):
        return f'Cat {self.name!r}'

c1 = Cat("Lenny")  #c1: 🐈🐈
c2 = Cat("kenny")  #c2: 🐈🐈
Cat("Kenny")
print(c1, c2)

