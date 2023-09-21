import random

win_conditions = {
    'p': 'r',
    's': 'p',
    'r': 's'
}

mapper = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
}
move_list = ['r', 'p', 's']
games_played = 0
score = {
    'computer': 0,
    'player': 0,
}
player_move = input('Please make your move [r]ock, [p]aper, [s]cissors or [e]xit ')
computer_move = random.choice(move_list)

while player_move != 'e':

    valid_key = False
    while not valid_key:
        try:
            valid_key = True if win_conditions[player_move] else False
        except KeyError:
            print('Wrong input. Try again')
            player_move = input('Please make your move [r]ock, [p]aper, [s]cissors or [e]xit ')

    if win_conditions[player_move] == computer_move:
        score['player'] += 1
        print(f'Player: {mapper[player_move]}')
        print(f'Computer: {mapper[computer_move]}')
        print('Round won by player')
    elif win_conditions[computer_move] == player_move:
        score['computer'] += 1
        print(f'Player: {mapper[player_move]}')
        print(f'Computer: {mapper[computer_move]}')
        print('Round won by computer')
    else:
        print(f'Player: {mapper[player_move]}')
        print(f'Computer: {mapper[player_move]}')
        print('Round tie')

    games_played += 1
    player_move = input('Please make your move [r]ock, [p]aper, [s]cissors or [e]xit ')
    computer_move = random.choice(move_list)

print(f'Total rounds played: {games_played}')
print('Score:')
for k, v in score.items():
    print(f'{k}: {v}')
