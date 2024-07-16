from functions import *
print('Bagels, a deductive logic game.')
print('By Prazwal D. Stark prazwaldstark@gmail.com\n\n')
print('I am thinking of a 3-digit number. Try to guess what it is in at most 10 guesses.')
print('Here are some clues:')
print('When I say:    That Means:')
print('PICO        -   One digit is correct but in the wrong direction.')
print('Fermi       -   One digit is correct and is in the right position.')
print('Bagels      -   No digit is correct.')
print('I have thought of a number.\nHere You Go!\nYou got 10 guesses.\n\n')
while True: #Main Game Loop   
    ca=correct_answer()
    for i in range(1, 11):
        print('Guess #{number}:'.format(number = i))
        ia=input_answer()
        answer = get_hints(ca,ia)
        if answer == 'You Got it!!':
            print('You Got it!!')
            break
        else:
            if i!=10:
                print(get_hints(ca,ia))
            else:
                print('Hey, You ran out of chances.')
                print('The correct answer was {ans}'.format(ans=ca))
                print('\nDo you want to play again?(Yes/No)')
                ques=input()
                if not ques.upper().startswith('Y'):   
                    break
    print('\nDo you want to play again?(Yes/No)')
    ques=input()
    if not ques.upper().startswith('Y'):   
        break       
print('Thanks For Playing!!')