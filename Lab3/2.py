temp = int(input("Enter temperature in celsius :"))
f = (temp * 9/5) + 32
print(f"{f} farenheit")


temp = int(input("Enter temperature in farenheit :"))
c = (temp -32)*(5/9)
print(f"{c} celsius")