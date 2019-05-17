#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'#defining 52 letters
MAX_KEY_SIZE = len(SYMBOLS) #defining a constant

def getMode():#defining a function
#whether or not the user wants to encrypt/decrypt a message
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        #something I noticed: the things withing the print states have single quotes instead of double
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            #there are two options for the users of this program
            #they could either encrypt or decrypt messages
            #only these four things are "correct" responses
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
            #basically an error message that tells the user what to type in

def getMessage(): #gets the message the user wants to encrypt/decrupt (similar to get_string in C)
    print('Enter your message: ')
    return input() #taking in the message as an input

def getKey():
    key = 0 #initializing the varible key (you don't need to say the data type in python)
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) #asks user for key
        key = int(input()) #forcing the input to be a numerical value/ a integer
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key #as long as the key is within the limits, it can be used
            #if it is not within the range, the user is reprompted

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key #if mode is decrypt, move the key backwards through the alphabet instead of forwards
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS): #this is where the shift happens
            symbolIndex -= len(SYMBOLS) #the symbol or character becomes the encrypted or decrypted letter using the lenght of the SYMBOLS and key provided
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

#these functions are just being called
mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ') #prints out translated message
print(getTranslatedMessage(mode, message, key)) #print statements