import data
import lab4
import unittest
import math

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = []
        result = lab4.first_element(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        input = [point1, point2]
        result = lab4.x_coordinates(input)
        expected = [1, 2]
        self.assertEqual(expected, result)

    def test_x_coordinates2(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        input = []
        result = lab4.x_coordinates(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant1(self):
        point1 = data.Point(-2,20)
        point2 = data.Point(4,7)
        point3 = data.Point(3,-8)
        input = [point1,point2,point3]
        result = lab4.are_in_positive_quadrant(input)
        expected = [point2]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant2(self):
        point1 = data.Point(-2,20)
        point2 = data.Point(-4,7)
        point3 = data.Point(3,-8)
        input = [point1,point2,point3]
        result = lab4.are_in_positive_quadrant(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 4
    def test_euclidean_distance1(self):
        point1 = data.Point(-2,20)
        point2 = data.Point(-4,7)
        input1,input2 = point1,point2
        result = lab4.distance(input1,input2)
        expected = math.sqrt(173)
        self.assertEqual(expected, result)

    def test_euclidean_distance2(self):
        point1 = data.Point(2,2)
        point2 = data.Point(4,8)
        input1,input2 = point1,point2
        result = lab4.distance(input1,input2)
        expected = math.sqrt(40)
        self.assertEqual(expected, result)

    # Part 5
    def test_manhattan_distance1(self):
        point1 = data.Point(-2,20)
        point2 = data.Point(-4,7)
        input1,input2 = point1,point2
        result = lab4.manhattan_distance(input1,input2)
        expected = 15.0
        self.assertEqual(expected, result)

    def test_manhattan_distance2(self):
        point1 = data.Point(2,2)
        point2 = data.Point(4,8)
        input1,input2 = point1,point2
        result = lab4.manhattan_distance(input1,input2)
        expected = 8.0
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all1(self):
        point1 = data.Point(-2,20)
        point2 = data.Point(4,7)
        point3 = data.Point(3,-8)
        input = [point1,point2,point3]
        result = lab4.distance_all(input)
        expected = [20.09975124224178, 8.06225774829855, 8.54400374531753]
        self.assertEqual(expected, result)

    def test_distance_all2(self):
        point1 = data.Point(8,0)
        point2 = data.Point(2,5)
        point3 = data.Point(9,-8)
        input = [point1,point2,point3]
        result = lab4.distance_all(input)
        expected = [8.0, 5.385164807134504, 12.041594578792296]
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
