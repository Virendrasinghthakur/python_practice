# Create a Desktop Python Program to insert a Button in Window. A message box should be display when user click on the button.

import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message","Button Clicked")
root=tk.Tk()

root.geometry("400x300")
label=tk.Label(root,text="My Window")
label.pack(padx=5,pady=10)
close=tk.Button(root,text="close window",command=root.destroy)
close.pack(padx=8,pady=12)
button=tk.Button(root,text="See Message",command=show_message)
button.pack(padx=10,pady=20)

# print(message)

root.mainloop()