s = "hello"
x = s.find("l")
print(x)

s = "hello"
for i in range(len(s)):
    print(i)

happy = input("Are you happy? (yes/no): ")
happy = happy.lower()
if happy == "yes":
    print("Smile")
elif happy == "no":
    print("Frown")
else:
    print("Invalid response")