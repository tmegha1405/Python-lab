num=int(input("Enter the value:"))
print("The fibonacci series is:")
def fibonacci(num):
    n1=0
    n2=1
    count=0
    print(n1)
    print(n2)
    while(count<num-2):
         n3=n1+n2
         print(n3)
         n1=n2
         n2=n3
         count=count+1
fibonacci(num)

//
o/p
Enter the value:6
The fibonacci series is:
0
1
1
2
3
5
