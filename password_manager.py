master_pwd = input('what is the master password: ')


def view():
     with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # return data on seperate lines
            data = line.rstrip()
            # returns a list
            user, passwd = data.split("|")
            print("user:", user, "Passwords:", passwd)

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + pwd + "\n")
        print('Added to file')

while True:
    mode = input('Would you like to add or view (view/add)?  Press q to quit. ').lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invald mode')
        continue

