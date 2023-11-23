import random


def rps():
    play_again = True
    while play_again:
        user = input('r for rock, p for paper, s for scissors: ')
        ai = random.choice(['r', 'p', 's'])
        if user in ['r', 'p', 's']:
            if win(user, ai):
                print('🎉🎉🎉You win!🎉🎉🎉')
            elif user == ai:
                print('It\' a tie!🤝')
            else:
                print('You lose!🥱🥱🥱')
        else:
            print('Invalid input!')

        play_again = input("Play again? Y for Yes or N for No: ").upper()
        while play_again != 'N':
            if play_again == 'Y':
                break
            else:
                print('Invalid input! Try again!')
                play_again = input("Play again? Y for Yes or N for No: ").upper()
        else:
            play_again = False


def win(u, a):
    if (u == 'r' and a == 's') or (u == 'p' and a == 'r') or (u == 's' and a == 'p'):
        return True


if __name__ == '__main__':
    rps()
