# Create a Desktop Python Program to insert a Image as button in Window.

import tkinter as tk
from PIL import Image,ImageTk

img=Image.open(r"C:/Users/Asus/Pictures/Project Sem 3/project Revenue2024.png")

root=tk.Tk()
root.geometry("400x600")
label=tk.Label(root,text="My Window")
label.pack(padx=10,pady=20)

photo=ImageTk.PhotoImage(img)
button=tk.Button(root,image=photo)
button.pack(padx=12,pady=18)

root.mainloop()