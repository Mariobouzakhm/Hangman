import os, filemanager
os.chdir('C:\\Users\\K\\PythonScripts\\Coursera\\Extra\\Hangman')

file = open('wordlist.txt', 'r')
words = wordlist.readLines(file)
while True:
    usage = '''
- Usage: 1- list: List all the words already added into the dictionary
         2- add: Add a word to the dictionary
         3- remove: Remove a word from the dictionary
         4- done: Exit editing the dictionary'''
    print(usage)
    user = input('Enter - ')
    if user == 'list':
        print('Word List: ')
        for word in words:
            print(word, end=' \n')
    elif user == 'add':
        word = input('Enter the word you want to add - ')
        if word.lower() in words:
            print('Word is already in the dictionary')
        else:
            words.append(word.lower())
            print('Word Added.')
    elif user == 'remove':
        word = input('Enter the word you want to remove - ')
        if word.lower() not in words:
            print('Word is not in the dictionary')
        else:
            words.remove(word.lower())
            print('Word Removed.')
    elif user == 'done':
        print('Exitting editer...')
        break
    else:
        print(usage)
file.close()

file = open('wordlist.txt', 'w')
for word in words:
    file.write(word.lower()+'\n')
file.close()
