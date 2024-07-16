'''
Palingrams: a pair of words when read reversely spells same
Semordnilap: it's same as palingrams but the words like bats and stab are just same when spelled backward

This code is the optimized version of palingrams.py
'''
import time
import load_dictionary
def find_palingrams(file):
    loaded_txt = load_dictionary.load(file)
    hold_palin = []
    loaded = set(loaded_txt)
    for word in loaded:
        end = len(word)
        if end > 1:
            rev_word = word[::-1]
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in loaded:
                    hold_palin.append((word,rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in loaded:
                    hold_palin.append((rev_word[:end-i],word))
    return hold_palin

file_name = input("Enter the text file name to apply palingram function to > ")
start_time = time.time()
list =find_palingrams(file_name)
print(*list,sep='\t')
print(f"This dictionary file has {len(list)} palingram pair words.")
end_time = time.time()
print(f"\n\nThis program took {end_time-start_time} seconds to process.")
