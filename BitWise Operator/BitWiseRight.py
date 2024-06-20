#Program for Demonstrating BitWise Right Shift Operator

print("*"*20)
a=10
b=a>>3
print(b,type(b))
print("*"*20)
print("Without Using Variables ")
print("-"*20)
print(16>>2)     #---> 4
print("-"*20)
print(32>>3)     #----> 4
print("-"*20)
print(32>>2)  #----> 8
print("-"*20)
print(80.5 >> 4)     #TypeError: unsupported operand type(s) for <<: 'float' and 'int'
print("-"*20)