# # ******set*******
# 1
# print('fruits')
# print('Apple',' Banana','Orange','Mango','Grapes')
# print(len('fruits'))

# # 2

# numbers1 = [10, 20, 10, 30, 20, 40, 50, 30]
# print(set(numbers1))



# # 3

# colour={"red", "blue", "green"}
# colour.add('yellow')
# print(colour)
# colour.add('black')
# print(colour)
# colour.remove
# print('blue')

# 4

# student1 = {"Python", "Java", "SQL", "HTML"}
# student2 = {"Python", "C++", "SQL", "CSS"}
# student1.intersection
# print(student1.intersection(student2))


# 6

# students={'name':'rahul',
#                 'age':22,
#                 'course':'python',
#                 'city':'kochi'}
# print('whole dictionary')
# print(students)

# print(students['name'])
# print(students['age'])
# print(students['course'])
# print(students['city'])


# 7

# employee = { "name": "Anu", "age": 25, "salary": 30000}

# print('department','it')
# print(employee['name'])
# print(employee['age'])
# print(employee['salary'])

# # 8

# marks = { "Maths": 80, "Science": 75, "English": 90,"Computer": 85}

# print(marks.keys())
# print(marks.values())
# sum=marks['Computer']+marks['English']+marks['Maths']+marks['Science']
# print(sum)
# length=len(marks)
# print(length)
# print('avarage',sum/length)

# # 9

# student = {"name": "Arun", "age": 21, "course": "Python","marks": 85}

# print(type(student))
# print(student['name'])
# print(student['course'])
# if (student['marks'] >=50):
#     print('pass')
# else:
#     print('fail')     

# student['grade']='A'  
# print(student)  
# for g in student.items():
#     print(g)

# 10

morning_batch = {"Anu", "Rahul", "Arun", "Meera"}
evening_batch = {"Rahul", "Meera", "John", "Priya"}

class1=morning_batch.intersection(evening_batch) 
print("who attend both batches",morning_batch.intersection(evening_batch)) #{'Rahul', 'Meera'}
class2=morning_batch.difference(class1)
print("who attend only the morning batch: ",class2)                                       #{'Anu', 'Arun'}
# class3=evening_batch.difference(class1)
class3=evening_batch.difference(class1)
print("who attend only the evening batch.",class3)
union=morning_batch.union(evening_batch)
 
print("All unique student names across both batches ",union.difference(class1)) # {'John', 'Anu', 'Arun', 'Priya'}























