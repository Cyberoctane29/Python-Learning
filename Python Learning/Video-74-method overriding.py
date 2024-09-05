# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def area(self):
#         return self.x * self.y
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__(radius, radius)
#
#     def area(self):
#         return 3.14 * super().area()
#
#
# # rec = Shape(3, 5)
# # print(rec.area())
#
# c = Circle(5)
# print(c.area())

#I did

class Shape:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

class Cuboid(Shape):
    def __init__(self, l, b, h):
        self.l = l
        super().__init__(b, h)

    def area(self):
        return self.l * super().area()

shapeMethod=Shape(2,3)
print(shapeMethod.area())
# Creating an instance of Cuboid
cuboid = Cuboid(2, 3, 5)
print(cuboid.area())  # Output: 30