import random


def rps():
    user = input('r for rock, p for paper, s for scissors: ')
    ai = random.choice(['r', 'p', 's'])
    if user in ['r', 'p', 's']:
        if win(user, ai):
            return 'You win!'
        elif user == ai:
            return 'It\' a tie!'
        else:
            return 'You lose!'
    else:
        print('Invalid input! Try again!')


def win(u, a):
    if (u == 'r' and a == 's') or (u == 'p' and a == 'r') or (u == 's' and a == 'p'):
        return True


if __name__ == '__main__':
    print(rps())
