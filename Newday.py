#TRY
#This is it.
#Length space as well 
# namin = input("ENTER name: ")
# print (len(namin))
# str = "Iam $"
# print(str.count(str))
# marks = int(input("Enter: "))
# if(marks >= 90):
#     print("Grade A")
# elif(marks >= 80 and marks < 90 ):
#     print("Grade B")
# else:
#     print("Failed")
# num = int(input("Enter num: "))
# if (num%2 == 0):
#     print("Even")
# else:
#     print("Odd")
# num1 = int(input("1st num:"))
# num2 = int(input("2nd num:"))
# num3 = int(input("3rd num:"))
# if(num1 > num2 and num1 > num3):
#     print("Greater num is",num1)
# elif(num2 > num1 and num2 > num3):
#     print("Greater num is",num2)
# else:
#     print("Greater num is",num3)
# sal = float(input())
# tax = sal * (0.1,0.2) [sal>50000 or sal == 50000]
# print(tax)
# list1 = [1 , 7, 5]
# list1.reverse()
# print(list1)
# m1 = str(input("N1: "))
# m2 = str(input("N2: "))
# m3 = str(input("N3: "))
# list1 = [m1, m2, m3]
# print(list1)

# list = ["a","d", "b"]
# list.sort(reverse= True)
# print(list)
# list =[1]
# print(list)
# print(type(list))
# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas', 9]
# formated_string = 'The following are python libraries:%s' % (python_libraries)
# print( formated_string)
# a = 4
# b = 3
# print(f'{a} + {b} = {a +b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b:.2f}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}') 
# language = 'Python'
# a,b,c,d,e,f = language # unpacking sequence characters into variables
# print(a) # P
# print(b) # y
# print(c) # t
# print(d) # h
# print(e) # o
# print(f) # n
# print(language)
# challenge = 'thirty days of python'
# print(challenge.count('y')) # 3
# print(challenge.count('y', 7, 14)) # 1, 
# print(challenge.count('th')) # 2`
# challenge = '\u00B2'
# print(challenge.isdigit())
# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = '# '.join(web_tech)
# print(result) # 'HTML# CSS# JavaScript# React'
# first = "coding" 
# second = "for" 
# third = "all"
# concatenated = f'{first} {second} {third}'
# print (concatenated)
# print("I am enjoying this challange.\nI just wonder what is next.")
# lst = ['item1','item2','item3', 'item4', 'item5']
# first_item, second_item, third_item, *rest = lst
# print(first_item)     # item1
# print(second_item)    # item2
# print(third_item)     # item3
# print(rest)           # ['item4', 'item5']
# First Example
# fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
# first_fruit, second_fruit, third_fruit, *rest = fruits 
# print(first_fruit)     # banana
# print(second_fruit)    # orange
# print(third_fruit)     # mango
# print(rest)           # ['lemon','lime','apple']
# # Second Example about unpacking list
# first, second, third,rest, *tenth = [1,2,3,4,5,6,7,8,9,10]
# print(first)          # 1
# print(second)         # 2
# print(third)          # 3
# print(rest)           # [4,5,6,7,8,9]
# print(tenth)          # 10
# # Third Example about unpacking list
# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic = countries
# print(gr)
# print(fr)
# print(bg)
# print(sw)
# print(scandic)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print (ages[0],ages[-1])
print (len(ages))
print(ages[0]-ages[-1])
print(ages[int(len(ages)/2)]/2)
print(ages)
a,b,c,d,e,f,g,h,i,j = ages
sum = a + b+c+d+e+f+g+h+i+j
avg = sum / len(ages)
print (avg)
