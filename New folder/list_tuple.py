#  list is a datatype user to a callection of value 
# since it is a combinetion of other datatype 
# we call it as a derived datatype 


# there is no rectriction in terms of datatype in a list
# a list can cantain variable type of data - Heterogenous 

# declaring a list

# method1

# ist_names1=[]
# print(type(ist_names1))

# # method 2

# ist_names2=['krishna','keerthi','grace','jayalekshmi','vishnu']
# print(type(ist_names2))

# # method 3                      
# ist_names3=list()
# print(type(ist_names3))

# # fetching value using index from a list 

# print(ist_names2[0])
# print(ist_names2[1])
# print(ist_names2[2])
# print(ist_names2[3])
# print(ist_names2[4])


# 

# personal info as a list :name ,age,univercity,graduation year 

# grace_info=['grace',21,2026,'mg',]
# print(type(grace_info))

# print(grace_info[0])
# print(type(grace_info[0]))
 
# print(grace_info[1])
# print(type(grace_info[1]))

# print(grace_info[2])
# print(type(grace_info[2]))

# print(grace_info[3])
# print(type(grace_info[3]))

# list1=[1,2,3,4,5,]
# list2=[False,True,False]
# print(list1+list2)          #list concantenation


# *******************************
# **********list function**********************
# ****************************

list1=[1,2,3,4,5,]
list2=[False,True,False]

ist_names2=['krishna','keerthi','grace','jayalekshmi','vishnu']

print(list1)
list1.sort()
print(ist_names2)


print(ist_names2)                #unsorted
ist_names2.sort()
print(ist_names2)               #sorted

list1.sort (reverse = True)     #sort the other way(descanding )
print(list1)                      #[7,3,1]

#ist_names2=['vishnu','ajith',7,3,1]

ist_names2.extend(list1)        #ist_names2 getrs extended with value of list1
print(ist_names2)


list2.append(list1)
#list will become [False, True, False, [5, 4, 3, 2, 1]
print(list2)
print(list2[3])


list1.append('a')
print(list1)

#reversing a list 

list1.reverse()
print(list1)            #['a', 1, 2, 3, 4, 5]


#checks the count of value 
print('the no of time false appear in the list =',list2.count(False))
print('the no of time true appear in the list =',list2.count(True))
print("the no of time 'x' appear in the list =",list2.count('x'))

# value at the last index
print(list2)
print('total number of elements in',list2,'is',len(list2))

len(list2)
print('total number of elements in',list2,'is',len(list2))

# value at the last index

print(list2[-1])
print(list2[len(list2)-1])

print('****************************')

print('befor clear ')
print(list2)

print('after clear')
print(list2)


print('**********************')

print(list2)    #[7,3,1,'a']
#in order to #[7,3,1,'a']->[7,3,100,1,'a']
#is inserting 100 at index 2

list1.insert(2,100)         #insorting 100 at index 2
print('after inserting a value',list1)


print('*****************************')

print('befor removing 3',list1)
list1.remove (3)
print('after removing 3',list1)

print('***************************')

list.pop
print(list1)





# ('*****************************************')
# ***********taple**************************
# ******************************************


# taple is a datatype used to store a callection of value 





# declaring a value
tuple1=()
tuple2= (2026,'now',2.75,False,[8,True,9,8])
tuple3= tuple()

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

print(tuple2[2])        #we can frtch value using index

print(tuple2.count('now'))
print(tuple2.index('now'))

# once a tuple created we cannot make changes to value.

# list->mutable can make changes to value.
# tuple ->inmutable cannot make change to value 

del(tuple2) #
del(list1)





