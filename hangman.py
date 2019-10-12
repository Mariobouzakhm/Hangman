import filemanager, random

def createWordList(word):
    lst = list()
    for i in range len(word):
        lst.append('-')
    return lst

#Open a File Handle with the file containing all the words
file = open('wordlist.txt', 'r')

#list of all the words contained in the hangman dictionnary
lst = filemanager.readLines(file)

#Number of wrong choices the user can make while guessing a word
chances = 8

while True:
    choice = input('Enter \'new\' to start a new game or \'done\' to exit the game - ').lower()
    if choice == 'new':
        print('Starting a new game....')

        #Word the user need to guess
        word = lst[random.randint(0, len(lst) -1)].lower()

        #Choices that are still available for the user
        choices = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        #Holds the correct letters a user has guessed with the remaining ones as well
        wordchoices = createWordList(word)

        ##Holds the wrong guesses a user has made
        wrong = list()

        while True:
            letter = input('Enter a new letter - ').lower()
            while letter not in choices:
                print('Invalid Choice')
                print('Choices: ', choices)
                letter = input('Enter a new letter - ').lower()
            



    elif choice == 'done':
        print('Exiting the system...')
        break
    else:
        print('Wrong Argument')
