def add(*numbers):
    return sum(numbers)

def multiply(*numbers):
    res=1
    for num in numbers:
        res*=num
    return res

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


square=lambda x:x*x

choices=(int(input("Enter 1 for addition, 2 for multiplication, 3 for factorial, 4 for square: ")))
if choices==1:
    nums=list(map(int,input('enter numbers').split()))
    print(add(*nums))
elif choices==2:
    nums=list(map(int,input('enter numbers').split()))
    print(multiply(*nums))
elif choices==3:
    n=int(input('enter number'))
    print(factorial(n))
elif choices==4:
    x=int(input('enter number'))
    print(square(x))
else:
    print("Invalid choice")