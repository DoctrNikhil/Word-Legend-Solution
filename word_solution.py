
import json
import itertools
import os

try:
    all_possible_words = {}
    with open("words_dictionary.json") as file:
        print("Loading Please wait")
        # this contains all valid english words
        all_possible_words = json.load(file)

        #print("OOps Error occured possibly 'words_dictionary.json' is not prsent in this directroy,\nGet this file from my Github project")

        usercharacters = input("Give me characters less than length 11, don't give space\n")

        # possible_words from user characters
        for i in range(1,len(usercharacters)+1):
            possible_words_of_len_i = [''.join(p) for p in itertools.permutations(usercharacters,i)]
            for words_made in possible_words_of_len_i:
                if words_made in all_possible_words.keys():
                    print(words_made)
        
        file.close()
except:
    scriptPath = os.path.realpath(__file__)
    print("Please include words_dictionary.json file in this directry ",scriptPath)




