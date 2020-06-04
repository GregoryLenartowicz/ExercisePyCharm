#! usr/bin/python3

# replay dictionary

a = {'apple':"fruit", "beetroot":"vegetable"}
a['doughnut']= "snack"

print(a)
print(a['doughnut'])
#print(a[0])  # error /KeyError: 0/

a['exemple'] = [4,5.1]

del a['doughnut']
print(a)

#a.clear()
print(a)
#del a

print(a.keys())
print(a.values())

#  from: https://docs.python.org/3.8/tutorial/datastructures.html?highlight=dictionary#dictionaries

print('apple' in a)   # fast membership testing
print('b' in a)

val_expr = {i: i**2 for i in (2,4,8)}  # dict comprehensions (value)
print(val_expr)

key_expr = {i-4: i for i in (4,8,12)}  # dict comprehensions (key)
print(key_expr)

# 5.5. Dictionaries  https://docs.python.org/3.8/tutorial/datastructures.html?highlight=dictionary#dictionaries

