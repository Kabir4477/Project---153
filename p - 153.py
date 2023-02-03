# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:56:42 2023

@author: drsau
"""

from tkinter import *
import random

root = Tk()
root.title("Password Generator")
root.geometry("400x400")

enter_password = Entry(root)

label1 = Label(root)

label = Label(root)

array_3d = [[["A","B","C","D","E","F","G","H"],["King","Queen"], ["#","@","!","$","^","%","*"]]]
print(array_3d[0][2][3])

def new_password():
    random_no_1 = random.randint(0,7)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,6)
    
    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    label["text"] =  "Generated password : " +  letter1 + "" + letter2 + "" + letter3
    label1["text"] = "Guessed password : " + enter_password.get()

btn = Button(root,text = "New Password", command = new_password)
btn.place(relx=0.5,rely=0.6,anchor = CENTER)

enter_password.place(relx = 0.5,rely = 0.4 , anchor = CENTER)
label1.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

label.place(relx = 0.5,rely = 0.7 , anchor = CENTER)

root.mainloop()