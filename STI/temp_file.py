import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

print(os.getcwd())

np_file = np.load("/Users/you/Desktop/90006105.npy")
np_file = cv2.cvtColor(np_file, cv2.COLOR_BGR2RGB)
plt.imshow(np_file)
plt.show()