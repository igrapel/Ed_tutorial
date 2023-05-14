#non parameterized function
def greeting()-> None:
    print("Welcome to the next stage")

#parameterized
def personalized_greeting(n: str) -> None:
    print(f"We are glad you joined us, {n}.....")

def rectangle_area(length: float, width: float) -> float:
    return length*width

def find_volume_from_base(base_area: float, height: float) -> float:
    print(base_area * height)
    return base_area * height

def get_average_cost(total, workers):
    try:
        result = total / workers
        return result
    except ZeroDivisionError:
        print("You entered zero workers.")



greeting()
personalized_greeting("Joey")

personalized_greeting("Sam")

personalized_greeting("Donna")

base_area = rectangle_area(100, 200)
print(f"Your base area is {base_area}")

vol = find_volume_from_base(base_area, 10000)

print(f"Volume of building will be: {vol}")

try:
    cost = float(input("What were today's worker costs? "))
except ValueError:
    print("You need to enter a numerical input. ")

try:
    workers = float(input("How many workers were there today? "))
except ValueError:
    print("Needs numerical input")

try:
    avg = get_average_cost(cost, workers)
    if (avg == None):
        avg = "Improper Input"
    print("Average Cost: ", avg)
except NameError:
    print("You had bad inputs. We cannot perform the calculation. ")

finally:
    print("Thank you for using our software.")

