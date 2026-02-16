print("=" * 50)
print("Question 1: Student grade list")
print("=" * 50)

grades = [85, 92, 78, 95, 88]

grades.append(90)

grades.sort()   
print("Sorted grades:", grades)
print("Sorted grades:", grades[-1])
print("Sorted grades:", grades[0])
print("Total number of grades:", len(grades))
print()