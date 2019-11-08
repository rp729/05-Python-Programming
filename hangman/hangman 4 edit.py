import pickle

def display_lib():
    eof = False
    while not eof:
        try:
            profile = open('profiles.dat', 'rb')
            load = pickle.load(profile)
            for i in load:
                print(i)
        except EOFError:
            eof = True
            print("File is empty")
            return 'empty'

if display_lib() == 'empty':
    profile = open('profiles.dat', 'wb+')
    dic = {}
    pickle.dump(dic,profile)
    profile.close()
    display_lib()
