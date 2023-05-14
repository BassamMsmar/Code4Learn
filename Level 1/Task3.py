'''
3. Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y

'''


first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))

def print_multiplication(first_number,second_number):
   
    for number1 in range(first_number,second_number+1):
        for number2 in range(1,13):
            print(f"{number1} X {number2} = {number1*number2}")
        
        print('----------------------------------------------')


print_multiplication(first_number,second_number)