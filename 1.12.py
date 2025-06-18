# program for checking amstrong number 
num = int(input("Enter number Eg 153 : "))
sum = 0
x = num 
while x>0:
    r=x%10
    sum+=r**3
    x//=10
if (sum==num):
    print("This is amstrong number")
else:
    print("This is not an amstrong number")






