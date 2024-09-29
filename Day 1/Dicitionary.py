a = {"brand" : "kia" , "Model":"celtos" , "year" : "2023"}

# # a['year'] = 2024
# # print(a)
# # for i in a.keys() :
# #     print(i)

# # for i in a.values():
# #  print(i) 

# a['clor'] = 'cyan'
# print(a)



#Pre Defined functions in dicitionary 
# # 1. len()
# x= len(a)
# print("Total Length = " , x)


# 2 . Removing Itmes 
# (b) popitem() >> This Function removes the last element of the disct

# a.popitem()
# print(a)



#(c) . del
# del a["Model"]
# print(a)



#(5) . setdefualt()
# x = a.setdefault("clor" ,"white")
# a['colr '] = 'white'
# print(a)



#(6) update()
a.update({"Clor" : "black"})
print(a)