'''Poor Man's Bar Chart prepare a bar chart of no. of letters in given sentence.'''
import pprint
sentence = input("Enter your sentence > ")
bar_chart = {}
for i in sentence:
    i = i.lower()
    if i not in bar_chart and i != ' ':
        bar_chart[i]= []
        bar_chart[i].append(i)
    elif i != ' ':
        bar_chart[i].append(i)
pprint.pprint(bar_chart)
''' Expected Output:
Enter your sentence > Hello My Name is Prazwal Pandey
{'a': ['a', 'a', 'a', 'a'],
 'd': ['d'],
 'e': ['e', 'e', 'e'],
 'h': ['h'],
 'i': ['i'],
 'l': ['l', 'l', 'l'],
 'm': ['m', 'm'],
 'n': ['n', 'n'],
 'o': ['o'],
 'p': ['p', 'p'],
 'r': ['r'],
 's': ['s'],
 'w': ['w'],
 'y': ['y', 'y'],
 'z': ['z']}
 '''
