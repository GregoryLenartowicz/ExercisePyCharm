#! usr/bin/python3

# replay dictionary

a = {'apple':"fruit", "beetroot":"vegetable"}
a['doughnut']= "snack"

a.pop("apple")  # removing items (key name)

# del a       # delete dictionary completely

a2 = a.copy()  # copy method
print(a2)

a3 = dict(a)
print(a3)
print('above are two methods of copying ')

#print(a)
#print(a['doughnut'])
#print(a[0])  # error /KeyError: 0/

a['exemple'] = [4,5.1]

# from   https://www.w3schools.com/python/python_dictionaries.asp

for i in a:      # key in loop
    print(i)
print('///') # interlude

for i in a:      # value in loop
    print(a[i])
print('///')
for i in a.values():  # value in loop (another possibility)
    print(i)
print('///')

print(len(a))  # directory length
print('///')


del a['doughnut']
#print(a)

for k,v in a.items(): # itens method
    print(k,v)
print('//')


#a.clear()
#print(a)
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

r = dict([('ab',50), ("ad",100)]) # the dict constructor
print(r)
s = dict(ab=50, ad=100)   # easier
print(s)


# looping techniques
dict_anim = {'cat':'big', 'mause':'small'}
print(dict_anim)
for k,v in dict_anim.items():   # items method
    print(k,v)

for i,v in enumerate(['a','b','c']):  # enumerate function
    print(i,v)

s = dict_anim['cat']
print(s)

# from: https://www.w3schools.com/python/python_dictionaries.asp


# 5.5. Dictionaries  https://docs.python.org/3.8/tutorial/datastructures.html?highlight=dictionary#dictionaries

