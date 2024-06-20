#This program will help us to Understand the Special Points of "not Opetrator"

print(not 1)        #not 1 ---> Any Non-Zero Value is considered as True ---> not True ---> False
print("-"*20)
print(not 123)      #not 123 ---> Any Non-Zero value is considered as True ---> not True ---> False
print("-"*20)
print(not -345)     #not -345 ---> Any Non-Zero value is considered as True ---> not True ---> False
print("-"*20)
print(not 0)        #not 0 ---> not False ---> True
print("-"*20)
print(not "Nehal")  #not "Nehal" ---> Any Non-zero Value is considered as True---> not True ---> False
print("-"*20)
print(not "not")    #not "not" ---> Any Non-zero Value is considered as True---> not True ---> False
print("-"*20)
print(not "")       #not "" ---> There is no Space between "" ---> it considered as False ---> not False ---> True
print("-"*20)
print(not " ")       #not " " ---> There is Space between "" ---> it considered as True ---> not True ---> False
print("-"*20)
print(not "10-10")      #not "10-10" ---> It Considered as True ---> not True ---> False
print("-"*20)
print(not (10-10))      #not (10-10) ---> not 0 ---> not False ---> True