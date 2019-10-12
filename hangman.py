import filemanager, random
#Open a File Handle with the file containing all the words
file = open('wordlist.txt', 'r')

#list of all the words contained in the hangman dictionnary
lst = filemanager.readLines(file)

while True:
    choice = input('Enter \'new\' to start a new game or \'done\' to exit the game - ').lower()
    if choice == 'new':
        print('Starting a new game....')
        word = lst[random.randint(0, len(lst) -1)]
    elif choice == 'done':
        print('Exiting the system...')
        break
    else:
        print('Wrong Argument')
