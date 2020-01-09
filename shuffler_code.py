import numpy as np
from random import seed
from random import random
seed(1)
def shuffle(data):
	for j in range(50):
		for i in range(len(data-1)):
			if random()>=0.5:
				a = data[i]
				data[i] = data[i+1]
				data[i+1] = a
			

