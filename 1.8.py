# program for reverse of a number
num = 96
i=0
rev=0
while num>0:
    n=num%10
    rev=rev*10+n
    num=num//10
print("Reverse of the number = ", rev)