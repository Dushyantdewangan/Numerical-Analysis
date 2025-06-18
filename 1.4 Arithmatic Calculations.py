#program for arithmatic calculations 
x = int(input("Enter the value of x = "))
y = int(input("Enter the value of y = "))
print("Addition ke liye 1 likhiye")
print("Subtraction ke liye 2 likhiye")
print("Multiplication ke liye 3 likhiye")
print("Division ke liye 4 likhiye")
i = int(input("Chayanit ank hai "))
if(i==1):
    print("x + y = ", x+y)
elif(i==2):
    print("x - y =", x-y)
elif(i==3):
    print("x * y =", x*y)
elif(i==4):
    print("x / y =", x/y)
else:
    print("1 se 4 tak hi likhiye!! Aur kuch na likhiye!!")
