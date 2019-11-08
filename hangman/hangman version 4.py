import pickle

def main():
    file = open('welcome.txt')
    print(file.read())
    ticklemypickle = menu_display()
    while True:
        if ticklemypickle == 1:
            display_users()
            select = input("Enter user:")
            ticklemypickle = menu_display()
        elif ticklemypickle == 2:
            create_user()
            ticklemypickle = menu_display()
        elif ticklemypickle == 3:
            remove_user()
            ticklemypickle = menu_display()
        elif ticklemypickle == 4:
            user = 'guest'
        else:
            break

def menu_display():
    file = open('menu.txt')
    print(file.read())
    user_input = input("Enter your selection (number only):")
    user_input = menu_validation(user_input)
    file.close()
    return user_input

def menu_validation(self):
    if str.isnumeric(self) == False:
        self = input("INVALID INPUT: Enter your selection (number only):")
    self = int(self)
    return self

def create_user():
    profile = open('profiles.dat','wb')
    name = input("Enter username:")
    new_user = {'username':name,
                'score':0}
    pickle.dump(new_user,profile)
    profile.close()

def display_users():
    profile = open('profiles.dat','rb')
    eof = False
    while not eof:
        try:
            users = pickle.load(profile)
            display_data(users)
        except EOFError:
            eof = True

def load_users():
    profile = open('profiles.dat', 'rb')
    eof = False
    while not eof:
        try:
            users = pickle.load(profile)
            return users
        except EOFError:
            eof = True

def display_data(self):
    for i in self:
        print(self['username'])
        print(self['score'])

def remove_user():
    display_users()
    delete = input("Which user would you like to remove?")
    load = load_users()
    for i in load:
        if i['username'] == delete:
            load.remove[i]
    file = open('profiles.dat','wb')
    pickle.dump(load,file)
    file.close()


main()