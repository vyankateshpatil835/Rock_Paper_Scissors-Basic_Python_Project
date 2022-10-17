print('''WELCOME!
LET'S PLAY...!!! ''')
import random
radnum=random.randint(1,3)
## Function
def game_win(c, y):
    if c==y:
        print("it's a tie")
    elif c==1 and y==2:
        print('you win!')
    elif c==2 and y==3:
        print('you win!')
    elif c==3 and y==1:
        print('you win!')
    else:
        print('you lose!')
## Controls
print('''For Rock press 1
For Paper press 2
For Scissors press 3
''') 
## Computer selection [Backend]
comp=print('Comp choice: Rock, Paper, Scissors ?')
if radnum==1:
    comp=1
elif radnum==2:
    comp=2
elif radnum==3:
    comp=3
## Your choice
you=int(input('Your trun: Rock, Paper, Scissors ?\n'))
if you==1:
    print('You choosed Rock')
elif you==2:
    print('You choosed Paper')
elif you==3:
    print('You choosed Scissors')
else:
    print('please Enter 1, 2 or 3')
## computer choice [Frontend]
if comp==1:
    print('Computer choosed Rock')
elif comp==2:
    print('Computer choosed Paper')
elif comp==3:
    print('Computer choosed Scissors')
    game_win(comp,you)



