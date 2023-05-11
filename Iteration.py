Deposit = 1000
interest = .1
years = 20

#Showing Balance after every year
for year in range(years):
    Deposit = Deposit * (1 + interest)
    print(f"After Year: {(year + 1)}")
    print(f"Your balance: {Deposit}", end = "\n\n")
    #Multiply Deposit by 1.04 and reassign to the variable
    #Deposit *= 1 + interest



for year in range(2000, 3000, 100):
    print("Leap Year: ", year)

#Figure out how long to achieve a certain amount:

Desired = 2000
Deposit = 1000
y = 0
while(Deposit <= Desired):
    y += 1
    Deposit = Deposit * (1 + interest)

print(f"It will take {y} years to reach ${Desired}")

#find and print all prime numbers in a range of numbers
import time

start_time = time.perf_counter()


low = 5
high = 10

print("Prime Search")
#2, 3, 5, 7
for num in range(low, high):
    #nested loop
    for i in range (2, num):
        #the modulus operator
        if ((num % i ) == 0):
            #not prime, no need to go farther in loop
            break
    else:
        print(num)


end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")

inp = input("Give me a number: ")


if(inp == "five"):
    inp = 5
elif(inp == "two"):
    inp = 2
elif(inp == "three"):
    inp = 3
elif(inp == "four"):
    inp = 4
elif(inp == "five"):
    inp = 5
elif(inp == "six"):
    inp = 6

print(inp)

sentinel = True
while(sentinel):
    inp = input("Ask me a question")
    if(inp == "exit"):
        break

