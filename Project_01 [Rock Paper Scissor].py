while True:
    print('''\t\n\nWELCOME!
    \tLET'S PLAY...!!! ''')
    print('''*********************************************************''')
    import random
    radnum=random.randint(1,3)
    ## Function
    def game_win(c, y):
        if c==y:
            print("\tit's a tie\n")
            print('''>>>>>>>>>>>>>>>>>>>>>>>>xxxxxxxxxxxxxxxxx<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<''')
        elif c==1 and y==2:
            print('\tyou win!\n')
            print('''>>>>>>>>>>>>>>>>>>>>>>>>xxxxxxxxxxxxxxxxx<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<''')
        elif c==2 and y==3:
            print('\tyou win!\n')
            print('''>>>>>>>>>>>>>>>>>>>>>>>>xxxxxxxxxxxxxxxxx<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<''')
        elif c==3 and y==1:
            print('\tyou win!\n')
            print('''>>>>>>>>>>>>>>>>>>>>>>>>xxxxxxxxxxxxxxxxx<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<''')        
        else:
            print('\tyou lose!\n')
            print('''>>>>>>>>>>>>>>>>>>>>>>>>xxxxxxxxxxxxxxxxx<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<''')
    ## Controls
    print('''For Rock press 1
    For Paper press 2
    For Scissors press 3
    ''') 
    print('''*********************************************************''')
    ## Computer selection [Backend]
    comp=print('\nComp choice: Rock, Paper, Scissors ?\n--> ...!')
    if radnum==1:
        comp=1
    elif radnum==2:
        comp=2
    elif radnum==3:
        comp=3

    ## Your choice
    you=int(input('\nYour trun: Rock, Paper, Scissors ?\n--> '))
    if you==1:
        print('\nYou choosed Rock')
    elif you==2:
        print('\nYou choosed Paper')
    elif you==3:
        print('\nYou choosed Scissors')
    
    else:
        print('\nplease Enter 1, 2 or 3')

    ## computer choice [Frontend]
    if comp==1:
        print('Computer choosed Rock')
        print('''*********************************************************\n''')
    elif comp==2:
        print('Computer choosed Paper')
        print('''*********************************************************\n''')
    elif comp==3:
        print('Computer choosed Scissors')
        print('''*********************************************************\n''')
    game_win(comp,you)


