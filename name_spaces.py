x = 90


def grades(n1, n2, n3):
    global result
    result = n1 + n2 + n3
    result /= 3
    return result

final_grade = grades(90, 80, x)
print(final_grade)


def combined_grades(s1):
    year = (result + s1)/2
    return year


print(combined_grades(100))

