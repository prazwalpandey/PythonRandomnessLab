'''
Now, we will try to find the phrase anagrams.
'''

from collections import Counter
import sys
import load_dictionary
'''

    1. We loaded the words from the dictionary by using the code and made sure 'a' and 'i' are also included and hence finally the collection is sorted.

    2. We ask the user for their name.

'''
load_text = load_dictionary.load("2of4brif.txt")
load_text.append('a')
load_text.append('i')
load_text.sort()
ini = input("Enter a name > ")

def main():
    name = ''.join(ini.lower().split())
    name = name.replace('-','')

    limit=len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase=phrase.replace(' ','')
        if len(temp_phrase)<limit:
            print(f"Length of the anagram phrase ={len(temp_phrase)}")
            find_phrase_anagrams(name)
            print("Current anagram phrase =",end=" ")
            print(phrase,file=sys.stderr)

            choice,name = process_choice(name)
            phrase+=choice+' '

        elif len(temp_phrase) == limit:
            print("\n *****FINISHED!*****\n")
            print("Anagram of name =",end=" ")
            print(phrase,file=sys.stderr)
            print()
            tryagain = input("\nTry again? (Press Enter else 'n' to quit)\n")
            if tryagain.lower()=='n':
                running=False
                sys.exit()
            else:
                main()
    return


def find_phrase_anagrams(ini):
    """

    1. In this function all the processing takes place.

    """
    name =ini
    # load = load_text
    anagram=[]
    name_letter_map = Counter(name.lower())
    for word in load_text:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if name_letter_map[letter]>=word_letter_map[letter]:
                test+=letter
        if Counter(test)==word_letter_map:
            anagram.append(word)

    print(*anagram,sep='\n')
    print()
    print(f"Remaining letters = {name}")
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining (real word) anagrams = {len(anagram)}")

def process_choice(name):
    '''

    1. Here we will provide the user with all the choices and asked to choose.

    '''
    while True:
        choice = input("Enter a word to select it else press enter to start again or '#' to exit. >")
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().strip())
        left_over_letter = list(name)
        for letter in candidate:
            if letter in left_over_letter:
                left_over_letter.remove(letter)
        if len(name)-len(left_over_letter)==len(choice) and choice.lower() in load_text:
            break
        else:
            print("Invalid, Chose any other word!")

    name=''.join(left_over_letter)
    return choice,name


if __name__ == "__main__":
    main()