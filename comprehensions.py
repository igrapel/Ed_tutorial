nums = [1, 2, 3, 4, 5, 6]

#List Comprehension
nums_cubed = [n**3 for n in nums]

print(nums_cubed)

evens_squared = [n**2 for n in nums if n%2 ==0]

print(evens_squared)

ids = [23, 44, 11, 18]
user_names = ["jonn", "dan", "sammy", "mika"]

caps = [n.upper() for n in user_names]
print(caps)

name_id = [(n, id) for n in caps for id in ids]
print(name_id)

name_ids = []
second_way = []
for i, n in enumerate(user_names):
    name_ids.append((n,ids[i]))


for i in range(len(user_names)):
    second_way.append((user_names[i], ids[i]))

print(name_ids)
print(second_way)