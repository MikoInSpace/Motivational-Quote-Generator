import random
import os
import time

def pick_random_quote(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = file.read().splitlines()

    if quotes:
        return random.choice(quotes)
    else:
        return "No quotes found in the file."

while True:
    print("Welcome to the motivational quote generator!")
    print("Select an option.")
    print("1. Get a random motivational quote.")
    print("2. Exit.")

    option = input("Option: ")

    if option == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        script_directory = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_directory, "quotes.txt")
        random_quote = pick_random_quote(filename)
        print("Random motivational quote:", random_quote)
        print(" ")
    elif option == "2":
        print("Exiting...")
        time.sleep(1)
        break
