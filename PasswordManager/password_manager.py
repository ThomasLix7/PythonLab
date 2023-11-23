from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

if open('key.key', 'r').read() == '':
    create_key()

key1 = open('key.key', 'rb').read()
fer = Fernet(key1)

def creat_master_key():
    master_key = input('Create your admin password: ')
    open('masterkey.txt', 'a').write(fer.encrypt(master_key.encode()).decode())

if open('masterkey.txt', 'r').read() == '':
    creat_master_key()

input_masterkey = input("Input your admin password: ")
master_key = fer.decrypt(open('masterkey.txt', 'r').read().encode()).decode()
chance = 5
while input_masterkey != master_key and chance >= 0:
    if chance == 0:
        print('\n❌Sorry. Your account has been locked!❌')
        exit()
    print(f'\n❌ You have {chance} chances left !')
    chance -= 1
    input_masterkey = input("\nInput your admin password: ")
    continue

key2 = open('key.key', 'rb').read() + master_key.encode()
fer = Fernet(key2)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            print(f'UserName: {user}\nPassword: {fer.decrypt(password.encode()).decode()}\n')


def add():
    name = input('User Name: ')
    pwd = input('password: ')

    with open('passwords.txt', 'a') as f:
        f.write(f'{name}|{fer.encrypt(pwd.encode()).decode()}\n')


while True:
    mode = input("What do you want to do?\nV to view current passwords\nA to add new passwords\nQ to Quit: \n").upper()
    if mode == 'V':
        print('\n')
        view()
    elif mode == 'A':
        print('\n')
        add()
        print('\nAdded Successfully!\n')
    elif mode == 'Q':
        print('\nThank you for using! Goodbye!👋')
        break
    else:
        print("Invalid!")
        continue