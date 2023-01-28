import random


class MyClass:
    # print("Hello World")
    how = 0

    def __init__(self, height=160, name = "noname", age = 12):
        self.height = height
        self.name = name
        self.age=age
        MyClass.how += 1

    def grow(self, height=5):
        self.height+=height
        return self.height

namelist = ["Богдан", "Иван", "Коля", "Андрей", "Максим"]
lst = []
times = random.randint(5, 10)
for i in range(times):
    lst.append(MyClass(height=random.randint(140, 180), name=namelist[random.randint(0,4)], age=random.randint(12, 14)))
for i in range(times):
    print(f"Студент №{i+1}: {lst[i].name} \n {lst[i].age} лет \n Изначальный рост: {lst[i].height} \n текущий:{lst[i].grow(random.randint(0, 16))}")