import os
os.chdir('C:\\Users\\K\\PythonScripts\\Coursera\\Extra\\Hangman')

def readLines(file):
    words = list()
    for line in file:
        words.append(line.strip())
    return words
