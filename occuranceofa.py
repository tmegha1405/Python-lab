firstnamelist=[]
len=int(input("How many names do you want to insert:"))
for i in range(0,len):
    fname=input("Enter firstname you want to add to list:")
    firstnamelist.append(fname)
    count_a=0
for names in firstnamelist:
    count_a+=names.count("a")
print(count_a)
    
