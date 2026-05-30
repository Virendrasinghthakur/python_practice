# Write a Desktop Python program to get a string from user to change uppercase if user string is in lowercase.

import tkinter as tk

root=tk.Tk()
root.geometry("300x500")
tk.Label(root,text="My window").pack(padx=12,pady=24)
tk.Button(root,text="close window",command=root.destroy).pack(padx=8,pady=10)


tk.Label(root,text="enter string").pack()
num1=tk.Entry(root)
num1.pack()



rem=tk.Label(root)
rem.pack()
def cal():
    n=num1.get()
    if n.islower():
        n=n.upper()
    rem.config(text=n)

tk.Button(root,text="string ",command=cal).pack()



root.mainloop()