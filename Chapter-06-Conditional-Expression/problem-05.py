# Write a program which finds out whether a given name is present in a list or not.
name_list=['krishna', 'nancy','henry','john']
name=input('Enter name: ').lower()
if name in name_list:
    print(name,'is present in the list')
else:
    print(name,'is not present in the list')