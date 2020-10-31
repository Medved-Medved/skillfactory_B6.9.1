class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_arrea(self):
        return self.b * self.a

class Square:
    def __init__(self, a):
        self.a = a
    def get_arrea_square(self):
        return self.a ** 2

class Circle:
    def __init__(self, a):
        self.a = a
    def get_arrea_circle(self):
        return self.a ** 2 * 3.1415
