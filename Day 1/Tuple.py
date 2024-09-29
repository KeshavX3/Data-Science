# # tuple ==> A tuple is a collection of items which is ordered and unchangable. Tuple Identification is = ().Indexing start from 0 and length start from 1.


# a = (34,'sam', 56, 'kritik')
# # a[2] = 'rubi'
# # print(a)
# b = list(a)
# print(b)
# b[2] = "rubi"
# print(b)


# a = ('sam' , 'raj' ,45 , 45.23 )
# for i in range(len(a)):
#     print(a[i] , end = " ")



#  How to create a user defined tuple ?
a = []
size = int(input("Enter size :"))
for i in range(size):
    val = int(input("Enter Numbers :"))
    a.append(val)
b = tuple(a)
print(b)