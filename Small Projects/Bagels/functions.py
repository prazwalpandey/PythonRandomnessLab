import random
def correct_answer():
    canswer = str(random.randint(100,999))
    return canswer.strip()

def input_answer():
    ianswer = input('>')
    return ianswer.strip()

def get_hints(ca,ia):
    '''Return the function with the hint i.e. PICO, FERMI, BAGELS'''
    if ca == ia:
        return 'You Got it!!'
    else:
        hint=[]
        for j in range(0,3):
            if ca[j] == ia[j]:
                hint.append('Fermi')
            elif ia[j] in ca:
                hint.append('Pico')
        if  len(hint) == 0:
            return 'Bagels'
        else:
            return hint