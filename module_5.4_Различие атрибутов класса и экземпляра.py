
class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        # cls.houses_history.append(kwargs[])
        return object.__new__(cls)



    def __init__(self, first, second):
        self.first = first
        self.second = second

    # def __str__(self):
    #     return self.first

    def __del__(self):
        print(f"{self.first} снесен, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)

del h2
del h3
print(House.houses_history)



