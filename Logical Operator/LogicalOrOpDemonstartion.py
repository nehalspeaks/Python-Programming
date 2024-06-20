# This program will help us to Demonstrate the functionality of Logical " Or Operator "

print(10>2 or 10>30)    #--> True and False --> True ---> #Short Length Evaluation
print("-"*20)

print(10>20 or 20>10)   #--> False and True --> True ---> #Full length Evaluation
print("-"*20)

print(10>20 or 20>30 or 10>4)   #--> False and False and True --> True ---> #Full Length Evaluation
print("-"*20)

print(10>2 or 30>20 or 10>2)    #---> True and True and True ---> True ---> #Short Length Evaluation
print("-"*20)

print(10>20 or 20>30)   #---> False and False ---> False---> #Full Length Evaluation
print("-"*20)

print(100>20 or 200>300 or 400>500)     #True or False or False --> True ---> #Short Length Evaluation
print("-"*20)