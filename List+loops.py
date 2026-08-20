num = 0
students = ["Dina","Esraa","Kholod","Ayat","Mai"]
for list in students:
    num+=1
    print(num,"-",list)
def count_students(student_list):
    return len(student_list)
total = count_students(students)
print("Total of students in list:",total)
