# Map Function() : The map() executes a specified function for each item in a iterable .
# the item is sent to the function as parameters

# a = ["3" , "45" , "89"]


# Method -1

#print(a)
#for i in range(len(a)):
#    a[i] = int(a[i])
#print(a)
#a[2] = a[2] + 1
#print(a[2])


# Method 2- (byr using map function )
# b = list(map(int , a))
# print(b)
# b[2] = b[2] + 1
# print(b[2])


# Example -2 
# a = [1,2,3,4,5]
# def squ(a):
#     return a*a

# square = list(map(squ , a ))
# print(square)


# a = [1,2,3,4,5]
# square  = list(map(lambda x : x*x , a))
# print(square)