from database_reader import reader
import numpy as np
txt_file = open("word_list.txt", "r")
word,meaning =reader(txt_file) # the func takes the file obj as its argument
txt_file.close()

w2m = np.zeros(len(word))     # word2meaning memory strength chart
m2w = np.zeros(len(meaning))  # meaning2word memory strength chart

np.save("w2m.npy", w2m, allow_pickle=True, fix_imports=True)
np.save("m2w.npy", m2w, allow_pickle=True, fix_imports=True)

#matrices are cleaned for a new_user