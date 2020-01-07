import numpy as np
import tkinter
from database_reader import reader
# from permutator_gui import permutator

txt_file = open("word_list.txt", "r")
word,meaning =reader(txt_file) #file obj as argument
txt_file.close() 
# print(word,end="\n")
# print(meaning,end="\n")

# print(len(word))
# print(len(meaning))
print("Enter Recap Style")
print("Meaning to Word; enter:'['")
choice = raw_input("Word to Meaning; enter:']' \n ") 
if choice =="[":
	