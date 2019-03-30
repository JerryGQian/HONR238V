import numpy as np
from PIL import Image #run> pip install Pillow

'''
Converts images and corresponding emotion labels into vectors
'''
#n = open("../Data/testFile.txt", "w")
#n.write("testing yo")

im = Image.open("../Data/Cohn_Kanade_Facial_Emotions/cohn-kanade-images/S005/001/S005_001_00000011.png") # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
print(pix[320,30])  # Get the RGBA Value of the a pixel of an image
#pix[x,y] = value  # Set the RGBA Value of the image (tuple)
#im.save('alive_parrot.png')  # Save the modified pixels as .png

e = open("../Data/Cohn_Kanade_Facial_Emotions/Emotion/S005/001/S005_001_00000011_emotion.txt", "r")
emotion = e.read().strip()[0]
print(emotion)

a = np.array([1,2,3,4])
np.savetxt('test1.txt', a, fmt='%d')