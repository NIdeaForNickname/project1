import random


class MyClass:
    # print("Hello World")
    how = 0

    def __init__(self, height):
        self.height = height
        print(self)
        MyClass.how += 1

    def grow2(self, lis=None):
        if lis is None:
            lis = []
        self.mid = 0
        for i in range(len(lis)):
            self.mid += lis[i]
        self.mid = self.mid / len(lis)


lst = []
for i in range(random.randint(5, 10)):
    hei = random.randint(140, 180)
    lst.append(MyClass(height=hei))
    print(lst[i])
print(MyClass.how)
hi = MyClass.grow2(lis=lst)
print(hi)