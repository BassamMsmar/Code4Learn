'''
8. Create a function that takes x,y and prints all the number that can be divide by y from x to 100

'''

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

def divide_by(x, y):
    for number in range(x, 101):
        if number%y == 0 :
            print(number)


divide_by(x, y)