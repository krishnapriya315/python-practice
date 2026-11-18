# *****************************
# ************set**************
# *****************************

# declaring a set
# method1
# set1={}         #this is not set but it is a dictionary    
# # method 2 
# set2={12,55,88,2026,True,'bsnl',2026,2026.0,'2026'}
# # method 3
# set3=set ()

# print(type(set1))
# print(type(set2))
# print(type(set3))

# print(set2)     
# #value were displayed but not in the order.
# # set spports all datatype .i.e; heterogenous
# # duplicats are deleted


# print('****************************')
# roll={1,2,3,4,}
# roll_odd={1,3,5}
# roll_even={2,4,6}
# random={1,5,9,4}

# random.add(2026)       #add this elament into the set
# print(random)

# # different between set
# print(random.difference(roll_odd))  #{9,4,2026}
# print(roll_odd.difference(random))  #{3}

# print(roll.issuperset(roll_odd))
# print(roll.issubset(roll_odd))  #False
# print(roll.issuperset(random))  #False


# print(random.intersection(roll_even))
# print(roll.issubset(roll_odd))  
# print(roll.isdisjoint(random)) 

# 
#  
# support hetergenous datatype 
# cannot access data using index 
# duplicate are not allowed 
# mutable

# ********************************
# **********dictionary*******************
# *************************

# diclaring a set 
# method 1 
# dict1={}
# # method 2
# dict2={'key1': 'valuel','key3':'value2',8:2026,True:'yes it wors'}
# # method 3
# dict3=dict()        #dictionary


# print(type(dict1))
# print(type(dict2))
# print(type(dict3))

# print(dict2)
# # dictionaries keys and value can be of any datatype

# sample_dict={1:'one',0:'zero',1:'true',1:'ict'} #key are duplicate 
# print(sample_dict)
# dulication of keys are not allowed 

# dictionary[key]=value association with 'key


student_dict={'name':'keerthi',
               'age':33,
               'distict':'kottayam',
               'university':'MG'}

print('whole dictionary')
print(student_dict)

# print('key are')
print(student_dict.keys())

# print('value are')
print(student_dict.values())

# print('items are')
print(student_dict.items())

# modifying value of a key
student_dict['university']='kerala university'
print(student_dict)


# creat a new dictionary to store 


