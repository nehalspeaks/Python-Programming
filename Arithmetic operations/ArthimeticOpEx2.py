#Program for calculating Square root of a number without using sqrt() of math module

n=float(input("Enter a number for calculating Square root of a Number :"))
result=n**(1/2)

#OR result = n**0.5

print("Square root ({})={}".format(n,result))