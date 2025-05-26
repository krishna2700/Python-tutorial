# friend_ages={"Bob": 20, 
#              "Alice": 22, 
#              "Charlie": 19, 
#              "David": 21}

# friend_ages["Bob"]  = 25

# print(friend_ages)

# friends = [{"name": "Bob", "age": 20}, 
#     {"name": "Alice", "age": 22}, 
#     {"name": "Charlie", "age": 19}, 
#     {"name": "David", "age": 21}]

# print(friends[0]["name"])
# print(friends[0])


student_attendance = {"Rolf": 96,
                      "Bob": 80,
                      "Anne": 100,
                      "Charlie": 90}

# for student in student_attendance:
#     print(student, student_attendance[student])

for student, attendance in student_attendance.items():
    # print(student, attendance)
    print(f"{student} has {attendance}% attendance")


    if "Rolf" in student_attendance:
        print("Rolf is in the class")
    else:
        print("Rolf is not in the class")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))  # Average attendance