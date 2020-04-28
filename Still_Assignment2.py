def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    return x % y

first = int(input("Please enter the first number:"))

second = int(input("Please enter the second number:"))

print('============')

print('Options')
print('1.   Add')
print('2.   Subtract')
print('3.   Multiply')
print('4.   Divide')
print('5.   Power')
print('6.   Modulo')

print('============')

option = input("Please select the calculation option:")

if option == '1':
  print("The answer is: ", add(first, second)) 
elif option == '2':
  print("The answer is: ", subtract(first, second))
elif option == '3':
  print("The answer is: ", multiply(first, second))
elif option == '4':
  print("The answer is: ", divide(first, second))
elif option == '5':
  print("The answer is: ", power(first, second))
elif option == '6':
  print("The answer is: ", modulo(first, second))
else:
  print("Wrong option!")