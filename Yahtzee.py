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
        if die1lock == True and die2lock == True and die3lock == True and die4lock == True and die5lock == True:
            rollnumber = 4
        else:
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
                        die2lock = False
                        question = 3
                        answer = True
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
                        print("Your answer must be yes or no.")
            if question == 5:
                answer = False
                while answer == False:
                    die5choose = input(f"Would you like to lock die 5's value, which is a {die5}? ")
                    if die5choose.lower() == 'yes':
                        die5lock = True
                        rollnumber = 3
                        answer = True
                    elif die5choose.lower() == 'no':
                        die5lock = False
                        rollnumber = 3
                        answer = True
                    else:
                        print('Your answer must be yes or no')


    if rollnumber == 3:
        if die1lock == True and die2lock == True and die3lock == True and die4lock == True and die5lock == True:
            rollnumber = 4
        else:
            print('Roll #3')
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
                print(f'Your new die 5 value is {die5}.')
            rollnumber = 4

    if rollnumber == 4:
        print(f'Your final die values are {die1}, {die2}, {die3}, {die4}, and {die5}.')

    return die1, die2, die3, die4, die5
print('Welcome to Yahtzee!')
rules = input('Would you like to know the rules? ')
if rules.lower() == 'yes':
    print('You have 3 rolls of 5 dice, and at any point you can choose to keep certain dice, and re-roll others.')
    print("You score points by choosing specific numbers, so for instance if you have 4 dice that show the number 3, that's 12 points")
    print('There are also set points, such as full house (3 of the same, and a pair), small straight (4 in a row), long straight (5 in a row)')
    print("There's also conditional ones, such as 3 of a kind, 4 of a kind, chance (all dice added up), and a YAHTZEE (5 of a kind)")
    print('A more detailed score breakdown will be provided later.\n')
print('In this game, we will have 3 rounds:\n'
      'The first round will consist of one round of rolling, where you can only try for a yahtzee worth 50 points.\n'
      'The second one is the conventional 13 rounds of rolling with standard rules.\n'
      'The last round is 5 rounds of rolling where you can only try for a yahtzee, with the first worth 50, the second worth 100 (so total 150), and so on.\n'
      'Good luck, and may the dice be in your favour.\n')

