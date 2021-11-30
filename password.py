#Program 2: Password validator
#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
##input: P@ssw0rd+P@ssw0rd
#ouput: Valid

print("Your password must meet the following requirements: \n a) Greater than 15 letters; \n b) at least 1 capital letter is present; \n c) at least 1 number is present; and \n d) at least 1 special character is present.")

def count_capLet(password):
    capLetA=0
    capLet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
        "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for char in password:
        if char in capLet:
            capLetA+=1
    if capLetA>=1:
        return True
    else: 
        print("Your password is invalid: Add at least 1 capital letter")
        return False

def count_num(password):
    numB=0
    num=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for char in password:
        if char in num:
            numB+=1
    if numB>=1:
        return True
    else:
        print("Your password invalid: Add at least 1 numeric value")
        return False

def count_speChar(password):
    speCharC=0
    speChar=["!", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"
        "[", "{", "]", "}", "~", "#", ";", "@", ":", "'", ",", "<", ".", ">", "?", 
        "/", "¬", "`"]
    for char in password:
        if char in speChar:
            speCharC+=1
    if speCharC>=1:
        return True
    else: 
        print("Your password is invalid: Add at least 1 special character")
        return False