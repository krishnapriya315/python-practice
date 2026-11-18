# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     print('i am sudhakaran',self.name)

#     def display_details(self):
#         print(self.name)
#         print(self.age)

# class Employee(person):
#     def __init__(self, name,age,salary,joining_date, employee_id):
#         super().__init__(name, age)
#         self.employee_id=employee_id
#         self.salary = salary
#         self.joining_date=joining_date

#     print('employee_id,salary,joining_date')

#     def display_details(self):
#         print(self.employee_id)
#         print(self.salary)
#         print(self.joining_date)


# class Father(person):
#     def __init__(self,no_child,name,age):
#         super().__init__(name,age)
#         self.age=age
#         self.no_child=no_child
#         self.name=name

    

# class Sun(person):
#     def __init__(self,name,age):
#         super().__init__(name, age)
#         self.name=name
#         self.age=age

# class Husband(person):
#     def __init__(self, age,name,wife_name,no_of_child):
#         super().__init__(name,age)
#         self.age=age
#         self.name=name
#         self.wife_name=wife_name
#         self.no_of_child=no_of_child

# employee=Employee('')


 
# ******************************************

class BankAccount:
    def __init__(self,bank_balance,account_holder,account_type,):
        self.bank_balance=bank_balance
        self.account_holder=account_holder
        self.account_type=account_type


    @property
    def balance(self):
        return self.bank_balance

    @balance.setter
    def bank_balance(self,depocite_amt):
        if depocite_amt>=0:
            raise ValueError('balance cannot be negative')
        self.bank_balance=self.bank_balance
        

    def calculate(self):
        pass

    def deoposite(self,amount):
        if amount>0:
            self.Balance=self.balance+self.amount
            print(f"deposite succesful:{amount}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.Balance=self.balance-amount
            print('withdraw succesful:rs.',amount)

        else:
            print("balance")

    def display_detials(self):
        print("inaccount holder:",self.account_holder)
        print("acount type:",self.account_type)
        print("balance:rs.",self.balance)


# 2 savings account
class savingsAccount(BankAccount):
    def __init__(self, bank_balance, account_holder):
        super().__init__( account_holder,"savinhd",self.balance)

        def calculate_interest(self):
            return self.balance*5/100

# 3 

class currentAccount(BankAccount):
    def __init__(self, bank_balance, account_holder):
        super().__init__(account_holder,"current",self.balance)

        def calculate_interest(self):
            return self.balance*2/100

# 4 create accounts

ashbi=savingsAccount("ashbi",10000)
rahul=currentAccount("rahul",20000)


# perform these operations:

ashbi.deoposite(3000)
rahul.withdraw(5000)


rahul.deoposite(3000)
ashbi.withdraw(5000)

print("\n.....account_details..........")

ashbi.display_detials()
rahul.display_detials()

print("\n........annual interet........")

print("ashbi's annual inteest:rs.",ashbi.calculate_interest())
print("rahul's annual interest:rs.",rahul.calculate_interest())

         


    
    



















    def display_details(self):
        print(self.account_holder,self.account_type,self.balance)






