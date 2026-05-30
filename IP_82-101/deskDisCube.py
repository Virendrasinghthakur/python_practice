# Write a Desktop Python program to get a number from user to display its cube.

import tkinter as tk

root=tk.Tk()
root.geometry("300x500")
tk.Label(root,text="My window").pack(padx=12,pady=24)
tk.Button(root,text="close window",command=root.destroy).pack(padx=8,pady=10)


tk.Label(root,text="enter number").pack()
num=tk.Entry(root)
num.pack()

cube=tk.Label(root)
cube.pack()
def cal_root():
    n=int(num.get())
    n=n*n*n
    cube.config(text=n)

tk.Button(root,text="cal cube",command=cal_root).pack()



root.mainloop()