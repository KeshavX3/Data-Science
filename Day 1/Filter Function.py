#Filter Function ==> The Fillter function returns an interator
#  where the items are filtered through a function to test ,
#  if the  item is accepted return true or false 


ages= [5,12,17,18,34,67,50]
def myFunc(x) :
    if (x<=18) :
        return True 
    else :
        return False 
    
kid = list(filter(myFunc , ages))
print(kid)
