# 1. write a Python to find the sum of all the elements in a lsit 

numbers = [1,2,3,4,5]
total_sum = 0 
for num in numbers:
    total_sum = total_sum + num
print("The sum of all elements in the list is :" , total_sum)

# 2. write a python program to merge two lists
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print("The merged list is :" , list3)


# 3. Write a Python program to find the second largest eleemnt in the list 

list1 = [10,20,4,45,99,105,2]
list1.sort()
print("The second largest element in the list is :" , list1[-2])


# 4.  Write a Python program to merge two dictionaries
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5,'f':6}
dict1.update(dict2)
print("The merged dictionary is :" , dict1)


# 5. Write a Python program to remove a key from dictionary
dict1 = {'a':1,'b':2,'c':3}
del dict1['b']
print("The dictionary after removing the key is :" , dict1)


# 6. Write  a Program to remove a element from set 
set1 = {1,2,3,4,5}
set1.remove(3)
print("The set after removing the element is :" , set1)



# 7.  Wite a Python program to find the maximum and minimum elelemts in a set
set1 = {55,6,4,25,98,86,1,85,0}
print("The maximum element in the set is :" , max(set1))
print("The minimum element in the set is :" , min(set1))


# 8. Write a python program to find the length of a tuple 
tuple1 = (1,2,3,4,5,6,7)
print("The length of the tuple is :" , len(tuple1))

# 9. Write a Python program to find the largest and samallest elements in a tuple
tuple1 = (55,66,7,5,32,86,745,1269,452,658,12,5,3,4,2,6,4,5,55,2,61754,8,4,42545445)
print("The largest element in the tuple is :" , max(tuple1))
print("The smallest element in the tuple is :" , min(tuple1))


# 10. Write a python program too print all even numbers between 1 and 100 using for loop 
for i in range(1,101):
    if i%2==0:
        print(i)


# 11. write a python program to sum the didgits to sum of a number using a while loop 
num = 123
sum = 0
while num > 0:
    sum = sum + num % 10
    num = num // 10
    print("The sum of the digits is :" , sum)

#  12. write a python program to calculte the sum of first 50 natural numbers using for loop
sum_numbers = 0
for i in range(1,51):
    sum_numbers += i
print("Sum of the first 50 natural : ", sum_numbers)


