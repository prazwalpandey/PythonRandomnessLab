'''Caesar Cipher Hacker, by Prazwal D. Stark prazwaldstark@gmail.com
This program hacks messages encrypted with the Caesar cipher by doing 
a brute force attack against every possible key.
'''
#Let the user specify the message to hack.
print('Enter the encrypted Caesar cipher message to hack.')
message=input('>')
#Every possible message that can be encrypted/decrypted:
#(This must match the Symbols used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(SYMBOLS)): #Loop through every possible key.
    translated=''
    #Decrpyt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) #Get the number of the symbol.
            num = num - key #Decrypt the number.
        
            #Handle the wrap-around if num is less than 0:
            if num<0:
                num = num +len(SYMBOLS)
        #Add decrypted numbers's symbol to translated:
            translated = translated + SYMBOLS[num]
        else:
            #Add the symbol without decrypting:
            translated = translated + symbol
    #Display the key being tested, aling with its decrypted text:
    print('Key #{}: {}'.format(key, translated))