#activity 2 check wether a given number is armstrong or not
orig=int(input("enter your 3 digit number"))
sum=0
temp= orig
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if orig==sum:
    print("the number is an armstrong number")
else:
    print("the number is not an armstrong number")