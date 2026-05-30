# Create a Desktop Python Program to insert Image in Window when a user click on button.

import tkinter as tk

root=tk.Tk()
root.geometry("300x500")
tk.Label(root,text="My window").pack(padx=12,pady=24)
tk.Button(root,text="close window",command=root.destroy).pack(padx=8,pady=10)


from PIL import Image,ImageTk

image_label = tk.Label(root)
image_label.pack(padx=22, pady=36)

def show_img():
    image_label.config(image=photo)

img=Image.open(r"C:/Users/Asus/Pictures/Project Sem 3/Project Internship2 2024.png").resize((120,140))
photo=ImageTk.PhotoImage(img)

show=tk.Button(root,text="show image",command=show_img).pack(pady=15)
root.mainloop()