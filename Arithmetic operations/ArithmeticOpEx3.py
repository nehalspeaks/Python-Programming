#Program for Demonstrating Cube Root of given number without using sqqrt() of math module

n=float(input("Enter a number for calculating Cube Root of a Number :"))
res=n**(1/3)
print("Cube Root ({})={}".format(n,res))
print("-------------OR--------")
print("Cube root ({})={}".format(n,round(res)))
