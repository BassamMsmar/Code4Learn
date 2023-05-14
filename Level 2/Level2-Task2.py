'''
2. Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional
programming]
'''

names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha', 'sleem']

# -----------------------normal list-----------------------
for name in names:
    if 'a' in name:
        print (name)


#-----------------------list comprehension-----------------------

name_a = [ print(item)for item in names if 'a' in item ]



# -----------------------functional programming-----------------------
def name_contains_a(item):
    if 'a' in item:
        return item


my_names = filter(name_contains_a, names)

print(list(my_names))
