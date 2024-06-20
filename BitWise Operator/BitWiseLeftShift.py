#Program for Demonstrating BitWise Left Shift Operator
print("*"*20)
a=10
b=a<<3
print(b,type(b))
print("*"*20)
print("Without Using Variables ")
print("-"*20)
print(4<<3)     #---> 32
print("-"*20)
print(9<<2)     #----> 36
print("-"*20)
print(10 << 0)  #---->10
print("-"*20)
print(10.7 << 3)
print("-"*20)   #TypeError: unsupported operand type(s) for <<: 'float' and 'int'