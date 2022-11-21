flist=[]
slist=[]
sum1=0
sum2=0
len1=int(input("how many numbers do you want to add in first list?"))
for i in range(0,len1):
   inp=int(input("enter the value for element"))
   flist.append(inp)
len2=int(input("how many numbers do you want to add in second list?"))
for i in range(0,len2):
    inp=int(input("enter the value for element"))
    slist.append(inp)
if(len(flist)==len(slist)):
    print("two list are of same length")
else:
    print("list have diff length")
for num in flist:
        sum1+=num
for num in slist:
        sum2+=num
if sum1==sum2:
            print("the sum of values of elements in both lists are equal")
else:
            print("the sum of values of both lists elements are different")
for num in flist:
        if num in slist:
           print(num,"found in both lists\n")
                        
                
        



