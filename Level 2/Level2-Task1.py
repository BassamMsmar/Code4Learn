names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

print(names)


# -----------------------normal list-----------------------
for name in names:
    print(name.upper())



#-----------------------list comprehension-----------------------

name_upper= [ print(name.upper()) for name in names]
print (name_upper)



# -----------------------functional programming-----------------------


def conver_name(name):
    return(name.upper())


upper_name = map(conver_name, names)

print(list(upper_name))
