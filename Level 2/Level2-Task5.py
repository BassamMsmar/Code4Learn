'''
5. Print a list contains the len of each word in the list using [normal list - list comprehension -
functional programming]
'''

names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha', 'sleem']


# -----------------------normal list-----------------------------------

list_len = []

for name in names:
    list_len.append(len(name))

print(list_len)
        
            

#-----------------------list comprehension------------------------------


list_len2 = [len(name) for name in names]
print(list_len)

# -----------------------functional programming------------------------


def list_len_name(names):
    
    return len(names)

result = map(list_len_name, names)

print(list(result))