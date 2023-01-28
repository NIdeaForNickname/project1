#import random
#class MyClass:
#    # print("Hello World")
#    how = 0

#    def __init__(self, height=160, name = "noname", age = 12):
#        self.height = height
#        self.name = name
#        self.age=age
#        MyClass.how += 1

#    def grow(self, height=5):
#        self.height+=height
#        return self.height

#namelist = ["Богдан", "Иван", "Коля", "Андрей", "Максим"]
#lst = []
#times = random.randint(5, 10)
#for i in range(times):
#    lst.append(MyClass(height=random.randint(140, 180), name=namelist[random.randint(0,4)], age=random.randint(12, 14)))
#for i in range(times):
#    print(f"Студент №{i+1}: {lst[i].name} \n {lst[i].age} лет \n Изначальный рост: {lst[i].height} \n текущий:{lst[i].grow(random.randint(0, 16))}")
import tkinter
import ctypes
from tkinter import messagebox as mb
from tkinter import *
class NewClass:
    def __init__(self, name=""):
        self.name = name
        self.happy = 50
        self.progress = 0
        self.live = True
        self.numday = 1
        self.chekvariable = 0
        user32 = ctypes.windll.user32  # информация про комп

        byx = user32.GetSystemMetrics(0)  # информация про разрешение по х
        byy = user32.GetSystemMetrics(1)  # информация про разрешение по у

        sizex = int(byx / 6)
        sizey = int(byy / 3)

        rightx = int((byx - sizex) / 2)
        righty = int((byy - sizey) / 2)

        window = Tk()
        window.title("Student life game")
        window.geometry(f"{sizey}x{sizey}+{rightx}+{righty}")
        window["bg"] = "white"
        window.resizable(False, False)

        self.ButtonSt = Button(bg="red", fg="black", text="Study", command=self.Study)
        self.ButtonSl = Button(bg="cyan", fg="black", text="Sleep", command=self.Sleep)
        self.ButtonRe = Button(bg="green", fg="black", text="Rest", command=self.rest)
        self.ButtonRe.place(relx=0.1, rely=0.7, relwidth=0.4, relheight=0.2)
        self.ButtonSl.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.2)
        self.ButtonSt.place(relx=0.1, rely=0.3, relwidth=0.4, relheight=0.2)

        self.Progress = Label(text=f"Progress: {self.progress}")
        self.Happiness = Label(text=f"Happiness: {self.happy}")
        self.Alive = Label(text=f"Alive?: {self.live}")
        self.Progress.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.2)
        self.Happiness.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.2)
        self.Alive.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.2)

        self.CurrentDay = Label(text="Day: " + str(self.numday))
        self.CurrentDay.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
        window.mainloop()

    def Study(self):
        self.happy -= 5
        self.progress += 10
        self.day()

    def Sleep(self):
        self.happy += 5
        self.day()

    def rest(self):
        self.progress -=5
        self.happy += 10
        self.day()

    def IsLive(self):
        if self.happy <= 0 or self.progress < 0:
            self.live = False
            mb.showinfo("Info", "You lost")
            exit()
        if self.progress >= 20 and self.chekvariable == 0:
            mb.showinfo("Info", "Session done")
            self.chekvariable = 1
        if self.progress >= 40 and self.chekvariable == 1:
            mb.showinfo("Info", "Session 2 done")
            self.chekvariable = 2
        if self.progress >= 60 and self.chekvariable == 2:
            mb.showinfo("Info", "Session 3 done")
            self.chekvariable = 3
        if self.progress >= 80 and self.chekvariable == 3:
            mb.showinfo("Info", "Session 4 done")
            self.chekvariable = 4
        if self.progress >= 100 and self.chekvariable == 4:
            mb.showinfo("Info", "You won")
            self.chekvariable = 5
        self.CurrentDay["text"] = "Day: " + str(self.numday)
        self.ButtonRe.place(relx=0.1, rely=0.7, relwidth=0.4, relheight=0.2)
        self.ButtonSl.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.2)
        self.ButtonSt.place(relx=0.1, rely=0.3, relwidth=0.4, relheight=0.2)
    def day(self):
        self.Progress["text"] = self.progress
        self.Happiness["text"] = self.happy
        self.ButtonSt.destroy()
        self.ButtonSl.destroy()
        self.ButtonRe.destroy()
        self.IsLive()
start = NewClass()