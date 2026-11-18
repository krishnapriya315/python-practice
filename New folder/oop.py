# student_name='keerthi'
# age=36
# student_1='grace'
# age=26
# student_2='akash'
# age=32
# student_3='vishnu'
# age=43
# student_4='ajith'
# age='23'
# print(student_name,age)
# print(student_1,age)
# print(student_2,age)
# print(student_3,age)
# print(student_4,age)


# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# student1=student('grace',26)

# print(student1.name,student1.age)

# class students:
#     def __init__(self,name,):
#         self.name=(name)
#         self.age=(age)

# student_2=students('neenu')
# print(student_2.name,student_2.age)


# class book:
#     def __init__(self,name,pages,author,year):
#         self.name=name
#         self.pages=pages
#         self.author=author
#         self.year=year

# book1=book


# class Employe:
#     # class attribute
#     age=24
#     def __init__(self,name,salary,id_no,job_role,joining_date):
#         self.name=name
#         self.salary=salary
#         self.id_no=id_no
#         self.job_role=job_role
#         self.joining_date=joining_date 

#     def display_details(self):
#         # print(self.name,self.salary,self.id_no,self.job_role,self.joining_date)



# # Employe1.display_details()




# # Employe1=Employe(name='ajin',salary='15000',id_no='632',job_role='asistant manager',joining_date='3/6/2026')
# # print(Employe1.name)
# # print(Employe1.salary)
# # print(Employe1.id_no)
# # print(Employe1.job_role)
# # print(Employe1.joining_date)

# Employe1.display_details()
# # accessing class attribute
# # print(Employe.age)


# class student:
#     count=0
#     def __init__(self,name,age,hight):
#             self.name=name
#             self.age=age
#             self.hight=hight
#             student.count=student.count+1
# # increment count by 1,when class has initializes
#     def display_count(self):
#         # print(student.count)

# student1=student('akash',16,172)


# class Animals:
#     def __init__(self,has_leg,speak):
#         self.has_leg=has_leg
#         self.speak=speak

# class Dog(Animals):
#     pass
# dog= Dog(has_leg='yes',speak='yes')

# print('the dog has 4 a legs',dog.has_leg)


# class Animal:
#     def __init__(self,sleep,eat):
#         self.sleep=sleep
#         self.eat=eat

# class Cat(Animal):
#         def __init__(self,sleep,eat):
#             super().__init__(sleep,eat)
#             self.speak='meow'

# cat=Cat(sleep='yes',eat='yes')
# print('the cat can sleep',cat.sleep)
# print('the cat can eat',cat.eat)

# *******************************************

# from typing import Any


# class Animal:
#      def __init__(self,name,age):
#           self.name=name
#           self.age=age

#      def eat(self):
#         return "the animal is eating"

# class Dog(Animal):

#      def bark(self):
#           print("Woof")

  
# class Cat(Animal):
#      def meow(self):
#           print("Meow")
#           return "Meow"



# cat = Cat("nim", 12)
# print(cat.name, cat.age, cat.meow(), cat.eat())


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display_details(self):
#         print(self.name,self.age)

# class students(Person):
#     def __init__(self, name, age,course):
#         super().__init__(name, age,course)
#         self.course='pgp'

# students=students('neenu',20)
# print(students,'name',students'age',students'course')

# # ****************************8


from abc import ABC,abstractmethod

class Bank(ABC):
#     @abstractmethod
#     def deposite(self):
#         pass

#     @abstractmethod
#     def deposite(self):
#         pass

# class SBI(Bank):
#     def deposite(self):
#         print('deposited is exicutive')

#     def loan(self):
#         print('appliting for sbi loan')

    


# SBI=SBI()
# SBI=deposite()
# SBI=loan()
        
# *******************************
#  from abc import ABC,abstractmethod
#from typing import Any


#  class shape(ABC):
#     @abstractmethod
#     def area(self,area): 
#         pass

#  class Rectangle(shape):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#         print(length*width)

#     def area(self,area):
#         return self.length , self.width

#  class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 *self.radius   
         
# Rectangle = Rectangle(5,4) 
# Circle = Circle(2.5)  

# print('Rectangle area:',Rectangle.area())
# print('circle area:',Circle.area())







        










          
          


    













