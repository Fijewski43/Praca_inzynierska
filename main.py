import cv2
import matplotlib.pyplot as plt
import numpy as np

#poprawne działanie
no_current = cv2.imread("venv\Zdjecia pomiarowe\\NoCurrent\\no-current-load\\1657011327886739015.png")
current_2A = cv2.imread("venv\Zdjecia pomiarowe\Current\current-load-6A\\1657011929225074450.png")
current_4A = cv2.imread("venv\Zdjecia pomiarowe\Current\current-load-4A\\1657011765501184326.png")
current_6A = cv2.imread("venv\Zdjecia pomiarowe\Current\current-load-6A\\1657011929225074450.png")

no_current = cv2.normalize(no_current,  0, None, 255, cv2.NORM_MINMAX)
current_2A = cv2.normalize(current_2A,  None, 0, 255, cv2.NORM_MINMAX)
current_4A = cv2.normalize(current_4A,  None, 0, 255, cv2.NORM_MINMAX)
current_6A = cv2.normalize(current_6A,  None, 0, 255, cv2.NORM_MINMAX)

f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(no_current)
axarr[0,0].set_title("current")
axarr[0,1].imshow(current_2A)
axarr[0,1].set_title("2A")
axarr[1,0].imshow(current_4A)
axarr[1,0].set_title("4A")
axarr[1,1].imshow(current_6A)
axarr[1,1].set_title("6A")
f.suptitle('Correct work')
plt.show()

misaligment_6A = cv2.imread("venv\Zdjecia pomiarowe\Misalignment\misalignment-current-load-6A-2\\1657013019105176859.png")
rotor_6A = cv2.imread("venv\Zdjecia pomiarowe\Rotor\\rotor-6-current-load-6A\\1657021566314963205.png")
misaligment_no_load = cv2.imread("venv\Zdjecia pomiarowe\Misalignment\misalignment-no-current-load\\1657012168831039560.png")
misaligment_2A = cv2.imread("venv\Zdjecia pomiarowe\Misalignment\misalignment-current-load-2A\\1657012253888714272.png")
misalignment_4A = cv2.imread("venv\Zdjecia pomiarowe\Misalignment\misalignment-current-load-4A-2\\1657012924095611905.png")


misaligment_6A = cv2.normalize(misaligment_6A,  None, 0, 255, cv2.NORM_MINMAX)
misaligment_2A = cv2.normalize(misaligment_2A,  None, 0, 255, cv2.NORM_MINMAX)
misalignment_4A = cv2.normalize(misalignment_4A,  None, 0, 255, cv2.NORM_MINMAX)
misaligment_no_load = cv2.normalize(misaligment_no_load,  None, 0, 255, cv2.NORM_MINMAX)
rotor_6A = cv2.normalize(rotor_6A,  None, 0, 255, cv2.NORM_MINMAX)

#cv2.imshow('current_2A' , current_2A)
#cv2.imshow('rotor_6A', rotor_6A)
#cv2.imshow('no-current', no_current)




cv2.waitKey(0)
