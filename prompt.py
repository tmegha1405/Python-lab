len=int(input("How many no.s do you want to store?"))
inputvaluelist=[]
for num in range(0,len):
    inputvalue=int(input('Enter a value'))
    if inputvalue>=100:
        inputvaluelist.append('OVER')
    else:
        inputvaluelist.append(inputvalue)
print(inputvaluelist)
