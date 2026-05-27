# Write A Python Program To Check Duplication of Student Identity In A  Student List


student=[]

n=int(input("enter no of student :"))

for i in range(n):
    student_id=input("enter student id:")

    if student_id in student:
        print("Duplicate student ID found ",student_id)
    else:
        student.append(student_id)
        print("student ID added ")

print("Final student list ",student)