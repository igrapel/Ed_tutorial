
#Packing a variable
person1 = "Sammmy", 39, "VA"
print(type(person1))

person2 = "Donna", 52, "DC", "Attorney"
#unpacking
name, id, STATE = person1

print(id)

n2, id2, city2, attorney = person2
print(n2)

professions = ["coder", "attorney", "engineer", "teacher", "physician"]
*p, p1, p2 = professions
p_list = list(p)
print(p_list)


def add_many(*args):
    total = 0
    for a in args:
        total = total + a
    return total

print(add_many(10, 20, 30, 100, -200, -50))