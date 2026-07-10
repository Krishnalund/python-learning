#python program capable of playing this game with the user.
#Snake Water Gun Game

import random
user_dict={'s':1 , 'w':-1 , 'g':0}
reversed_dict={1:'Snake' , -1:'Water' , 0:'Gun'}

computer=random.choice([-1,0,1])
user_input=input('Enter your choice(S = Snake, W = Water, G = Gun): ').lower()

if user_input not in user_dict:
    print('Invalid choice! Please enter S, W, or G.')
    exit()

user=user_dict[user_input]
print(f"Computer chose {reversed_dict[computer]}\nYou chose {reversed_dict[user]}")

if computer==user:
    print("It's a draw")
else:
    if computer==-1 and user==1:
        print('You win!')
    elif computer==-1 and user==0:
        print('You lose!')
    elif computer==1 and user==-1:
        print('You lose!')
    elif computer==1 and user==0:
        print('You win!')
    elif computer==0 and user==1:
        print('You lose!')
    elif computer==0 and user==-1:
        print('You win!')
    else:
        print('Something went wrong')
