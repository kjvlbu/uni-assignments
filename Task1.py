#!/usr/bin/env python3

import random

if __name__ == '__main__':

    print("Password Generator\n==================")

    proceed = False
    while proceed == False:
        try:
            passwords_required = int(input("Please enter your required number of passwords. "))
        except:
            print("Enter a valid number to proceed.")
            continue
        if passwords_required < 1 or passwords_required > 24:
            print("Please enter a number between 1 and 24")
        else:
            proceed = True


    ADVERB_LIST = ["secretly", "wildly", "curiously", "rapidly", "miserably", "vacantly", "lazily"]
    ADJECTIVE_LIST = ["charming", "dashing", "fluttering", "shaggy", "tricky", "fancy", "nutty"]
    NOUN_LIST = ["dog", "robot", "cat", "brother", "car", "football", "doortodoorsalesman"]

    count = 0
    while passwords_required > 0:

        first_word = random.choice(ADVERB_LIST)
        second_word = random.choice(ADJECTIVE_LIST)
        third_word = random.choice(NOUN_LIST)

        user_generated_passwords = (first_word + second_word + third_word)
        count += 1
        print(count, "->", user_generated_passwords)
        passwords_required -= 1
