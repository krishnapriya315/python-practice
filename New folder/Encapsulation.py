# *********************************

# class Bankaccount:
#     def __init__(self,owner_name,bank_balance,account_type):
#         self.owner_name=owner_name
#         self.__bank_balance=bank_balance        #private aakn (__) use cheyuka 
#         self._account_type=account_type         #protect cheyan( _ )use cheyuka

#     # to get the private atribute
#     @property
#     def bank_balance(self):
#         return self.__bank_balance

#     @property
#     def account_type(self):                 #def same name thanne kodukkuka
#         return self._account_type

#     #to  update the   value private attribute
    
#     @bank_balance.setter
#     def bank_balance(self,deposite_amt):
#         if deposite_amt <= 0:
#             raise ValueError("Deposite amount must be greater than 0")
#         self.__bank_balance = self.__bank_balance + deposite_amt

#     @account_type.setter
#     def account_type(self, acc_type):
#         if acc_type == "":
#             raise ValueError("Account type cannot be empty string")
#         self._account_type = acc_type


# bank=Bankaccount('ABC',12000,'saving') 

# print(bank._account_type)
# print(bank.bank_balance)

# #syntax:class.setter function =new value

# bank.bank_balance=120
# print(bank.bank_balance)

# # bank.account_type = "Current"
# # print(bank.account_type)


# # ************************************************

# class Employee:
#     def __init__(self,employee_name,department,salary):
#         self.employee_name=employee_name
#         self.department=department
#         self.salary=salary

#      # to get the private  attribute

#     @property
#     def salary(self):
#         return self.salary

    
#     # to update salary

#     @salary.setter
#     def salary(self,salary):
#         if salary=="":
#             raise ValueError('salary cannot be negative')
# salary=5000
# print(salary)

# class manager(Employee):
#     def display_detials(self):
#         print(self.employee_name,self.department)

#         @property
#         def department(self):



# *********************************

class vehicle:
    def __init__(self,_rental_type,vehicle_name,__rental_price):
        self._rental_type=_rental_type
        self.vehicle_name=vehicle_name
        self.__rental_price=__rental_price

    @property
    def rental_type(self):
            return self._rental_type

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, updated_rental_price):
        if updated_rental_price < 0:
            raise ValueError('rental price cannot be nagative')

    def display_detials(self):
        print(self.vehicle_name)
        print(self.rental_price)

# B

class Car(vehicle):
     def calculate_rante(self,day):
          self.day=day
          print('total rebtal cost',self.rental_price*day)

     def display_detials(self):
        print(self.vehicle_name)
        print(self.rental_price)
        print(self.rental_type)

class Bike(vehicle):
     def calculate_rent(self,day):
          self.days=day

          print('total rebtal cost',self.rental_price*day)

     def display_detials(self):
          print(self.vehicle_name)
          print(self.rental_price)
          print(self.rental_type) 



bike = Bike('mt','Bike',2000)

print(bike.calculate_rent(3))

bike.display_detials()

car=Car("bmw",'car',6000)
print(car.calculate_rante(3))
car.display_detials()








    
    
