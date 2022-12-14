def charFreq(str):
    wordCount=dict()
    for letter in set(str):
        wordCount[letter]=str.count(letter)
    return wordCount
word=input("Rnter a string to check for character frequency:")
print(charFreq(word))