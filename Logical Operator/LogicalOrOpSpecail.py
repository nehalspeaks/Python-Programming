#This Program will help us to Understand the Special Points of " Or operator "

print(100 or 200)   #True or True ---> 100
print("-"*20)
print(100 or 0)     #True or True ---> 100
print("-"*20)
print(0 or 100)     #False or True ---> 100
print("-"*20)
print(0 or True or 200)     #False or True or True ---> True
print("-"*20)
print(100 or 200 or 0)      #True or True or False ---> 100
print("-"*20)
print("Python" or "Java" or "C" or "HTML")      #True or True or True or True ---> Python
print("-"*20)
print(0 and 30 or -123 and 0 and "Python" or True )