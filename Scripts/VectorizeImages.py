import numpy
from PIL import Image #run> pip install Pillow

'''
Converts images and corresponding emotion labels into vectors
'''
n = open("../Data/testFile.txt", "w")
n.write("testing yo")

#f = open("../Data/Cohn_Kanade_Facial_Emotions/cohn-kanade-images", 'r')
#c = f.read()


im = Image.open("../Data/Cohn_Kanade_Facial_Emotions/cohn-kanade-images/S005/001/S005_001_00000011.png") # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
print(pix[1,50])  # Get the RGBA Value of the a pixel of an image
#pix[x,y] = value  # Set the RGBA Value of the image (tuple)
#im.save('alive_parrot.png')  # Save the modified pixels as .png