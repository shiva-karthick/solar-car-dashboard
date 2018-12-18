class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        # Addition with another vector.
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        # Subtraction with another vector.
        return Vector(self.x - v.x, self.y - v.y)

    def __mul__(self, s):
        # Multiplication with a scalar.
        return Vector(self.x * s, self.y * s)

    def __div__(self, s):
        # Division with a scalar.
        float_s = float(s)
        return Vector(self.x / float_s, self.y / float_s)

    def __floordiv__(self, s):
        # Division with a scalar (value floored).
        return Vector(self.x // s, self.y // s)

    def __repr__(self):
        # Print friendly representation of Vector class. Else, it would
        # show up like, <__main__.Vector instance at 0x01DDDDC8>.
        return ("<Vector (%f, %f)>" % (self.x, self.y))


class Test(object):
    def method(self, value):
        kself.num = value
        return self.num

    @staticmethod
    def display():
        print(self.num)


if __name__ == "__main__":
    # a = Vector(3, 5)
    # b = Vector(2, 7)
    # print(a + b)  # Output: <Vector (5.000000, 12.000000)>
    # print(b - a)  # Output: <Vector (-1.000000, 2.000000)>
    # print(b * 1.3)  # Output: <Vector (2.600000, 9.100000)>
    # print(a // 17)  # Output: <Vector (0.000000, 0.000000)>
    # print(a / 17)  # Output: <Vector (0.176471, 0.294118)>

    test = Test()

    test.display(test.method(5))
