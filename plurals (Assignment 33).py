#Name: Richard Aguilar
#Date: June 20th, 2019
#This program: Takes in a series of nouns by the user, and then counts the number of nouns that are plural

nounString = input("Enter nouns: ")
wordCount = 0
plural = 0
wordRetainer = ""

for char in range(len(nounString)):

    if (nounString[char].isalnum() == True): #Checks if character is alphanumeric. If it is, it's concatenated to the variable
        wordRetainer = wordRetainer + nounString[char]

    if (nounString[char].isalnum() == False) or char == len(nounString) - 1: #Checks to see if loop has reached a space or the end of the string
        wordCount = wordCount + 1

        if (wordRetainer[(len(wordRetainer) - 1)] == 's'): #Checks to see if the character at the end of wordRetainer is an s, meaning it's plural
            #print(wordRetainer)
            #print(len(wordRetainer))
            #print(wordRetainer[len(wordRetainer) - 1])
            plural = plural + 1 
            wordRetainer = "" #After the plural has been noted, wordRetainer is cleared to make room for the next word
        else:
            wordRetainer = ""

print("Number of words: " + str(wordCount))
print ("Fraction of your list that is plural: " + str(plural/wordCount))