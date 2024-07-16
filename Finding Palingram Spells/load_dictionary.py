'''
This python code extracts all the word  from file inputed and store it in list.
'''

import sys

def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [text.lower() for text in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\nError Opening {file}.\nTerminating program.",file=sys.stderr)
        sys.exit(1)

