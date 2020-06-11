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


# nested dictionaries

myfamily = {'child1' :{'name': 'Emily', 'year': 2000
            },'child2': { 'name': "Tobias", 'year': 2010},
            'child': {'name': 'Jordan', 'year': 2020}}
print(myfamily)

print('//')
a = myfamily.values()
b = myfamily.keys()
print(a)
print(b)
print('//')

c = myfamily.get('child')  # get method
print(c)


# from: https://www.datacamp.com/community/tutorials/python-dictionary-comprehension#pdc

# the general template for dictionary comprehension
# dict_variable = {key:value for (key,value) in dictionary.items()}

ty = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

tyx = { k : v*3 for (k,v) in ty.items()}
print(tyx)

# from    https://www.datacamp.com/community/tutorials/python-dictionary-comprehension#pdc

# check for items greater then 3

dict_1cond = { k:v for (k,v) in ty.items() if v>3}  # check by value
print(dict_1cond)

dict_2cond = {k:v for (k,v) in tyx.items() if k=="d"} # check by key
print(dict_2cond)

dict_3cond = { k:v for (k,v) in ty.items() if v>2 if v%2==0 if v%3==0}
print(dict_3cond)


# nested dictionary comprehension

nested_dict = {'first':{'a':1}, 'secend':{'b':2}}

float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items() }
              for ( outer_k, outer_v) in nested_dict.items()}
print(float_dict)

