
subjects=("Python","Maths","DBMS")
print(subjects)

student={}

student_ID=[]

n=int(input("How many student do you want to access?"))

for i in range(n):
    print("Enter details of a student",i+1)

    student_ID=input("Enter Stuent ID:")

    while student_ID in student:
        print("Student id is already exists.Enter a unique ID.")
        student_ID=input("Enter Student ID:")

    name=input("Enter Student name:")


    marks=[]

    for subject in subjects:
        mark=int(input("Enter "+subject+" marks"))

        while mark<0 or mark>100:
            print("Invalid marks!")
            mark=int(input("Enter "+subject+" marks"))

        marks.append(mark)

    students = {
    "S101": {
        "name": "Aman",
        "marks": [78, 65, 88]
    },
    "S102": {
        "name": "Riya",
        "marks": [35, 72, 61]
    }
}
          
for student_id,details in student.items():

    name=details["name"]
    marks=details["marks"]

total=0

for mark in marks:
    total=total+mark


average=total/len(marks)

if average>=75:
    result="Distinction"

elif average>=40:
    result="Pass"

else:
    result="Fail" 


print("Student ID: ",student_ID)
print("Name:",name)

for i in range(len(subjects)):
    print(subjects[i]+":",marks[i])
print("Total:",total)
print("Average:",average)
print("Result:",result)           


print("Student IDs:", list(students.keys()))

student_id = input("Enter Student ID: ")

if student_id in students:
    print("Name:", students[student_id]["name"])

    print("1. Python")
    print("2. Maths")
    print("3. DBMS")

    subject_no = int(input("Enter subject number: "))
    new_marks = int(input("Enter new marks: "))

    if 1 <= subject_no <= 3 and 0 <= new_marks <= 100:
        students[student_id]["marks"][subject_no - 1] = new_marks
        print("Marks updated")
        print("New marks:", students[student_id]["marks"])
    else:
        print("Invalid subject number or marks.")

else:
    print("Student ID not found.")



passed_subjects=set()
for student_id,details in students.item():
    marks=details["marks"]

    for i in range(len(subjects)):
        if marks[i]>=40:
          passed_subjects.add(subjects[i])
          print("Subjects passed by at least one student:", passed_subjects)


          # Select two students
id1 = input("Enter first Student ID: ")
id2 = input("Enter second Student ID: ")

if id1 in students and id2 in students:

    passed1 = set()
    passed2 = set()

    # First student's passed subjects
    for i in range(len(subjects)):
        if students[id1]["marks"][i] >= 40:
            passed1.add(subjects[i])

    # Second student's passed subjects
    for i in range(len(subjects)):
        if students[id2]["marks"][i] >= 40:
            passed2.add(subjects[i])

    print("\nFirst Student Passed Subjects:", passed1)
    print("Second Student Passed Subjects:", passed2)

    # Set operations
    print("Union:", passed1 | passed2)
    print("Intersection:", passed1 & passed2)
    print("Difference (First - Second):", passed1 - passed2)
    print("Symmetric Difference:", passed1 ^ passed2)

else:
    print("Student ID not found.")

    print("\n========== CLASS SUMMARY ==========")

print("Total Students:", len(students))

averages = []

for student_id, details in students.items():
    marks = details["marks"]
    average = sum(marks) / len(marks)
    averages.append(average)

if len(averages) > 0:
    class_average = sum(averages) / len(averages)

    print("Class Average:", round(class_average, 2))
    print("Highest Average:", round(max(averages), 2))
    print("Lowest Average:", round(min(averages), 2))
# else:
#     print("No student records available.")
