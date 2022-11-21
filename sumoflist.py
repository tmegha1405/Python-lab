flist=[]
slist=[]
sum1=0
sum2=0
len1=int(input("How many no.s do you want to add in first list?"))
for i in range(0,len1):
    inp=int(input("Enter the value of element:"))
    flist.append(inp)
len2=int(input("How many no.s do you want to add in second list?"))
for i in range(0,len2):
    inp=int(input("Enter the value of element:"))
    slist.append(inp)
if(len(flist)==len(slist)):
    print("Two list are of same length")
else:
     print("List have different length")
     for num in flist:
        sum1+=num
     for num in slist:
        sum2+=num
        if sum1==sum2:
            print("The sum of values of elements in both list are equal")
        else:
            print("The sum of values of both list elements are different")
        for num in flist:
              if num in slist:
               print(num,"found in both lists\n")
    
    
