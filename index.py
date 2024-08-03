def add(value1, value2):
    addition = value1 + value2
    return addition    

def subtract(value1, value2):
    subtraction = value1 - value2
    return subtraction

def multiply(value1, value2):
    multiplication = value1 * value2
    return multiplication

def divide(value1, value2):
    division = value1 / value2
    return division

method = input("Select mathematical method: (1) add (2) subtract (3) multiply (4) divide: ")
value1 = int(input("Enter your first value: "))
value2 = int(input("Enter your second value: "))

if method == "1":
    print(add(value1, value2))
elif method == "2":
    print(subtract(value1, value2))
elif method == "3":
    print(multiply(value1, value2))
elif method == "4":
    print(divide(value1, value2))

    