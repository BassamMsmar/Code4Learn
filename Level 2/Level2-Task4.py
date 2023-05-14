'''
4. Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional
programming]
'''

names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha', 'sleem']
result = 0

# -----------------------normal list-----------------------

for name in names:
    if name.count('a') >= 2 :
        print(name)
        
        
            

#-----------------------list comprehension-----------------------

name_count_aa = [name for name in names if name.count('a')>= 2]
print(name_count_aa)

# -----------------------functional programming-----------------------

result = 0
def name_aa(name):
    if name.count('a') >= 2 :
        return(name)
        
my_name = filter(name_aa,names)
print(list(my_name))
