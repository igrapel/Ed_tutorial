

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