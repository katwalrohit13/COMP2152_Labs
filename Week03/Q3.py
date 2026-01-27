print("=" * 50)
print("Question 3: Coordinate system(Tuples)")
print("=" * 50)

point1 = (3, 5)
print("The Point 1 is :", point1)

point2 = (7, 2)
print("The Point 2 is :", point2)

x1, y1 = point1
print("X1:", x1, ", Y1:", y1)

x2, y2 = point2
print("X2:", x2, ", Y2:", y2)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between the Points :", distance)
