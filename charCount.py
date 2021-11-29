#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

sntnc=input("What do you want to say?: ")
sntnc_low=sntnc.lower() # convert the words to lowercase

words=len(sntnc_low.split())
print("Words: ", words)

vows=["a", "e", "i", "o", "u"]
count=0
for char in sntnc_low:
    if char in vows: 
        count+=1
print("Vowels: ", count)
