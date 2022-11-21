#!/usr/bin/env python3

import random

if __name__ == '__main__':
    
    adverb_list = ["secretly", "wildly", "curiously", "rapidly", "miserably", "vacantly", "lazily"]
    adjective_list = ["charming", "dashing", "fluttering", "shaggy", "tricky", "fancy", "nutty"]
    noun_list = ["dog", "robot", "cat", "brother", "car", "football", "doortodoorsalesman"]
    
    random_word = (random.choice(adverb_list) + random.choice(adjective_list) + random.choice(noun_list))
