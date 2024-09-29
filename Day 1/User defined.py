# a = []
# size = int(input("Enter size"))
# for i in range(size):
#     val = int(input("ENter item:"))
#     a.append(val)
# print(a)



# Question 1  Program to find sum of elelments in a list 
# a = []
# size = int(input("Enter size:"))
# for i in range(size):
#     val = int(input("Enter number"))
#     a.append(val)
# print(a)
# sum = 0
# for i in range(size):
#     sum = sum + a[i]
# print("Sum of list elements = " , sum )



# Question 2  Write a program who count total number of odd and total number of even in the list ?
# a = []
# size = int(input("Enter Numbers:"))
# for i in range(size):
#     val = int(input("Enter number:"))
#     a.append(val)
# print(a)
# odd = 05
# even = 0
# for i in range(size):
#     if (a[i]%2 == 0):
#         even = even + 1
#     else:
#      odd = odd + 1
# print("Total Even = ", even , "Total Odd = ",odd)

#Question 3    Write a program who find maximum number in the list ?
a = []  
size = int(input("Enter size:"))
for i in range(size):
    val = int(input("Enter number:"))
    a.append(val)
print(a)
max = a[0]
for i in range(size):
    if (a[i] > max):
        max = a[i]
print("Maximum number is =", max)        