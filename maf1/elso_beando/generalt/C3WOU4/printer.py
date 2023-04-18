from PIL import Image, ImageOps
import numpy as np
# Creating the 144 X 144 NumPy Array with random values



def qr_print(arr):
    arr=np.array(arr)
    arr=(1-arr)*255
    arr = arr.astype('uint8')
   
    scale=10 # Méret
    narr=np.array([ [val for val in a for _ in range(scale)] for a in arr for t in range(scale)])
   
    # Converting the numpy array into image
    img  = Image.fromarray(narr)
    img_with_border = ImageOps.expand(img,border=1,fill='grey')
    display(img_with_border)