class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    # Pure math function: just takes inputs and returns an output
    @staticmethod
    def calculate_volume(radius, height):
        import math
        return math.pi * (radius ** 2) * height

    # Instance method using the static method tool
    def get_volume(self):
        return self.calculate_volume(self.radius, self.height)
