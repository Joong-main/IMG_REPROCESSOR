import tkinter
import numpy as np
from imageio import imread, imwrite
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import os
## GUI

root = tkinter.Tk()
root.title("IMG ReProcessor")
root.geometry("540x300+100+100")
root.resizable(False, False)


"""def ask():
	root.file = filedialog.askopenfile(
	initialdir='path',
	title='select file',
	filetypes=(('jpg files','*.jpg'),('jpeg files','*.jpeg'),('png files', '*.png'),
		('all files', '*.*')))


	txt.configure(text="FILE directory: " + root.file.name)
	return root.file.name
"""
lbl = tkinter.Label(root, text="Press this button >>")
lbl.grid(row=0,column=0)

txt = tkinter.Label(root, text=" ")
txt.grid(row=3,column=0)

condition_lbl = tkinter.Label(root, text= "Condition:   Ready")
condition_lbl.grid(row=3,column=0)

"""btn = tkinter.Button(root,text="Select FILE",command=processing)
btn.grid(row=0,column=1)"""

## image processing Area


def processing():
	condition_lbl = tkinter.Label(root, text="Condition:   WORKING")
	condition_lbl.grid(row=3, column=0)

	root.file = filedialog.askopenfile(
	initialdir='path',
	title='select file',
	filetypes=(('jpg files','*.jpg'),('jpeg files','*.jpeg'),('png files', '*.png'),
		('all files', '*.*')))

	this=os.path.basename(root.file.name)
	print(this)

	img = cv2.imread(this)
	arr=img * np.array([0.1,0.2,0.5])
	arr2=(255*arr/arr.max()).astype(np.uint8)
	imwrite(this+'night_ver.png',arr2)
	img2=cv2.imread(this+'night_ver.png')
	gamma=2

	gamma_img=np.array(255*(img2/255)**gamma,dtype='uint8')

	cv2.imwrite(this+'night_fin.png',gamma_img)
	print("Well Done!")

	condition_lbl = tkinter.Label(root, text="Condition:   Ready ")
	condition_lbl.grid(row=3, column=0)


btn = tkinter.Button(root,text="Select FILE",command=processing)
btn.grid(row=0,column=1)
root.mainloop()
