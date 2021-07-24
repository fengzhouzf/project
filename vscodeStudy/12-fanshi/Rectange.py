class Rectangele():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectange = Rectangele(10, 20)
print(rectange.area())
rectange.change_size(20, 40)
print(rectange.area())