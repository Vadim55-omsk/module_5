
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей:{self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    # def __add__(self, value):
    #     self.number_of_floors += value
    #     return self
         
    def __add__(self,value):
        if isinstance(value, int):
        self.number_of_floors = self.number_of_floors + value
        return self  
   
    def __radd__(self, value):
        self.number_of_floors += value
        return self

 

    def __iadd__(self, value):
        self.number_of_floors += value
        return self


h1 = House("ЖК Эльбрус", number_of_floors = 18)
h2 = House("Домик в деревне", 2)
h1 = h1 + 10
h2 = h2 + 10
h1 += 10

print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))

print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)

print(h1)
print(h1==h2)

print(h2)
print(h1)
