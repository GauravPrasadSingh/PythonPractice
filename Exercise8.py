'''
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations 
to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
# Welcome the user to the game and explain the rules
print('Welcome to our little rock paper scissors game!')
print('The rules are simple:')
print('Rock beats scissors')
print('Scissors beats paper')
print('Paper beats rock')
user1=input('Enter your name : ')
user2=input('Enter your name : ')
def decide_winner(answer1,answer2):
    if answer1 == answer2:
        return "It's a tie"
    elif answer1=='rock':
        if answer2=='paper':
            return 'paper wins'
        else:
            return 'rock wins'
    elif answer1=='scissors':
        if answer2=='paper':
            return 'scissors win'
        else:
            return 'rock wins'
    elif answer1 == 'paper':
        if answer2== 'rock':
            return 'paper wins'
        else:
            return 'scissors wins'           
    else:
        return 'Invalid input.'

while True:       
    user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
    user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)
    print(decide_winner(user1_answer,user2_answer))
    if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
    else:
        print('game over.')
        break  


# another approach
print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')

