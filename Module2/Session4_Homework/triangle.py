from point import Point

class Triangle:
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.__points = []
        self.__points.append(point1)
        self.__points.append(point2)
        self.__points.append(point3)

    def perimeter(self):
        return (self.__points[0].distance_from_point(self.__points[1]) + 
                self.__points[1].distance_from_point(self.__points[2]) + 
                self.__points[2].distance_from_point(self.__points[0]))

if __name__ == "__main__":
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())