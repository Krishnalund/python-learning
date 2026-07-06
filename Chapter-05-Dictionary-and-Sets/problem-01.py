# Write a program to create a dictionary of English words with values as their meaning.
# Provide user with an option to look it up!
my_dic={
    "Apple":"A fruit",
    "Candy Crush":"A game",
    "Computer":"An electronic device"
}
word=input('Enter a word from the dictionary: ')
check_word=my_dic.get(word, "Word not found in the dictionary.")
print(check_word)
