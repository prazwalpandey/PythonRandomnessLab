'''Caesar Cipher, by Prazwal D. Stark prazwaldstark@gmail.com
The Caeser Cipher is a shift cipher that uses addtition and subtraction to encrypt
and decrpyt letters.
'''
try:
    import pyperclip #pyperclip copies text to the clipboard
except ImportError:
    pass
#Every possible symbol that can be encrypted/decrypted:
#(!)You can add numbers and puntuation marks to encrypt those symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('Caesar Cipher, by prazwaldstark@gmail.com - Prazwal D. Stark')
print('The Caesar Cipher encrypts letters by shifting them over by \'a\'')
print('key number. For example, a key of 2 means the letter A is')
print()
#Let the user enter if they are encrypting or decrypting:
while True:
    #Keep asking until the user enters e or d.
    response=input('DO you want to (e)ncrypt or (d)ecrypt?\n>').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

    #Let the user enter the key to use:

while True:
    maxkey= len(SYMBOLS) -1
    print('Please enter the key (0 to {})'.format(maxkey))
    response=input('>')
    if not response.isdecimal():
        continue
    if 0<= int (response)<len(SYMBOLS):
        key = int(response)
        break
#Let the user enter the message to encrypt/decrypt:
print('Enter the message to {}'.format(mode))
message= input('>')
#Caeser cipher only works on uppercase letters.
message= message.upper()
#Stores the encrypted/decrypted form of the messge:
translated = ''
#Encrypt/Decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
    #Ger the encrypted (or decrypted) number for this symbol.
        num= SYMBOLS.find(symbol)#Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        #Handle the wrap-around if num is larger than the length of
        #SYMBOLS or less than 0:
        if num>=len(SYMBOLS):
            num= num -len(SYMBOLS)
        elif num< 0:
            num = num + len(SYMBOLS)
        #Add encrypt/decrypt number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol
#Display the encrypted/decrypted string to the screen:
print(translated)
try:
    pyperclip.copy(translated)
    print('FUll {}ed text copied to clipboard.'.format(mode))
except:
    pass # Do nothing if pyperclip wasn't installed.



