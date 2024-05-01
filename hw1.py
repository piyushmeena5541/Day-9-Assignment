class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
area = circle.calculate_area()
print("The area of the circle is:", area)
