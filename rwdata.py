# read and write data.txt
import os
import getpass


username = ''
password = ''
comments = True


def is_data():
    dane = False
    if os.path.exists('data.txt'):
        data = open('data.txt', 'r')
        lines = data.readlines()
        if len(lines) == 5:
            dane = True
    data.close()
    return dane


def get_data_from_file():
    data = open('data.txt', 'r')
    lines = data.readlines()

    user = lines[0].strip()
    passw = lines[1].strip()

    if lines[2].strip() == '1':
        comme = True
    else:
        comme = False

    data.close()
    return user, passw, comme


def get_data_from_user():
    print('No login data. Please give me your:')

    user = input('Librus account: ')
    passw = getpass.getpass(prompt='Password to librus: ')

    inr = input('Do you want to see comments during whole process?[y/n]')
    inr.lower()
    if inr == 'y':
        comme = True
    else:
        comme = False
    
    data = open('data.txt', 'w+')
    data.write(user)
    data.write("\n")
    data.write(passw)
    data.write("\n")
    if comme is True:
        data.write('1')
    else:
        data.write('0')


def init():
    if is_data() is False:
        get_data_from_user()

    username, password, comments= get_data_from_file()

    return username, password, comments
