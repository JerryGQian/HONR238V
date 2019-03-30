import numpy as np
from PIL import Image #run> pip install Pillow
import glob

'''
Converts images and corresponding emotion labels into vectors
'''

#ipaths = glob.glob("../Data/CK/images/S[0-9]*/[0-9]*/*")
epaths = glob.glob("../Data/CK/emotions/S129/[0-9]*/*")
#print(paths)

for epath in epaths:
	
	ipath = epath[0:11] + "images" + epath[19:46] + ".png"
	print(epath)
	print(ipath)

	im = Image.open(ipath) # Can be many different formats.
	pix = im.load()

	e = open(epath, "r")
	emotion = e.read().strip()[0]

	#copies pixel values into array
	v = np.empty(shape=(im.size[0] * im.size[1] + 1, 1)) # +1 to fit emotion label at end
	for x in range(0, im.size[0]):
		for y in range(0, im.size[1]):
			print(type(pix[x,y]), pix[x,y])
			if type(pix[x,y]) == "int":
				v[x*im.size[1] + y + 1] = pix[x,y]

	v[0] = emotion

	#np.savetxt("../Data/CK/vectorstest/" + epath[20:24] + "_" + epath[25:28] + ".txt", v, fmt='%d')