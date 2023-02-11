import random
import time


class NoFruitTree:
    def __init__(self, treetype):
        try:
            self.test = self.type
        except:
            self.rand = random.randint(0, len(treetype) - 1)
            self.type = treetype
            print(self.type)
        self.age = 0
        self.height = 10

    def grow(self):
        self.age += 1
        self.height += 1

    def __str__(self):
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")
        time.sleep(1)
        self.grow()


class FruitTree(NoFruitTree):
    def __init__(self, treetype):
        super().__init__(treetype)
        try:
            self.test2 = self.fruits
        except:
            self.fruits = 0

        self.fruitsCheck = 1
        self.chs = 0
        self.fertility = treetype[1]

    def grow(self):
        super().grow()
        self.fruitsCheck += 1
        print(self.fruitsCheck)
        self.__str__()

    def __str__(self):
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")
        print(f"Fruits you Have: {self.fruits}")
        self.choose()

    def choose(self):
        print("Take fruit(1 - yes, 2 - No)?")
        self.chs = int(input())
        if self.chs == 1:
            self.Take()
        elif self.chs == 2:
            self.grow()
        else:
            print("Wrong value")
            self.choose()

    def Take(self):
        if self.fruitsCheck >= 1:
            self.fruits += self.fertility
            print(f"Fruits collected: {self.fertility}")
            print(f"All fruits you have: {self.fruits}")
            self.fruitsCheck -= 1
        else:
            print("No fruits on tree")
        self.grow()


treeList = [[["Cherry Tree", 1], ["Orange Tree", 1], ["Banana Tree", 2], ["Apple Tree", 3]],
            ["Oak", "Birch", "Acacia", "Pine"]]
for i in range(4):
    print(f"{i} - {treeList[0][i][0]}")
for i in range(4):
    print(f"{i + 4} - {treeList[1][i]}")
sel = int(input("Which tree?"))
print(sel)
if sel // 4 == 0:
    MyClass = FruitTree(treeList[0][sel])
    MyClass.grow()
elif sel // 4 == 1:
    MyClass = FruitTree(treeList[1][sel])
    MyClass.grow()
else:
    print(print("Something gone wrong, try again"))

