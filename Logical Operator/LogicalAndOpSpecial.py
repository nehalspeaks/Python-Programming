#This Program will help us to understand the Special Points of " and Operator "

print(100 and 200)      #True and True ---> 200
print("-"*20)
print(100 and 0)        #True and False ---> 0
print("-"*20)
print(-24 and -34)      #True and True ---> -34
print("-"*20)
print(100 and 10 and 1)     #True and True and True ---> 1
print("-"*20)
print(100 and 0 and 200)    #True and False and True ---> 0
print("-"*20)
print(100 and True and -25)     #True and True and True ---> -25
print("-"*20)
print("Python" and "Java" and "HTML")   # True and True and True ---> HTML
print("-"*20)
print(True and True and "Python")   #True and True and True ---> Python