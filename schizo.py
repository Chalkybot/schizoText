#!/usr/bin/env python3
import sys
from random import randrange
from random import choice

input = list(sys.argv)
try:
    location=str(input[1])

except:
    print("Input file location not stated")
    exit()    
output =''
SchizoFrequency = 3
runningNum=0
swears = ['fuck','fucking','fucker','faggot','cunt','shit','shitter','retard','nigger','nigga','whore','bitch','slut']


inputFile = open(location,'r')
content=inputFile.read()
input=content.split(' ')
input = [s.replace("'","") for s in input]

for word in input:
    if word.lower() in swears: #and randrange(1*SchizoFrequency)==0:
        NewWord=''
        Censor = ['$','!','@','#','&','%']
        for letter in word:
            ToAdd=choice(Censor)
            Censor=[s.replace(ToAdd,'') for s in Censor]
            NewWord=NewWord+ToAdd
        word=NewWord
    # Random word capitalization
    if randrange(2*SchizoFrequency) == 0 or runningNum ==6:
        word = word.upper()
        runningNum=0
    # Random characters capitalized
    elif randrange(3*SchizoFrequency) == 0:
        word = ''.join(choice((str.upper,str.lower))(char) for char in word)
    # Randomly add a number of ? or .
    if randrange(3*SchizoFrequency) == 0:
        toadd=choice(['?','.'])
        word = word + toadd*(randrange(4)+1)
    #if wordrange(4*SchizoFrequency)==0:
    # sometimes turn a's into @ OR make one letter capitalized
    elif randrange(2*SchizoFrequency)==0:
        if word[randrange(len(word))].lower()=='a':
            word[randrange(len(word))]=='@'
        else:
            word[randrange(len(word))].upper()
    runningNum=runningNum+1
    if randrange(30*SchizoFrequency) == 0:   
        word=word+''
    else:
        word=word+' '
    
    output  = output + word

print(output)
