string1 = 'my name is krishnapriya'
string2 = 'python'
string3 = 'program'


print(string1)
print(string2)
print(string3)

print('\n')  
print(string2,string3)      


# by defalte python print a new line at the end.

# changing the end string from '\n' to the end

print(string1, end='&') #python &
print(string2, end='&') #program &
print('\n', end='&')    #new line &
print(string1,string2,end='&') #python programing &


# \n(\t\t', string2, '\n', string2)

print('********************')


print(string2,string3)

s1 = 'ict'
s2 ='academy'
s3 = 'of'
s4 = 'kerala'



print(s1+s2+s3+s4)      # ictacademyofkerala
print(s1,s2,s3,s4)      # ict academy of kerala

combined_string ='s1'+'s2'+'s3'+'s4'
print(combined_string)      #ict academy of kerala

print('*****************************')

print(s1)
print(s1 + s2 + s3 + s4)
print(s1*5)

print( (s1 + '') *5)
print(( s1+'\t' )*5)
print((s1+ '\n')*5)

print('*********************index*********')

print(string3)          #programing
print(string3[0])       #print charecter value at 0th index
print(string3[5])       
print(string3[2])     
# print(string3[21])      # we cannot go beyond the msximum index of a string.

string1 = 'krishnapriya' 
print(string3[-5]) 

s1= ('thiruvanandhapuram')
print(s1[-4])
print(s1[6])     #last index value 



# **************************************
# *********string slicing***************
# ******************************


s1 = 'trivandrum'
print(s1[6])
print(s1[-4])

print(s1[0:5])
print(s1[6:10])
print(s1[-10])
print(s1[4:7])

print(s1[:5])       # from start index till 5    'triva'
print(s1[6:1])       # from 6th index till index 'drum'

print(s1[0:5:2])        # intrudacing step operator. (by default,step 1s 1)
print(s1[:5:2])         #'tia'

# string_name [starting name index :ending index :step]
print(s1[0:8:3])  # 'tvd'  

string_demo = "join our offline program is kerla it park"
print(string_demo[5:])      
print(string_demo[5::2])    # 5th ill ninnum thungittu end vare ullath 

# reversing &string.

print(s1[::-1])             # back ill ninnum frendlekku 
print(string_demo[::-1])    # end ill ninnum thudangunnu 

#**************************************
#****************functions********************
#************************************


print(s1)
print(s1.lower())       # convert string to lowe case 'trivandru m'
print(s1.upper())       # convert string to upper case 'TRIVANDFRUM'
print(s1.swapcase())    # switch case of each of charector in the string 'TRIVANDRUM'
print(s1.capitalize())  # first letter it upper and the rest will be lower 'Trivandrum'









