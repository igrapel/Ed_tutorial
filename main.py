

print("Hello World, Welcome to the course")
d1 = float(input("Deposit: "))
d2 = float(input("Deposit: "))
d3 = float(input("Deposit: "))
d4 = float(input("Deposit: "))
avg = (d1 + d2 + d3 + d4)/ 4
print(f"your average deposit is $ {avg:.2f}")

print("Next year, your interest rate will be: $", end=" \t")
next_year = avg*1.05
print("{:.2f}".format(next_year))


your_name = "Edward"
your_name = "e" + your_name[1:]
print(your_name)
your_name = "EdwarD"
my_list = ["Ed", "Joe", "Sara"]
print(my_list)
my_list[1] = "Don"
print(my_list)
