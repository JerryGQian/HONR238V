from PIL import Image 
import glob
 '''
Converts all rgb colored images to grayscale
 '''

ipaths = glob.glob("../Data/CK/images/S[0-9]*/[0-9]*/*")

for ipath in ipaths:
	im = Image.open(ipath) # Can be many different formats.
	pix = im.load()

	if type(pix[10,10]) != int:
		print(ipath)
		im = im.convert('L') # convert image to grayscale
		im.save(ipath)