monday_class = {"Alice", "Bob", "Charlie", "Diana"}

wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

print("Mondy class ", monday_class)
print("Wedensday class ", wednesday_class)

both_classes = monday_class & wednesday_class
print("Attended in both classes:", both_classes)

all_students = monday_class | wednesday_class
print("All students who attended either class:", all_students)

only_monday = monday_class - wednesday_class
print("Only Monday class:", only_monday)

only_one = monday_class ^ wednesday_class
print("only one class:", only_one)
print("Is mondsay class a subset of all students?", monday_class<=wednesday_class)