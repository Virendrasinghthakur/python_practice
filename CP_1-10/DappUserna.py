# Write a Desktop Application in Python To Get A Username From The User That Should Have Alphanumeric Characters
import tkinter as tk 

root=tk.Tk()
root.geometry("200x250")
tk.Label(root,text="username").pack()
user=tk.Entry(root)
user.pack()

valid=tk.Label(root,text="")
valid.pack()

def check():
    u=user.get()
    if u.isalnum():
        valid.config(text="user is valid")
    else:
        valid.config(text="user is not valid")


tk.Button(root,text="submit",command=check).pack()
# print(user)

root.mainloop()