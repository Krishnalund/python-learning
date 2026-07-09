# Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.
maths=int(input('Enter here marks of maths: '))
english=int(input('Enter here marks of english: '))
science=int(input('Enter here marks of science: '))

average=(maths + english + science)/3
if(maths>=33 and english>=33 and science>=33 and average>=40):
    print('Student has passed')
else:
    print('Student has failed')

