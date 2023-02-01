import cv2
import numpy as np
from matplotlib import pyplot as plt


import matlab.engine


eng = matlab.engine.start_matlab()
eng.cd('D:/MyCode/Python/Skin_Barrier/Python-Image-feature-extraction-master',nargout=0)
t = eng.gclm("../My_image/group_tape_stripping_numbers/3_20_90/3_0_20_90.jpg")
print(t)



cv2.waitKey(0)
cv2.destroyAllWindows()


