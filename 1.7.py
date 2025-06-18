# program for the sum of the digits
num=25
sum=0
while num>0:
    n=num%10
    sum+=n
    num=num//10
print("Sum of the digits = ", sum)