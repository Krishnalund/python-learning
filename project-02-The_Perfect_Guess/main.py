import random
random_num = random.randint(1,100)

user_guess = -1
count_guesses = 1
while(user_guess != random_num):
    user_guess = int(input('Guess the number: '))
    if user_guess > random_num:
        print('Lower number please')
        count_guesses +=1
    elif user_guess< random_num:
        print('Higher number please')
        count_guesses +=1

print(f"You have guessed the number {user_guess} correctly in {count_guesses} attempts")