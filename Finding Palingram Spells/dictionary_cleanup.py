'''
Here, we remove other that alpha and single letter words from list if not 'a' or 'i'.
'''
import sys,re
def cleanup(file_path):
    try:
        with open(file_path,'r+') as dic_file:
            load_text = dic_file.read().strip().split('\n')
            load_text = [text for text in load_text]
            permissible = ('a','i')
            check = 'abcdefghijklmnopqrstuvwxyz'
            clean_txt=[]
            deleted_txt=[]
            for word in load_text:
                 if word.isalpha():
                    if len(word)>1:
                        clean_txt.append(word)
                    elif len(word) == 1 and word in permissible:
                        clean_txt.append(word)
                    else:
                        deleted_txt.append(word)
                 else:
                    deleted_txt.append(word)
            for word in clean_txt:
                dic_file.write(word + '\n')
            print(*deleted_txt,sep="\t")
            print(len(deleted_txt))
    except IOError as e:
        print(f"{e} error occured.\n Exiting...")
        sys.exit(1)

cleanup(input("Enter file path >"))