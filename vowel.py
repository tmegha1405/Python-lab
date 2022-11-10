elem=input("Enter a word:")
vowels=["a","e","i","o","u"]
list=[]
for x in elem:
    if(x in vowels and x not in list):
        list.append(x)
print("Vowels present in the given word are:",list)
