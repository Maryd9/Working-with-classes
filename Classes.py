from copy import deepcopy


class Plant:
    def __init__(self, name="", height=0, colour="Разноцветное", lifetime="Однолетнее"):
        self.name = name
        self.height = height
        self.colour = colour
        self.lifetime = lifetime

    def __str__(self):
        return f"Название: {self.name}, высота растения: {self.height}," \
               f" цвет: {self.colour}, время жизни: {self.lifetime},"


class Flower(Plant):
    def __init__(self, name="Бегония", height=0, colour="Разноцветное", lifetime="Однолетнее"):
        self.name = name
        self.height = height
        self.colour = colour
        self.lifetime = lifetime

    def __add__(self, other):
        if isinstance(other, Flower):
            return Bouquet(flowers=[self, other])
        else:
            print(f"Нельзя добавить к цветку объект класса {type(other)}!")

    def __eq__(self, other):
        if isinstance(other, Flower):
            return True if self.name == other.name and self.height == other.height and \
                           self.colour == other.colour and self.lifetime == other.lifetime else False
        else:
            print(f"Нельзя сравнить с {type(other)}!")

    def __str__(self):
        return f"Название: {self.name}, высота растения: {self.height}," \
               f" цвет: {self.colour}, время жизни: {self.lifetime}"


class EmptyException(BaseException):
    def __init__(self, name):
        self.message = f"Букет не существует"

    def __str__(self):
        return self.message

try:
    class Bouquet:
        def __init__(self, name="Новый букет", flowers=[]):
            self.name = name
            self.flowers = deepcopy(flowers)

        def isInBouquet(self, flower):
            if isinstance(self, Flower):
                for i in self.flowers:
                    if i == flower:
                        return f"Такой цветок есть"
            else:
                return f"Нет такого цветка в этом букете!"

        def getCount(self):
            return len(self.flowers)

        def isInGroup(self, flower):
            for i in range(len(self.flowers)):
                if self.flowers[i] == flower:
                    return i
            return -1

        def __add__(self, other):
            if isinstance(other, Bouquet):
                newBouquet = deepcopy(self)
                for flower in other.flowers:
                    newBouquet += flower
                return newBouquet

            elif isinstance(other, Flower):
                return Bouquet(flowers=self.flowers + [other])

            else:
                print(f"Нельзя сформировать букет с этим объектом {type(other)}!")

        def __sub__(self, other):
            try:
                if len(self.flowers) < 1:
                    raise EmptyException(self.name)
                else:
                    if isinstance(other, Flower):
                        if self.isInGroup(other) > -1:
                            newFlowers = deepcopy(self.flowers)
                            newFlowers.pop(self.isInGroup(other))
                            return Bouquet(flowers=newFlowers)
                        else:
                            return deepcopy(self)
                    elif isinstance(other, Bouquet):
                        newBouquet = deepcopy(self)
                        for flower in other.flowers:
                            newBouquet -= flower
                        return newBouquet
                    else:
                        print(f"Нельзя вычесть из группы объект класса {type(other)}!")
            except EmptyException as err:
                print(err)

        def __str__(self):
            if self.getCount() > 0:
                return f"{self.name}:\n" + \
                       f" Цветы, из которых состоит:\n " + \
                       f" ".join(map(lambda a, i: str(a) + "\n", self.flowers, range(len(self.flowers))))
            else:
                return "Букет не может существовать, если в нем нет цветов"


    flower1 = Flower(name="Бегония", height=60, colour="Розовый", lifetime="Многолетнее")
    flower2 = Flower(name="Роза", height=40, colour="Красный", lifetime="Однолетнее")
    flower3 = Flower(name="Роза", height=40, colour="Красный", lifetime="Однолетнее")
    flower4 = Flower(name="Ирис", height=73, colour="Фиолетовый", lifetime="Многолетнее")
    flower5 = Flower(name="Роза", height=40, colour="Розовый", lifetime="Однолетнее")

    bouquet1 = Bouquet(name="Букет с розами", flowers=[flower4])
    bouquet2 = Bouquet(name="Букет с ирисами", flowers=[flower3, flower4,flower5])

    print(bouquet2-flower4)

except (NameError, TypeError):
    print("Неверные данные!")
