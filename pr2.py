import random


class Test:
    def __init__(self, vopros=""):
        try:
            self.otvet2 = self.otvet[0]
        except:
            self.otvet =[]
        self.vopros = vopros

    def __str__(self):
        print(self.vopros)

    def save(self, otv):
        self.otvet.append([self.vopros, otv])

    def res(self):
        print("Test result:")
        for i in self.otvet:
            print(f"Question: {i[0]} \nAnswer: {i[1]}")
