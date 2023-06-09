"""Hangman program"""
import random
import requests

LEVELS = [" +----+\n |    |\n O    |\n      |\n      |\n      |\n=======\n",
          " +----+\n |    |\n O    |\n/     |\n      |\n      |\n=======\n",
          " +----+\n |    |\n O    |\n/|    |\n      |\n      |\n=======\n",
          " +----+\n |    |\n O    |\n/|\\   |\n      |\n      |\n=======\n",
          " +----+\n |    |\n O    |\n/|\\   |\n/     |\n      |\n=======\n",
          " +----+\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n=======\n"]

def get_list_of_words():
    """
    Get list of words
    """
    response = requests.get(
        'https://www.mit.edu/~ecprice/wordlist.10000',
        timeout=10
    )
    string_of_words = response.content.decode('utf-8')
    list_of_words = string_of_words.splitlines()
    return list_of_words

def generate_word():
    """
    generate word
    """
    words= get_list_of_words()
    return random.choice(words)

def generate_output(word_length):
    """
    Generate output
    """
    output=[]
    for _ in range(word_length):
        output+="_"
    return output

def start():
    """
    start game
    """
    word = generate_word()
    word_length=len(word)
    output=generate_output(word_length)
    game_over=False
    level = 0
    while not game_over:
        guess=input("Guess a letter: ").lower()
        flag = False
        for index in range(word_length):
            letter = word[index]
            if letter == guess:
                flag = True
                output[index] = letter
        print(output)
        if not flag:
            print(LEVELS[level])
            level += 1
            if level==6:
                print("You Killed Him!!!")
                print(word)
                game_over = True
        if "_" not in output:
            print("You Saved Him!!!")
            game_over = True
if __name__ == "__main__":
    start()
