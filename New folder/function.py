# # function to add 2 numbers 

# def display_sum(num1,num2):
#     sum= num1+num2
#     print('the sum of',num1,'and',num2,'is',sum)

#     # a.function will have 
#     # b.function name 
#     # c.input()
#     # d.body of the function (what the function actualy dose):mandatory
#     # e.output

#     # while we define input variable inthe function definition,we are 
#     # creating new variable with scope within the function


# # # call the function /invoking the function
# # display_sum(8,7)
# # display_sum(2026,8)
# # display_sum(9.8,6)


# def display_sum_custom():
#     print('we will display the sum of the 2 numbers you enter ')
#     num1=float(input('enter first number:'))
#     num2=float(input('enter second number:'))
#     sum= num1+num2
#     print('the sum of',num1,'and',num2,'is',sum)

# # display_sum_custom()

# def display_name_custom():
#     print('we will display the sum of name you enter')
#     # user=(input('enter name'))
#     print('hi',user)
#     print('good afternoon')
#     print('how are you')

# display_name_custom()

# # generating 3 multiplication table

# num=5
# print('multiplication table of',num)
# print('******************************')
# for i in range(1,11):
#     print(i,'*',num,'=',(i,num))
# print('**********************')

# num=8
# print('multiplication table of',num)
# print('******************************')
# for i in range(1,11):
#     print(i,'*',num,'=',(i,num))
# print('**********************')

# # function to display multiplication table of any number
# def display_multiplication_table():
#     print('we will display the multiplication table of the number you enter ')
#     # num=int(input('enter the number:'))
#     print('****************************')
#     print('multiplcation table of',num)
#     print('***********************')
#     for i in range(1,11):
#         print(i,'*',num,'=',(i,num))
#         print(f"{i}*{num}={i,num}")
#     print('********************')

# display_multiplication_table()    #invoking the function



# def calculation_sum(score_list1):
#     sum=0
#     for i in range(len(score_list1)):
#         sum=sum+score_list1[i]
#         print('total score={sum}')
#         return sum                              #output of the function

# def calcultion_sum(score_list1):
#     sum=0
#     for score in range(len(score_list1)):
#         sum=sum+score
#         print('total score={sum}')              #output of the function 
#         return sum 


# def calculation_avg(score_list1):
#     total=calculation_avg(score_list1)
#     count=len(score_list1)
#     avarage = total/count
#     print(f'avarage score={avarage}')
#     return avarage                          #output of the function
 

# ('**************************)
# ***********option argument******************
# **********************************

def calculate_exponent(num,exp=2):
    print(num**exp)

# calculate_exponent(5)
# calculate_exponent(5,3)

def create_wish(name,wish='good day'):
    print(f'hi{name},{wish}')

create_wish('anjaly')
create_wish('anjaly','good morning')

# we can give value of arguments explicity,
create_wish(wish ='good evening',name='anjaly')

# *******************************************
# **********************************************
# **********************************

def divide(num,den):
    result=num/den
    print(f'the answer is{result}')

divide(78,6)
divide(43,8)
divide('a','g')         #type error
divide(765,0)           #zerodivition error

# exception hnadiling
# we write specific criteria so that code flow is not interupted
# we write potential runtime erros making code inside 'try'
# rawriting the function with exception block

def divide_new1(num,den):
    try:
        result = num/den
        print(f'the answer is{result}')
    except Exception as e:
        print(f'thre is a problem:{e}')

        print('the end')

divide_new1(40,5)
divide_new1(345,0)
divide_new1('a','g')         
divide_new1(55,5) 


def divide_new2 (num,den):
    try:
        result = num/den
        print()
    except  TypeError:
        print('please make sure you are entering numbers')
    except ZeroDivisionError:
        print('please make sure to give a non zero value as denominetor')
    except Exception as e:
        print('thre is a problem:{e}')
        print('the end')

divide_new2(40,5)
divide_new2(345,0)
divide_new2('a','g')         
divide_new2(55,5)










          



    


