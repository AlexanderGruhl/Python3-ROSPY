def get_name():
    name = input('Enter your full name: ')
    name = name.split()

    for s in reversed(name):
        print(s, end=' ')
    


