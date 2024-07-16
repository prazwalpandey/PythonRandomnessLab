'''
From this python code we pass the path of dictionary file and get the ouput from the
load_dictionary.py code as a list of dictionary word and then we check for palindrome words.
'''
import load_dictionary

def main():
    '''
    In this function all the loading of words into a list and checking is done.
    '''
    palindrome_list=[]
    words_list = load_dictionary.load("dictionary.txt")
    for word in words_list:
        if word[:] == word [::-1] :
            palindrome_list.append(word)
    print(f"\nNumber of Palindromes found = {len(palindrome_list)}")
    print(*palindrome_list,sep='\t')


if __name__ == "__main__":
    main()

