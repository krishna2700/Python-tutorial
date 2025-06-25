student = {"name":"Krishna","grades":(88,90,78,77,95,85)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))  # This will print the average of the grades
 

class Student:
    def __init__(self):
        self.name = "Krishna"
        self.grades = (88,90,78,77,95,85)

    def average(self):
        return sum(self.grades) / len(self.grades)    




student = Student()
print(student.name)  # This will print the name of the student
print(student.grades)  # This will print the grades of the student
print(average(student.grades))  # This will print the average of the student's grades

print(student.average())  # This will print the average of the student's grades using the method in the Student class

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
student = Student("Krishna", (88, 90, 78, 77, 95, 85))
student2 = Student("Radha", (85, 92, 88, 90, 80, 95))
# print(student.name)  # This will print the name of the student
# print(student.grades)  # This will print the grades of the student
# print(student.average())  # This will print the average of the student's grades

print(student.name)  # This will print the name of the student
print(student.grades)  # This will print the grades of the student
print(Student.average_grade(student))  # This will print the average of the student's grades using the method in the Student class
print(student2.name)  # This will print the name of the second student
print(student2.grades)  # This will print the grades of the second student
print(Student.average_grade(student2))  # This will print the average of the student's grades using the method in the Student class