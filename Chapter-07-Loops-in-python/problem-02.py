# Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name[0].lower()=='s':
        print('Good Morning!',name)