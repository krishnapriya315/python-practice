#1

def calculate_grade(mark):
 if("mark>=90"):
    print('A grade')
 elif("mark>=75"):
    print("B grade")
 elif("mark>=60"):
    print("C grade")
 elif("mark>40"):
  print("D grade")
 else:
  print("fail")

# 2
def calculator():
    num1=int(input('enter a number'))
    num2=int(input('enter a number'))
    operator=input('enter a number')
    if (operator=='+'):
        print=num1+num2
    elif(operator=='-'):
       print=num1-num2
    elif(operator=='*'):
       print=num1*num2
    elif(operator=='/'):
       print=num1/num2
    else:
       return('invalid symbol')


    # 3

def simple_intrest():
    interest=int(input("enetr your total amount: "))
    rate=int(input("enetr your interest rate: "))
    time=int(input("how many months: "))
    intrest_amount=(interest*rate*time)/100
    print(intrest_amount)
#simple_intrest()


#4

def last_charecter():
   charecter=input("type anything you like: ")
   charecter_last=charecter[-1]
   print(charecter_last)
#last_charecter()

#5

def calculate_bill():
   unit=int(input("enter your cunsumed unit: "))
   unit1=100*5
   next=100*7
   above=200*10
   if unit<=unit1:
        print(unit1+(unit-unit1)*5)
   elif unit<=next:
        print(unit1+next+(unit-next)*7)

   elif unit<=above:
        print(unit1+next+above+(unit-above)*10)

 
#calculate_bill()


#6

def count_even():
   list1=[20,21,35,66,78,99]

   for i in range(len(list1)):
      if list1

count_even()         