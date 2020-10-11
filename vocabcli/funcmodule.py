import json
import os

def challenge(words_list):
    path_to_here = os.path.dirname(os.path.abspath(__file__))
    with open(path_to_here + "/wordlists/"+words_list+".json", "r") as read_file:
        #print("Converting JSON encoded data into Python dictionary")
        word_list = json.load(read_file)

        #print("Decoded JSON Data From File")
        for key, value in word_list.items():
            test_word(key, value)
            next = input("Pressez Entrée pour continuer")

def test_word(key,value):
    answer = input(key+":  ")
    if answer == value:
        print('\U0001f604' + " " + bcolors.OKGREEN + "Bonne réponse !" + bcolors.ENDC)
    else:
        print('\U0001f641' + " " + bcolors.FAIL + "Mauvaise réponse :( Correction : " + value + bcolors.ENDC)
    return answer == value

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'