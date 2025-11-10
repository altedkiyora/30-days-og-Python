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

list = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(list)-1,-1,-1):
    print((list[i]))
    