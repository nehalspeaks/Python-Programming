# Program for Multiplying Three Numbers

x=input("Enter First Value : ")
y=input("Enter Second Value : ")
z=input("Enter Third Value : ")

#Convert Str intp Int
a=int(x)
b=int(y)
c=int(z)

z=a*b
temp=z*c

print("Mul of ({},{},{})={}".format(a,b,c,temp))

