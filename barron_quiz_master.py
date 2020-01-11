import numpy as np
from database_reader import reader
import time
from shuffler_code import shuffle

# Required files are:
#
# 1. database_reader.py
# 2. shuffler_code.py
# 3. word_list.txt

txt_file = open("word_list.txt", "r")
word,meaning =reader(txt_file) # the func takes the file obj as its argument
txt_file.close()

# =================== INPUT ===================
print("**** If you are a new user run 'new_user.py' once ****")

choice = input("*** Enter whether you want \n 'Word to Meaning'/'Meaning to word' : 1/0 ")
amount1 = input("*** Enter the starting module: (1 to 79) ")
print("*** Enter the ending module: (", amount1," to 80) ", end="")
amount2 = input()
print("Note: This code will be let you revise your mistakes")


print("\n-------------Brace up for revision------------")
time.sleep(1)
start_time = time.clock()


amount1 = int(amount1)
amount2 = int(amount2)
amount1=(amount1-1)*10
amount2=(amount2-1)*10

rng = np.array(range(amount1,amount2)) #contains indexes of revision words
l = len(rng)
rng,original_data = shuffle(rng) # now rng contains permuted/jumbled indexes values

w2m = np.load("w2m.npy")
m2w = np.load("m2w.npy")

# =================== REVISION STARTS ===================

for i in range(l):
	k=rng[i]
	if choice == "1":
		print(i+1, ".", meaning[k], end="")
		input()
		print(i+1, ".",  word[k],"\n")
		a = input("??")
		if a !="":
			m2w[k] = m2w[k]+1
		elif m2w[k] >=1:
			m2w[k] = m2w[k] - 1


	else:
		print(i+1, ".", word[k], end="")
		input()
		print(i+1,".", meaning[k], "\n")
		a = input("??")
		if a !="":
			w2m[k] = w2m[k]+1
		elif w2m[k] >=1:
			w2m[k] = w2m[k] - 1

time.sleep(2)
print("-----------Nice work----------\n"
	  "You have Revised in:","{:.0f}".format((time.clock() - start_time)*1000), "Seconds")
print("\n Check your Happy-lil-Mistakes:")

for i in range(len(word)):
	if choice == 1:
		if w2m[i] >= 1:
			w2m[i]-=1
			print(word[i],"---",meaning[i])
	else:
		if m2w[i] >= 1:
			m2w[i] -= 1
			print(meaning[i],"---",word[i])

np.save("w2m.npy", w2m, allow_pickle=True, fix_imports=True)
np.save("m2w.npy", m2w, allow_pickle=True, fix_imports=True)
