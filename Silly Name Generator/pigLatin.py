'''This simple code forms Pig Latin i.e. it takes an English word that begins with a consonant, move that consonant to the end, and then add ""ay" to the end of the word. If the word begins with a vowel, it simply add "way" to the end fo the word.'''

vowels = ('a','e','i','o','u')

word = input("Enter a word > ")

if word[0] in vowels:
    new_word = word + 'way'
else:
    new_word = word[1:]+word[0].lower()+'ay'

print(new_word)