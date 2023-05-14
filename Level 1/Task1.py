
'''
Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range

'''


def classify_number(x,y):
    odd  = []
    even = []

    for number in range(x,y+1):
        if number%2 == 0 :
            even.append(number)
        else:
            odd.append(number)
    return odd ,even


print(classify_number(1,10))


