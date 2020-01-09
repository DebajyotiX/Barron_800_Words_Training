import numpy as np
import tkinter
from database_reader import reader
import time



import random
# from scrambler import scrambled
# def scrambled(orig):
#     dest = orig[:]
#     random.shuffle(dest)
#     return dest



txt_file = open("word_list.txt", "r")
word,meaning =reader(txt_file) #file obj as argument
txt_file.close() 

# Enter Recap Style:
# Meaning to Word; enter choice = 1
# Word to Meaning; enter choice = 2
choice = 1

# Starting module no. in range[1-79],amount1=??
# Starting module no. in range[amount1-79],amount2=??
amount1 = 3
amount2 = 12

amount1=(amount1-1)*10
amount2=(amount2-1)*10
rng = range(amount1,amount2)
print(rng)
# random.shuffle(rng)
time_1 = 2
time_2 = 1

if choice =="1":
	for i in rng:
		print(i+1,".",,": ",meaning[i])
		time.sleep(time_1)
		print("It was ", word[i],"\n")
		time.sleep(time_2)

	print("Nice work N*gg@!")
else:
	for i in rng:
		print("Guess: ",word[i])
		time.sleep(time_1)
		print("It was ", meaning[i],"\n")
		time.sleep(time_2)		
	print("Nice work N*gg@!")



	