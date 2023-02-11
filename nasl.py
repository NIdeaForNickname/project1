class Phone:
    def __init__(self):
        self.alive = False

    def work(self):
        self.alive = True

    def calling(self):
        if self.alive:
            print("Incoming call")
    def Info(self):
        print(f"Is on: {self.alive}")


class Mobile(Phone):
    def __init__(self):
        super().__init__()
        self.battery = 0

    def ChargeCheck(self, percents):
        self.battery = percents
        print(f"Current charge: {self.battery}")

    def calling(self):
        if self.alive and self.battery >= 1:
            print("Incoming call")
    def Info(self):
        print(f"Current charge: {self.battery}")

def poli():
    for i in Phone, Mobile:
        i().Info()
# wadas = Mobile()
# wadas.work()
# wadas.calling()
# wadas.ChargeCheck(percents=100)
print(poli())