# The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
# Hi-score. You need to write a program to update the Hi-score whenever the game()
# function breaks the Hi-score.
def game():
    return 85
score = game()
filename='Hi-score.txt'
with open(filename,'r') as file:
    high_score = file.read()
if not high_score or score > int(high_score):
    with open(filename,'w') as file:
        file.write(str(score))
else:
    print("High score remains unchanged.")

