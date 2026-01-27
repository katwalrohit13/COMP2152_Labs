print("=" * 50)
print("Question 1: Student grade list")
print("=" * 50)

grade = [85, 92, 78, 95, 88]

grade.append(90)

grade.sort()

print("Sorted grades:", grade)
print("Sorted grades:", grade[-1])
print("Sorted grades:", grade[0])
print("Total number of grades:", len(grade))
print()