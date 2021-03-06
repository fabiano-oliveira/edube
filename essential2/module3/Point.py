import math

"""
Let's visit a very special place - a plane with the Cartesian coordinate system (you can learn more about this concept here: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

Each point located on the plane can be described as a pair of coordinates customarily called x and y. We expect that you are able to write a Python class which stores both coordinates as float numbers. Moreover, we want the objects of this class to evaluate the distances between any of the two points situated on the plane.

The task is rather easy if you employ the function named hypot() (available through the math module) which evaluates the length of the hypotenuse of a right triangle (more details here: https://en.wikipedia.org/wiki/Hypotenuse) and here: https://docs.python.org/3.7/library/math.html#trigonometric-functions.

This is how we imagine the class:

it's called Point;
its constructor accepts two arguments (x and y respectively), both default to zero;
all the properties should be private;
the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates (the coordinates are stored privately, so they cannot be accessed directly from within the object);
the class provides a method called distance_from_xy(x,y), which calculates and returns the distance between the point stored inside the object and the other point given as a pair of floats;
the class provides a method called distance_from_point(point), which calculates the distance (like the previous method), but the other point's location is given as another Point class object;
"""

class Point:
    def __init__(self, x = 0.0, y = 0.0) -> None:
        self.__x = x
        self.__y = y


    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        a = self.__x - x
        b = self.__y - y
        return math.hypot(a, b)

    def distance_from_point(self, point): 
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1:Point, vertice2:Point, vertice3:Point) -> None:
        self.__v1 = vertice1
        self.__v2 = vertice2
        self.__v3 = vertice3

    def perimeter(self):
        return self.__v1.distance_from_point(self.__v2) \
            + self.__v2.distance_from_point(self.__v3) \
            + self.__v3.distance_from_point(self.__v1)


p1 = Point(0, 0)
p2 = Point(1, 1)

print(p1.distance_from_point(p2))
print(p2.distance_from_xy(2, 0))

t = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(t.perimeter())