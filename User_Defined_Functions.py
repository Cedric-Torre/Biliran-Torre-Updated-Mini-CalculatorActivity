def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        print("Cannot be divided, enter valid number.")
    else:
        return num1 / num2

def get_values(num1,num2):
    return num1,num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Select operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Get Values")

choice = input("Enter choice (1/2/3/4/5): ")

if choice == ('1'):
    total = addition(num1, num2)
    print(total)

elif choice == ('2'):
    total = subtraction(num1, num2)
    print(total)

elif choice == ('3'):
    total = multiplication(num1, num2)
    print(total)

elif choice == ('4'):
    total = division(num1, num2)
    if total is not None:
        print(total) 

elif choice == ('5'):
    num1, num2 = get_values(num1, num2)
    print("Values are:", num1, "and", num2)
        
