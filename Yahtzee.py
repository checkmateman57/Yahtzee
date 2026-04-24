import random
def roll():
    rollnumber = 1
    if rollnumber == 1:
        print('Roll #1:')
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,6)
        die4 = random.randint(1,6)
        die5 = random.randint(1,6)
        print(f'You rolled a {die1}, {die2}, {die3}, {die4}, and {die5}')
        die1lock = False
        die2lock = False
        die3lock = False
        die4lock = False
        die5lock = False
        question = 1
        if question == 1:
            answer = False
            while answer == False:
                die1choose = input(f"Would you like to lock die 1's value, which is a {die1}? ")
                if die1choose.lower() == 'yes':
                    die1lock = True
                    question = 2
                    answer = True
                elif die1choose.lower() == 'no':
                    die1lock = False
                    question = 2
                    answer = True
                else:
                    print('Your answer must be yes or no.')
        if question == 2:
            answer = False
            while answer == False:
                die2choose = input(f"Would you like to lock die 2's value, which is a {die2}? ")
                if die2choose.lower() == 'yes':
                    die2lock = True
                    question = 3
                    answer = True
                elif die2choose.lower() == 'no':
                    answer = True
                    die2lock = False
                    question = 3
                else:
                    print('Your answer must be yes or no.')
        if question == 3:
            answer = False
            while answer == False:
                die3choose = input(f"Would you like to lock die 3's value, which is a {die3}? ")
                if die3choose.lower() == 'yes':
                    die3lock = True
                    question = 4
                    answer = True
                elif die3choose.lower() == 'no':
                    die3lock = False
                    question = 4
                    answer = True
                else:
                    print('Your answer must be yes or no.')
        if question == 4:
            answer = False
            while answer == False:
                die4choose = input(f"Would you like to lock die 4's value, which is a {die4}? ")
                if die4choose.lower() == 'yes':
                    die4lock = True
                    question = 5
                    answer = True
                elif die4choose.lower() == 'no':
                    die4lock = False
                    question = 5
                    answer = True
                else:
                    print('Your answer must be yes or no')
                    question = 4
        if question == 5:
            answer = False
            while answer == False:
                die5choose = input(f"Would you like to lock die 5's value, which is a {die5}? ")
                if die5choose.lower() == 'yes':
                    die5lock = True
                    answer = True
                    rollnumber = 2
                elif die5choose.lower() == 'no':
                    die5lock = False
                    answer = True
                    rollnumber = 2
                else:
                    print('Your answer must be yes or no')

    if rollnumber == 2:
        if die1lock and die2lock and die3lock and die4lock and die5lock == True:
            rollnumber = 4
        print('Roll #2:')
        if die1lock == False:
            die1 = random.randint(1,6)
            print(f'Your new die 1 value is {die1}.')
        if die2lock == False:
            die2 = random.randint(1,6)
            print(f'Your new die 2 value is {die2}.')
        if die3lock == False:
            die3 = random.randint(1,6)
            print(f'Your new die 3 value is {die3}.')
        if die4lock == False:
            die4 = random.randint(1,6)
            print(f'Your new die 4 value is {die4}.')
        if die5lock == False:
            die5 = random.randint(1,6)
            print(f'Your new die 5 value is {die5}')
        print(f'You now have {die1}, {die2}, {die3}, {die4}, and {die5}')
        question = 1
        if question == 1:
            answer = False
            while answer == False:
                die1choose = input(f"Would you like to lock or unlock die 1's value, which is a {die1}? ")
                if die1choose.lower() == 'lock':
                    die1lock = True
                    question = 2
                    answer = True
                elif die1choose.lower() == 'unlock':
                    die1lock = False
                    question = 2
                    answer = True
                else:
                    print('Your answer must be lock or unlock.')
        if question == 2:
            answer = False
            while answer == False:
                die2choose = input(f"Would you like to lock or unlock die 2's value, which is a {die2}? ")
                if die2choose.lower() == 'lock':
                    die2lock = True
                    question = 3
                    answer = True
                elif die2choose.lower() == 'unlock':
                    die2lock = False
                    question = 3
                    answer = True
                else:
                    print('Your answer must be lock or unlock.')
        if question == 3:
            answer = False
            while answer == False:
                die3choose = input(f"Would you like to lock or unlock die 3's value, which is a {die3}? ")
                if die3choose.lower() == 'lock':
                    die3lock = True
                    question = 4
                    answer = True
                elif die3choose.lower() == 'unlock':
                    die3lock = False
                    question = 4
                    answer = True
                else:
                    print('Your answer must be lock or unlock.')
        if question == 4:
            answer = False
            while answer == False:
                die4choose = input(f"Would you like to lock or unlock die 4's value, which is a {die4}? ")
                if die4choose.lower() == 'lock':
                    die4lock = True
                    question = 5
                    answer = True
                elif die4choose.lower() == 'unlock':
                    die4lock = False
                    question = 5
                    answer = True
                else:
                    print("Your answer must be lock or unlock.")
        if question == 5:
            answer = False
            while answer == False:
                die5choose = input(f"Would you like to lock or unlock die 5's value, which is a {die5}? ")
                if die5choose.lower() == 'lock':
                    die5lock = True
                    rollnumber = 3
                    answer = True
                elif die5choose.lower() == 'unlock':
                    die5lock = False
                    rollnumber = 3
                    answer = True
                else:
                    print('Your answer must be lock or unlock')


    if rollnumber == 3:
        print('Roll #3')
    if rollnumber == 4:
        print('Greetings')
roll()