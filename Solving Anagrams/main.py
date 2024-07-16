'''
In this program we will take a user input (word) and try to find all the corresponding anagrams from the dictionary.
'''
'''
Do you know that in Harry Porter "I am lord Voldemort" is an anagram from the student then "Tom Marvolo Riddle"
'''
import sys
def main(file):
    try:
        with open(file) as file_name:
            load_text=file_name.read().strip().split('\n')
            words=[txt for txt in load_text]
    except IOError as e:
        print(f"{e} error occured. Exiting....")
        sys.exit(1)
    u_word = input("Enter a word > ")
    user_word=sorted(u_word.lower())
    ana_list=[]
    for word in words:
        wo = sorted(word.lower())
        if user_word == wo and u_word.lower() != word:
            ana_list.append(word)
    print(f"All the anagrams for the word {u_word} in the dictionary are: ")
    print(*ana_list,sep="\t")
    return
if __name__ == "__main__":
    main("2of4brif.txt")