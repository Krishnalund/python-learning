# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. 
# Place these files in a folder for a 13-year-old.

for i in range(2,21):
    filename = f"Chapter-09-File-IO/Tables/table_{i}.txt"
    with open(filename,'w') as file:
        file.write(f"Multiplication Table of {i}\n")
        file.write('-'*25 + '\n')
        for j in range(1,11):
            file.write(f"{i} * {j} = {i*j}\n")