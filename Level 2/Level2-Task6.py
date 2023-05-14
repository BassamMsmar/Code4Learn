'''
6. Unpack the list in
7. a,b , a= the first index , b = rest of the list
8. a = the first index , b = the last index
9. a = the first index , b = the second index
'''

names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha', 'sleem']


# -----------------------a,b , a= the first index , b = rest of the list---------------------

a, *b = names
print(a)
print(b)


#-----------------------a = the first index , b = the last index-----------------------------

a, *_, b = names
print(a)
print(b)

# -----------------------functional programming------------------------

a, b, *_ = names
print(a)
print(b)