# ********************************
# ********Arithametic************
# *******************************

# binary operatore we need mn of 2 operands 

num1 = 399
num2 = 5

sum = num1 +num2     
difference = num1-num2 
product = num1*num2
division = num1 /num2
exponent = num1 **  num2 
reminder =num1 % num2
floor =num1 //num2 

print(num1,'+',num2,'=',sum)
print(num1, '-', num2,'=',difference)
print(num1,'*',num2,'=',product)
print(num1,'/',num2,'=',division)
print('to power num1','**',num2,'=',exponent)
print('reminder of ', num1,'%',num2,'=',reminder)
print(num1,'//',num2,'=',floor)


# *******************************
# *****relational**************
# ******************************

print(num1, '>', num2, num1 > num2) 
print(num1, '<', num2, num1 < num2)
print(num1, '>=', num2, num1 <= num2)
print(num1, '>=', num2, num1 >= num2)
print(num1,'==',num2, num1 == num2)
print(num1,'!=',num2, num1 != num2)


# ***************************
# *********logical*********
# ***************************

#  and - all has to be in agreement
#  or -at least i must be in agreement
#  not -opposite 

#  operation are booleam

statement_1= True
statement_2= False
statement_3= True
statement_4=False

# AND

print(statement_1 and statement_2) # true and false=fals
print(statement_1 and statement_3) # true and true = true 
print(statement_2 and statement_4) # false and false =alse

# OR

print(statement_1 or statement_2)# true and false=fals
print(statement_1 or statement_3) # true and true = true 
print(statement_2 or statement_4) # false and false =alse

#NOT

print(not statement_2) # true 
print(not statement_1)#false
print(not statement_3) #true










 