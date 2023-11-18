import os


game = True
lt = ''
n = 0
count = 0
letter_grid = ['A', 'B', 'C']
number_grid = [1, 2, 3]
player1_result = []
player2_result = []
output = """
    1    2    3\nA   %(1)s |  %(2)s  | %(3)s \n   -------------\nB   %(4)s |  %(5)s  | %(6)s \n   -------------\nC   %(7)s |  %(8)s  | %(9)s
        """
result = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
win_conditions = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]


print("""
   _____ _      _____     _     _____        
  |_   _(_)__  |_   ___ _| |__ |_   ____ ___ 
    | | | / _|   | |/ _` | / /   | |/ _ / -_)
    |_| |_\__|   |_|\__,_|_\_\   |_|\___\___|
      """)


def print_message():
    print('\nWelcome to the Tic Tac Toe game. This game is played by two players')
    print('\nType the location "A2", "3B" etc. to play "X" or "O" at the indicated spot. Your input is NOT case sensitive\n')


def print_players():
    print('Player 1: X')
    print('Player 2: O\n')


def print_game(player, index):
    if player == 1:
        lt = 'X'
    else:
        lt = 'O'

    if index == 0:
        print(output%result)
    else:
        result[str(index)] = lt
        print(output%result)


def get_input(player):
    for i in player:
        try:
            int(i)
        except ValueError:
            letter = i
        else:
            number = int(i)
    try:
        return (letter, number)
    except UnboundLocalError:
        return False


def clean():
    os.system('cls')
    print_players()


def check_win(player, number):
    global count
    if len(player) >= 3:
            for i in win_conditions:
                for j in i:
                    if j in player:
                        count += 1
                    
                    if count == 3:
                        print('Game Over')
                        print(f'Player_{number} wins')
                        return False
                        


def play_game():
    global game, n
    while game:
        if n == 0:
            start = input('Do you want to start the game (y/n): ').lower()
            if start == 'y':
                clean()
                print_game(0, 0)

        if start == 'y':
            n += 1
            if n%2 == 0:
                number = 2
            else:
                number = 1
            player_1 = input(f'\nPlayer_{number} turn: ').upper()

            if len(player_1) != 2:
                print('Invalid input please try again')
                n -= 1
            else:
                inputs = get_input(player_1)
                if not inputs:
                    print('Invalid input please try again')
                    n -= 1
                elif inputs[0] not in letter_grid:
                    print('Invalid letter please try again')
                    n -= 1
                elif inputs[1] not in number_grid:
                    print('Invalid number please try again')
                    n -= 1
                else:
                    num = letter_grid.index(inputs[0])
                    if num == 1:
                        num = 3
                    elif num == 2:
                        num = 6
                    index = num + inputs[1]

                    if index in player1_result or index in player2_result:
                        print('Location invalid. A player has already played at that spot.')
                        n -= 1
                    else:
                        if number == 1:
                            player1_result.append(index)
                        else:
                            player2_result.append(index)
                        clean()
                        print_game(number, index)
        else:
            end = input('Do you want to end the game (y/n): ').lower()
            if end == 'y':
                game = False
                print('\nThank you for playing')
    
        if len(player1_result) >= 3:
            game = check_win(player1_result, 1)
            if game:
                game = check_win(player2_result, 2)


print_message()
play_game()
