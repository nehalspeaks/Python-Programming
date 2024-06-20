#Program for Demonstrating difference Between "and" And "&"

print("Programs for and : ")
print("-"*20)
print(10 and 4)     #True and True ---> 4
print(4 and 10 )    #True and True ---> 10
print(True and True )   #True and True ---> True
print("Apple" and "Mango")      #True and True --->Mango
print(10.3 and 6)   #True and True ---> 6
print(4 and 5)      #True and True ---> 5
print(5 and 4)      #True and True ---> 4
print("-"*20)

print("Programs for BitWise & :")
print("-"*20)
print(True & True )     #True & True ---> True
print(5 & 4)            #True and True ---> 4
print(4 & 5)            #True and True ---> 4
#print("Apple" & "Mango")    #TypeError: unsupported operand type(s) for &: 'str' and 'str'
#print(10.2 & 2)     #TypeError: unsupported operand type(s) for &: 'float' and 'int'
print("-"*20)