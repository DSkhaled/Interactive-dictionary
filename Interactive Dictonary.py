# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:08:17 2019

@author: K6433702
"""
# Import libraries
import json
from difflib import get_close_matches
import os

# Loading data
data = json.load(open("data.json","r"))

# Translation function
def translate(w):
    w = w.lower()
    if w in data.keys():
        return(data[w])
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return(data[w.title()])
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(w,data.keys())[0])
        if str(yn) == 'Y':
            return(data[get_close_matches(w,data.keys())[0]])
        elif str(yn) == 'N':
            return("The word does not exists, Please double check it!!")
        else:
            raise ValueError("We didn't understand your entry.")
    else:
        return("The word does not exists, Please double check it!!")
# Main
if __name__ == "__main__":
    word  = input("Enter the word you are looking for: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    os.system("pause")
