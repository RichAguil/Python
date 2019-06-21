#Name: Richard Aguilar
#Date: June 4th, 2019
#This program: Accepts a word and shifts it based on the key value

word = input("Enter a word: ")
cipherKey = 13;
codeWord = None
counter = 0

for wordCharacter in word:
    if (ord(wordCharacter) + cipherKey > 122): #This checks to see if new value is within ASCII bounds
        overFlowChar = chr(ord(wordCharacter) - cipherKey) #If not within ASCII bounds, it will take the original value, and subract 13 instead
        
        if (counter > 0): #This keeps track of how long the word is, so that when the second character is to be converted, it doesn't overwrite the first
            codeWord = codeWord + overFlowChar
            
        else:
            codeWord = overFlowChar
        counter = counter + 1
        
    else:
        if (counter > 0):
            codeWord = codeWord + chr(ord(wordCharacter) + cipherKey)
            
        else:
            codeWord = chr(ord(wordCharacter) + cipherKey)
        counter = counter + 1
        
print('Your word in code is: ' + codeWord)
