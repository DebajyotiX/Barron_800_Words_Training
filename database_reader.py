
def reader(txt_file):  #file obj as argument
	word = []
	meaning = []
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
	return word,meaning
