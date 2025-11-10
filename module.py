# # The outer loop runs 8 times, once for each row.
# for i in range(8):
    
#     # The inner loop runs 8 times *for each row*.
#     # It prints the '#' across the line.
#     for j in range(8):
#         # print() usually adds a new line,
#         # so 'end=" "' tells it to add a space instead.
#         print("#1", end=" 2")
    
#     # After the inner loop finishes a row,
#     # this empty print() adds the newline to move down.
#     print( "3")
# sumeven = 0
# sumodd = 0
# for numbers in range(101):
#     if numbers %2 == 0:
#         sumeven += numbers
#     else:
#         sumodd += numbers
# print (sumeven)
# print(sumodd)

# list = ['banana', 'orange', 'mango', 'lemon']
# for i in range(len(list)-1,-1,-1):
#     print((list[i]))
    
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
# print(add_two_numbers())

# def greetings (name):
#     message = name + ', welcome to Python for Everyone!'
#     return message
# print(greetings('Asabeneh'))

# def find_even_numbers(n):
#     evens = []
#     for i in range(n + 1):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
# print(find_even_numbers(10))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))