# Create a Desktop Python Program to insert Image in Window.
import tkinter as tk

root=tk.Tk()
root.geometry("300x500")
label=tk.Label(root,text="My window")
label.pack(padx=12,pady=24)
close=tk.Button(root,text="close window",command=root.destroy)
close.pack(padx=8,pady=10)

from PIL import Image,ImageTk

img=Image.open(r"C:/Users/Asus/Pictures/Project Sem 3/Project Internship2 2024.png")
img=img.resize((120,140))
photo=ImageTk.PhotoImage(img)

button=tk.Label(root,image=photo,text="IMAGE",compound="bottom")
button.pack(padx=10,pady=12)

root.mainloop()