'''
3. Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional
programming]
'''

names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha', 'sleem']


# -----------------------normal list-----------------------
for name in names:
    if name[0] == 't':
        print(name)


#-----------------------list comprehension-----------------------


name_start_t = [print(item) for item in names if item[0] == 't']

# -----------------------functional programming-----------------------


def name_if_start_t(name):
    if name[0] == 't':
        return(name)


my_names = filter(name_if_start_t, names)

print(list(my_names))
        
