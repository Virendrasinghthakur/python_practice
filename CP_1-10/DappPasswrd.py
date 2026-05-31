# Write a Desktop Application in Python To Get A Password From The User That Should Have Alphanumeric and Special Characters

import tkinter as tk 

root=tk.Tk()
root.geometry("200x250")
tk.Label(root,text="Password").pack()
password=tk.Entry(root)
password.pack()

valid=tk.Label(root,text="")
valid.pack()

def check():
    u=password.get()
    if u.isalnum():
        valid.config(text="password is valid")
    else:
        valid.config(text="password is not valid")


tk.Button(root,text="submit",command=check).pack()
# print(password)

root.mainloop()