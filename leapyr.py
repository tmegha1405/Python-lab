Year=int(input("Enter the current year:"))
Fut=int(input("Enter the future year:"))
print("The leap year are")
for Year in range(Year,Fut+1,2):
    if((Year%4==0)and (Year%100!=0) or (Year%400==0)):
       print(Year)
