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

