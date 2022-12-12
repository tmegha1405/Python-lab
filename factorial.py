num=int(input("Enter the number:"))
def fact(num):
    factorial=1
    if num==0 or num==1:
       return 1
    for i in range(1,num+1):
        factorial=factorial*i
    return factorial
fact(num)
print("Factorial of",num,"is:",fact(num))