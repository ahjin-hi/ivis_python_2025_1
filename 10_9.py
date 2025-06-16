class Counter:
    def __init__(self,number=0):
        if number >= 100 or number <= 0:
            self.__number = 0
        else:
            self.__number = number

    def __add__(self,other):
        return Counter(self.__number + other.__number)

    def __sub__(self,other):
        return Counter(self.__number - other.__number)

    def __str__(self):
        return f"C({self.__number})"

c1 = Counter(10)
c2 = Counter(20)

c3 = c1 + c2
c4 = c1 -c2

print('c3 = ', c3)
print('c4 = ', c4)