import data
import math

# Write your functions for each part in the space below.

# Part 1
'''
Design recipe: first_element
input: List of lists of floating points
output: List containing the first element of each nested list from the input
purpose:output all of the first elements of a list of nested lists.
template: 
(1)check if empty list:
    (1.1) return []]
(2)create new list
(3)loop for list in listoflists        
(4) return new list
'''

def first_element(elementList:list[list[int]])-> list[int]:
    if elementList == []:
        return []
    results = []
    for lst in elementList:
        if lst:
            results.append(lst[0])

    return results

# Part 2
'''
Design Recipe: x_coordinates
input: List of point objects
output: List containing the x-coordinate of each point in the input list
purpose: Extract the x-coordinate of each point in a list of point objects.
template:
(1) Check if the input list is empty:
    (1.1) Return []
(2) Create a new list to store x-coordinates
(3) Loop through each point in the input list:
    (3.1) Append the x-coordinate of the current point to the new list
(4) Return the new list containing x-coordinates
'''

def x_coordinates(pointList:list[data.Point]):
    if pointList == []:
        return []
    results = []
    for point in pointList:
        results.append(point.x)
    return results
# Part 3
'''Design Recipe: are_in_positive_quadrant
input: List of point objects
output: List containing points located in the positive quadrant (first quadrant)
purpose: Filter out points from a list of point objects that are located in the positive quadrant (first quadrant).
template:
(1) Check if the input list is empty:
    (1.1) Return None
(2) Create a new list to store points in the positive quadrant
(3) Loop through each point in the input list:
    (3.1) Check if the x-coordinate and y-coordinate of the current point are both non-negative:
        (3.1.1) If true, append the point to the new list
(4) Return the new list containing points in the positive quadrant
'''

def are_in_positive_quadrant(pointList:list[data.Point]):
    if pointList == []:
        return None
    results = []
    for point in pointList:
        if point.x >= 0 and point.y >= 0: #0 is part of 1st quadrant
            results.append(point)
    return results

# Part 4
'''Design Recipe: distance
input: Two point objects representing coordinates in a 2D space
output: Euclidean distance between the two points
purpose: Calculate the Euclidean distance between two points in a 2D space.
template:
(1) Import the math library to access the square root function
(2) Calculate the squared difference of x-coordinates between pointA and pointB
(3) Calculate the squared difference of y-coordinates between pointA and pointB
(4) Sum the squared differences of x-coordinates and y-coordinates
(5) Take the square root of the sum to obtain the Euclidean distance
(6) Return the calculated Euclidean distance'''

def distance(pointA:data, pointB:data):
    return math.sqrt(((pointB.x - pointA.x)**2)+((pointB.y-pointA.y)**2))

# Part 5
'''Design Recipe: manhattan_distance
input: Two point objects representing coordinates in a 2D space
output: Manhattan distance between the two points
purpose: Calculate the Manhattan distance between two points in a 2D space.
template:
(1) Calculate the absolute difference of x-coordinates between pointA and pointB
(2) Calculate the absolute difference of y-coordinates between pointA and pointB
(3) Sum the absolute differences of x-coordinates and y-coordinates to obtain the Manhattan distance
(4) Return the calculated Manhattan distance
'''

def manhattan_distance(pointA:data, pointB:data):
    return float(abs(pointA.x - pointB.x) + abs(pointA.y - pointB.y))


# Part 6
'''Design Recipe: distance_all
input: List of point objects
output: List containing the Euclidean distance of each point in the input list from the origin (0,0)
purpose: Calculate the Euclidean distance of each point in the input list from the origin (0,0).
template:
(1) Check if the input list is empty:
    (1.1) If empty, return None
(2) Create a point object representing the origin (0,0)
(3) Create an empty list to store the distances
(4) Iterate over each point in the input list:
    (4.1) Calculate the Euclidean distance between the current point and the origin
    (4.2) Append the calculated distance to the results list
(5) Return the list containing all the distances'''

def distance_all(pointList):
    if pointList == []:
        return None
    origin = data.Point(0,0)
    results = []
    for pointA in pointList:
        results.append(distance(origin,pointA))
    return results


