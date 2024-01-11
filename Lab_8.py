import matplotlib.pyplot as plt
import numpy as np
from ctypes import * 
from NImage import ImageClass
import os

NImg = ImageClass()

current_dir = os.path.dirname(os.path.abspath(__file__))
array = NImg.LoadBMP( os.path.join(current_dir, "pattern.bmp"));

print(array.size)

plt.imshow(array, cmap='gray')     
plt.show()                   