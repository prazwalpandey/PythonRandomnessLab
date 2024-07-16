'''
Palingrams: a pair of words when read reversely spells same
Semordnilap: it's same as palingrams but the words like bats and stab are just same when spelled backward
'''

import load_dictionary
import time
start_time = time.time()
def find_palingrams():
    loaded_txt = load_dictionary.load("2of4brif.txt")
    hold_palin = []
    for word in loaded_txt:
        end = len(word)
        if end > 1:
            rev_word = word[::-1]
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in loaded_txt:
                    hold_palin.append((word,rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in loaded_txt:
                    hold_palin.append((rev_word[:end-i],word))
    return hold_palin

print(find_palingrams())

end_time = time.time()
'''
Here, I have used time module which uses time.time() function for starting time from 1st Jan 1970 and now by starting the time from the starting of the code to the end and differencing the time I have calculated the time for processing the whole function except for print and import time function.😊
'''
print(f"This program took {end_time-start_time} seconds for processing.")
