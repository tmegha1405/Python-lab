def findLongestWord(wordList):
    highestLength=0
    for word in wordList:
        if(len(word)>highestLength):
            highestLength=len(word)
    return highestLength
words=input("Enter a series of words separated by spaces:").split(" ")
print(findLongestWord(words))
