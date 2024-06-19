# This Program will help us to Demonstrate the
# Functinality of Relational Operator

a=int(input("Enter First Value :"))
b=int(input("Enter Second Value :"))

print("-"*30)

print("Results of Relational Operators ")

print("-"*30)

print("{} > {} = {}".format(a,b,a>b))
#a=10,b=20---> 10>20---> False
print("{} < {} = {}".format(a,b,a<b))
#a=10,b=20---> 10<20---> True
print("{} == {} = {}".format(a,b,a==b))
#a=10,b=20--->10==20--->False
print("{} != {} = {}".format(a,b,a!=b))
#a=10,b=20--->10!=20--->True
print("{} >= {} = {}".format(a,b,a>=b))
#a=10,b=20---> 10>=20--->False
print("{} <= {} = {}".format(a,b,a<=b))
#a=10,b=20---> 10<=20--->True
print("-"*30)
