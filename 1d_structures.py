import sys


my_large_tuple = tuple(range(9999999))
my_large_list = list(range(9999999))

num = int(input("Give me anumber"))

if num>100:
    print("Successful Operation")
    sys.exit(0)
else:
    print("Failure!")
    sys.exit((1))
print("Tuple: ", end=" ")
print(sys.getsizeof(my_large_tuple))
print("List: ", end=" ")
print(sys.getsizeof(my_large_list))

andy = ("Andy", 10000)
bob = ("Bob", 20000)
candice = ("Candice", 30000)


students = [andy, bob, candice]
a = [87, 89, 90, 85, 99]
b = [87, 89, 90, 85, 99]
c = []


def add_grades(l: list, num: int) -> list:
    for grade in range(num):
        g = int(input(f"What was the grade {grade + 1}: "))
        l.append(g)

    return c

def calc_gpa(grades: list) -> float:
    sum = 0
    for g in grades:
        sum = sum + g
    return sum/len(grades)

def update_grade(grades: list, index: int, grade: int):
    grades[index] = grade


c = add_grades(c, 4)

print(c)
gpa = calc_gpa(c)
print(f"Candice's GPA: {gpa}")

update_grade(a, 3, 97)
print("Andy: " + str(a))

print(students[1][1])
