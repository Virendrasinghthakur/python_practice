# Create a Desktop Python Program to insert a Button in Window. When click on that button a function should run

import tkinter as tk 

root=tk.Tk()

root.geometry("200x400")
root.resizable(False,False)
root.title("My window")
# root.iconbitmap("C:/Users/Asus/Pictures/Project Sem 3/Project Internship2 2024.png")
def func():
    print("hii")

tk.Button(root,text="click me",command=func).pack()
root.mainloop()