'''
Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y

'''



def divid_by(x,y):
   
    for number in range(1,101):
        if number%x==0 and number%y==0:
            print (number)

divid_by(2,4)