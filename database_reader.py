
txt_file = open("word_list.txt", "r")

word = ["",""]
word.clear()
meaning = ["",""]
meaning.clear()

trig = 1 
wrd = ""

txt=txt_file.read()
for c in txt:
	if c!= "~" and c!= "\n":
		wrd = wrd + c
	elif trig == 1 and c== "~":
		word.append(wrd)
		wrd = ""
		trig = - trig
	elif trig == -1 and c== "~":
		meaning.append(wrd)
		wrd = ""
		trig = - trig
print("\n".join(word))
print("\n".join(meaning))

print(len(word))
print(len(meaning))

txt_file.close() 

