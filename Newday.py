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
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# print (ages[0],ages[-1])
# print (len(ages))
# print(ages[0]-ages[-1])
# print(ages[int(len(ages)/2)]/2)
# print(ages)
# a,b,c,d,e,f,g,h,i,j = ages
# sum = a + b+c+d+e+f+g+h+i+j
# avg = sum / len(ages)
# print (avg)
# tpl = (1,3,4)
# a, *b= tpl
# print(tpl)
# print (b)
# print(tpl[int(len(tpl)/2)])
# dict = {
#     "first" : "Ok",
# }
# print (dict)
# set = dict(
# )
# print(type(set))
# clt = {1,3,4}
# print(clt.pop())
# print(clt)

# i = 100
# while i >=1 :
#     print(i)
#     i-= 1

# print ("end")

# x = int(input())
# n = 1
# while n<=10 :
#     mult = x * n
#     print (mult)
#     n += 1
# print ("end")


# x = [3,4]
# y = 0
# z = len(x)-1
# while y <= z :
#     print(x[y])
#     y += 1
# print ("done")


# tup = (2,3,5,56,7,)
# i = int(input())
# x = 0
# while x < len(tup) :
#     if(tup[x] == i ):
#         print("found at : ",x)
#     else: print("ing")  
#     x+=1
# print ("end")

# tup = (2,3,5,56,7,)
# i = int(input())
# x = 0
# while x < len(tup) :
#     if(tup[x] == i ):
#         print("found at : ",x)
#         break
#     else:
#         print("ing")  
#     x+=1
#NOT today
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
# fruits.update(vegetables)
# print(fruits)
# syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.update(['item5','item6','item7'])
# print(st)
# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6', 'item7', 'item8'}
# st3 = st1.union(st2)
# print (st3)
# print(st1)
# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# print(st2.difference(st1)) # set()
# print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2
# del st1
# print(st1)
#Rev Session
# challenge = 'thirty days of python'
# print(challenge.split()) # ['thirty', 'days', 'of', 'python']
# challenge = 'thirty, days, of, python'
# print(challenge.split(' ')) # ['thirty', 'days', 'of', 'python']
# X = "I am a teacher and I love to inspire and teach people"
# print(X.split())
# Y = set(X.split())
# print(Y)
# print(len(Y)==len(X.split()))
# syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# values = dct['key1']
# print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

# def new(a):
#     b = a * 83
#     print(a , "usd=",b,"inr")
#     return b


# def home(a):
#     if a%2==0:
#      print("EVEN")
#     else:
#         print("ODD")

# home(9)

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return fact(n-1)*n
#     print(fact(n))

# print(fact(5))

# def pint(lst,idx):
#     if (idx == len(lst)):
#         return
#     print(lst[idx])
#     pint(lst,idx+1)
# LIst = ["man","ok"]
# pint(LIst, -1)

# def sum_sum(a,b):
#     sum = a + b
#     print (sum)
#     return sum
# sum_sum (5,5)
# print(sum_sum(52,5))


# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#         }
# }
# person['job_title'] = 'Instructor'
# person['skills'].append('HTML')
# print(person)

# dcdt = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dcdt.items()) 

# numbers = [0, 1, 2, 3, 4, 5]
# for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
#     print(number)       # the numbers will be printed line by line, from 0 to 5

# language = 'Python'
# for letter in language:
#     print(letter)


# for i in range(len(language)):
#     print(language[i])]

# numbers = (0, 1, 2, 3, 4, 5)
# for number in numbers:
#     print(number)

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# for key in person:
#     print(key)

# for key, value in person.items():
#     print(key, value) # this way we get both keys and values printed out

# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)

# def generate_full_name ():
#     first_name = 'Asabeneh'
#     last_name = 'Yetayeh'
#     space = ' '
#     full_name = first_name + space + last_name
#     print(full_name)
# generate_full_name () # calling a function
# print(generate_full_name)
# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     print(total)
# add_two_numbers()
# print (add_two_numbers)

# def generate_full_name ():
#     first_name = 'Asabeneh'
#     last_name = 'Yetayeh'
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print(generate_full_name())

# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     return total
# add_two_numbers
# print(add_two_numbers())

# def print_fullname(firstname, lastname):
#     space = ' '
#     full_name = firstname  + space + lastname
#     print(full_name)
# print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

# def print_fullname(firstname, lastname):
#     space = ' '
#     full_name = firstname  + space + lastname
#     print(full_name)
#     return full_name
# print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))


# # def add_two_numbers (num1, num2):
# #     total = num1 + num2
# #     print(total)
# # print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter

# print_fullname('s','p')
# print(print_fullname('s','pq'))