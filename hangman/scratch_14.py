import pickle
dic = {}

def main():
    profile_select()


def profile_select():
    profile_select = input("RESPONSE:")
    if profile_select == '1':
        user = profile_create(dic)
        file = open('profiles.dat','wb')
        pickle.dump(user,file)

def profile_read():
    file = open('profiles.dat','rb')
    eof = False
    while not eof:
        try:
            pickled_profile = pickle.load(file)
            return display_data(pickled_profile)
        except EOFError:
            eof = True

def display_data(self):
    self_sort = sorted(self.keys)
    for i in self_sort():
        print(f'{i}')
        print(f'Name: {self["name"]}')

def profile_create(dic):
    print("CREATED PROFILES:")
    read = profile_read()
    num_key = input("Assign a number key for your user:")
    num_key = profile_validation(num_key)
    user_name = input("Enter user name:")
    dic[num_key] = {}
    dic[num_key]['name'] = user_name
    return dic

def profile_validation(num):
    while str.isdigit(num) == False:
        num = input("INVALID INPUT: Assign a number key for your user:")
    return int(num)

main()