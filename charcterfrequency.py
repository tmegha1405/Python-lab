def charFreq(str):
    wordCount=dict()
    for letter in set(str):
        wordCount[letter]=str.count(letter)
    return wordCount
word=input("Rnter a string to check for character frequency:")
print(charFreq(word))

//
o/p
Enter a string to check for character frequency:mgha
{'h': 1, 'm': 1, 'a': 1, 'g': 1}
