class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created~")

    def rot(self, days, temp):
        self.mold = days * temp


org1 = Orange(10, "dark orange")
print(org1)
print(org1.mold)
org1.rot(10, 98)
print(org1.mold)