play = True
action = 1
while play == True:
    if action == 1:
        ask = input('Would you like to play? ')
        if ask.lower() == 'yes':
            action = 2
        elif ask.lower() == 'no':
            play = False
        else:
            print('Your answer must be yes or no')

    if action == 2:
        print('You have one attempt to get a yahtzee.')
        score = 0
        die1, die2, die3, die4, die5 = roll()
        if die1 == die2 == die3 == die4 == die5:
            print('YAHTZEE! 50 points!\n')
            score += 50
        else:
            print('You did not get a yahtzee.\n')
        action = 3
        rounds = 0
        roundcounter = 13
        scoring = 0

    if action == 3:
        while scoring != 1:
            print('Scoring is as follows:\n'
                  'Ones, Twos, Threes, Fours, Fives, and Sixes is in the upper bracket, and however many of that number you have is how many points you get. If you get 63 or more points, you get a 35 point bonus.\n'
                  'In the bottom bracket, full house is 25, short straight is 30, long straight is 40, chance is all dice added up, 3 of a kind is if you have 3 of the same, you add up all your dice. Same applies for 4 of a kind, just for 4 of the same.\n')
            scoring = 1
        Ones = False
        Twos = False
        Threes = False
        Fours = False
        Fives = False
        Sixes = False
        Threekind = False
        Fourkind = False
        FullHouse = False
        SmallStraight = False
        LongStraight = False
        Chance = False
        Yahtzee = False
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        score3kind = 0
        score4kind = 0
        scoreFullHouse = 0
        scoresmall = 0
        scorelarge = 0
        scorechance = 0
        scoreYahtzee = 0
        action = 4

    if action == 4:
        while roundcounter != rounds:
            die1, die2, die3, die4, die5 = roll()
            dice = [die1, die2, die3, die4, die5]
            from collections import Counter
            counts = Counter(dice)
            rounds += 1
            print('Time to select a category!')
            answer = False
            while answer == False:
                scoretype = input('What would you like to register points for?\n'
                                  'Ones, Twos, Threes, Fours, Fives, Sixes, 3 of a kind, 4 of a kind, Full House, Small Straight, Long Straight, Chance, or Yahtzee?\n')
                if scoretype.lower() == 'ones':
                    if Ones == True:
                        print('You already selected this in a previous round.')
                    elif die1 != 1 and die2 != 1 and die3 != 1 and die4 != 1 and die5 != 1:
                        confirm = input('None of your dice have 1, are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            Ones = True
                            answer = True
                        else:
                            print('Please select a different option.\n')
                    else:
                        score1 = 0
                        if die1 == 1:
                            score1 += 1
                        if die2 == 1:
                            score1 += 1
                        if die3 == 1:
                            score1 += 1
                        if die4 == 1:
                            score1 += 1
                        if die5 == 1:
                            score1 += 1
                        score += score1
                        print(f'You got {score1} points.\n')
                        answer = True
                        Ones = True

                elif scoretype.lower() == 'twos':
                    if Twos == True:
                        print('You already selected this in a previous round.')
                    elif die1 != 2 and die2 != 2 and die3 != 2 and die4 != 2 and die5 != 2:
                        confirm = input('None of your dice have 2, are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            Twos = True
                            answer = True
                        else:
                            print('Please select a different option.\n')
                    else:
                        score2 = 0
                        if die1 == 2:
                            score2 += 2
                        if die2 == 2:
                            score2 += 2
                        if die3 == 2:
                            score2 += 2
                        if die4 == 2:
                            score2 += 2
                        if die5 == 2:
                            score2 += 2
                        score += score2
                        print(f'You got {score2} points.\n')
                        answer = True
                        Twos = True

                elif scoretype.lower() == 'threes':
                    if Threes == True:
                        print('You already selected this in a previous round.')
                    elif die1 != 3 and die2 != 3 and die3 != 3 and die4 != 3 and die5 != 3:
                        confirm = input('None of your dice have 3, are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            Threes = True
                            answer = True
                        else:
                            print('Please select a different option.\n')
                    else:
                        score3 = 0
                        if die1 == 3:
                            score3 += 3
                        if die2 == 3:
                            score3 += 3
                        if die3 == 3:
                            score3 += 3
                        if die4 == 3:
                            score3 += 3
                        if die5 == 3:
                            score3 += 3
                        score += score3
                        print(f'You got {score3} points.\n')
                        answer = True
                        Threes = True

                elif scoretype.lower() == 'fours':
                    if Fours == True:
                        print('You already selected this in a previous round.')
                    elif die1 != 4 and die2 != 4 and die3 != 4 and die4 != 4 and die5 != 4:
                        confirm = input('None of your dice have 4, are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            Fours = True
                            answer = True
                        else:
                            print('Please select a different option.\n')
                    else:
                        score4 = 0
                        if die1 == 4:
                            score4 += 4
                        if die2 == 4:
                            score4 += 4
                        if die3 == 4:
                            score4 += 4
                        if die4 == 4:
                            score4 += 4
                        if die5 == 4:
                            score4 += 4
                        score += score4
                        print(f'You got {score4} points.\n')
                        answer = True
                        Fours = True

                elif scoretype.lower() == 'fives':
                    if Fives == True:
                        print('You already selected this in a previous round.')
                    elif die1 != 5 and die2 != 5 and die3 != 5 and die4 != 5 and die5 != 5:
                        confirm = input('None of your dice have 5, are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            Fives = True
                            answer = True
                        else:
                            print('Please select a different option.\n')
                    else:
                        score5 = 0
                        if die1 == 5:
                            score5 += 5
                        if die2 == 5:
                            score5 += 5
                        if die3 == 5:
                            score5 += 5
                        if die4 == 5:
                            score5 += 5
                        if die5 == 5:
                            score5 += 5
                        score += score5
                        print(f'You got {score5} points.\n')
                        answer = True
                        Fives = True

                elif scoretype.lower() == 'sixes':
                    if Sixes == True:
                        print('You already selected this in a previous round.')
                    elif die1 != 6 and die2 != 6 and die3 != 6 and die4 != 6 and die5 != 6:
                        confirm = input('None of your dice have 6, are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            Sixes = True
                            answer = True
                        else:
                            print('Please select a different option.\n')
                    else:
                        score6 = 0
                        if die1 == 6:
                            score6 += 6
                        if die2 == 6:
                            score6 += 6
                        if die3 == 6:
                            score6 += 6
                        if die4 == 6:
                            score6 += 6
                        if die5 == 6:
                            score6 += 6
                        score += score6
                        print(f'You got {score6} points.\n')
                        answer = True
                        Sixes = True

                elif scoretype.lower() == '3 of a kind':
                    if Threekind == True:
                        print('You already selected this in a previous round.')
                    elif max(counts.values()) >= 3:
                        score3kind = sum(dice)
                        score += score3kind
                        print(f'You got {score3kind} points.\n')
                        Threekind = True
                        answer = True
                    else:
                        confirm = input('You do not have a 3 of a kind. are you sure you want to record a 0? ' )
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            Threekind = True
                            answer = True
                        else:
                            print('Please select a different option.\n')

                elif scoretype.lower() == '4 of a kind':
                    if Fourkind == True:
                        print('You already selected this in a previous round.')
                    elif max(counts.values()) >= 4:
                        score4kind = sum(dice)
                        score += score4kind
                        print(f'You got {score4kind} points.\n')
                        Fourkind = True
                        answer = True
                    else:
                        confirm = input('You do not have a 4 of a kind. are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            Fourkind = True
                            answer = True
                        else:
                            print('Please select a different option.\n')

                elif scoretype.lower() == 'full house':
                    if FullHouse == True:
                        print('You already selected this in a previous round.')
                    elif sorted(counts.values()) == [2,3]:
                        scoreFullHouse = 25
                        score += scoreFullHouse
                        print(f'You got {scoreFullHouse} points.\n')
                        FullHouse = True
                        answer = True
                    else:
                        confirm = input('You do not have a full house. are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            FullHouse = True
                            answer = True
                        else:
                            print('Please select a different option.\n')

                elif scoretype.lower() == 'small straight':
                    unique = set(dice)
                    if SmallStraight == True:
                        print('You already selected this in a previous round.')
                    elif (
                            {1,2,3,4}.issubset(unique) or
                            {2,3,4,5}.issubset(unique) or
                            {3,4,5,6}.issubset(unique)
                    ):
                        scoresmall = 30
                        score += scoresmall
                        print(f'You got {scoresmall} points.\n')
                        SmallStraight = True
                        answer = True
                    else:
                        confirm = input('You do not have a small straight, are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            SmallStraight = True
                            answer = True
                        else:
                            print('Please select a different option.\n')

                elif scoretype.lower() == 'long straight':
                    if LongStraight == True:
                        print('You already selected this in a previous round.')
                    elif set(dice) in [{1,2,3,4,5}, {2,3,4,5,6}]:
                        scorelarge = 40
                        score += scorelarge
                        print(f'You got {scorelarge} points.\n')
                        LongStraight = True
                        answer = True
                    else:
                        confirm = input('You do not have a long straight, are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            LongStraight = True
                            answer = True
                        else:
                            print('Please select a different option.\n')

                elif scoretype.lower() == 'chance':
                    if Chance == True:
                        print('You have already selected this in a previous round.')
                    else:
                        scorechance = sum(dice)
                        score += scorechance
                        print(f'You got {scorechance} points.\n')
                        Chance = True
                        answer = True

                elif scoretype.lower() == 'yahtzee':
                    if Yahtzee == True:
                        print('You already selected this in a previous round.')
                    elif die1 == die2 == die3 == die4 == die5:
                        scoreYahtzee = 50
                        score += scoreYahtzee
                        print(f'YAHTZEE! {scoreYahtzee} points!\n')
                        Yahtzee = True
                        answer = True
                    else:
                        confirm = input('You do not have a yahtzee, are you sure you want to record a 0? ')
                        if confirm.lower() == 'yes':
                            print('You have recorded 0 for this section.\n')
                            Yahtzee = True
                            answer = True
                        else:
                            print('Please select a different option.\n')

                else:
                    print('Your answer must be from:\n'
                          'Ones, Twos, Threes, Fours, Fives, Sixes, 3 of a kind, 4 of a kind, Full House, Small Straight, Long Straight, Chance, or Yahtzee.')
        if roundcounter == rounds:
            action = 5

    if action == 5:
        scoretop = score1 + score2 + score3 + score4 + score5 + score6
        if scoretop >= 63:
            print("You got 63 or more points in your top bracket, earning you a 35 point bonus!\n")
            score += 35
        else:
            print("You did not get 63 or more points in your top bracket, so you don't get a bonus.\n")
        action = 6


    if action == 6:
        print('You now get 5 attempts to get a yahtzee.\n'
              'First yahtzee is worth 50, second one 100, third one 150, fourth one 200, fifth 250\n')
        yahtzeecounter = 0
        roundcounter = 5
        rounds = 0
        while roundcounter != rounds:
            die1, die2, die3, die4, die5 = roll()
            rounds += 1
            if die1 == die2 == die3 == die4 == die5:
                print('YAHTZEE!\n')
                yahtzeecounter += 1
            else:
                print('No yahtzee\n')
        if roundcounter == rounds:
            yahtzeescore = 0
            if yahtzeecounter == 0:
                print('You got no yahtzees.\n')
            elif yahtzeescore == 1:
                yahtzeescore = 50
                score += yahtzeescore
                print(f'You got 1 yahtzee! You get {yahtzeescore} points!\n')
            elif yahtzeescore == 2:
                yahtzeescore = 150
                score += yahtzeescore
                print(f'You got 2 yahtzees! You get {yahtzeescore} points!\n')
            elif yahtzeescore == 3:
                yahtzeescore = 300
                score += yahtzeescore
                print(f'You got 3 yahtzees! You get {yahtzeescore} points!\n')
            elif yahtzeescore == 4:
                yahtzeescore = 500
                score += yahtzeescore
                print(f'You got 4 yahtzees! You get {yahtzeescore} points!\n')
            else:
                yahtzeescore = 750
                score += yahtzeescore
                print(f'5 YAHTZEES???!!!! WHAT LUCK!!!! YOU GET {yahtzeescore} POINTS!!!\n')
            action = 7

    if action == 7:
        print(f'You finished with a score of {score}!')
        if score <= 200:
            print('You can do better.\n')
        elif score > 200 and score <= 400:
            print('Good Job!\n')
        elif score > 400 and score <= 600:
            print('Amazing Job!\n')
        elif score > 600 and score <= 800:
            print('Insane Score!\n')
        elif score > 800 and score <= 1000:
            print('Wow! What an inane score! You got really lucky!\n')
        elif score > 1000:
            print('With this luck, you should buy a lottery ticket. Great work!\n')
        action = 8

    if action == 8:
        ask = input('Would you like to play again? ')
        if ask.lower() == 'yes':
            action = 2
        elif ask.lower() == 'no':
            play = False
        else:
            print('Your answer must be yes or no.')

print('Thanks for playing!')