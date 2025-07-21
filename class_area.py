class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Rectangle):
    def area2(self):
        return (self.width * self.height) / 2


triangle = Triangle(10, 5)
print(f"矩形面積 {triangle.area()}")
print(f"三角形面積 {triangle.area2()}")
