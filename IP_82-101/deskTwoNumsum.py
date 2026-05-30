# Write a Desktop Python program to get two number from user to display their reminder after division.


import tkinter as tk

root=tk.Tk()
root.geometry("300x500")
tk.Label(root,text="My window").pack(padx=12,pady=24)
tk.Button(root,text="close window",command=root.destroy).pack(padx=8,pady=10)


tk.Label(root,text="first number").pack()
num1=tk.Entry(root)
num1.pack()


tk.Label(root,text="second number").pack()
num2=tk.Entry(root)
num2.pack()

rem=tk.Label(root)
rem.pack()
def cal():
    n=int(num1.get())/int(num2.get())
    rem.config(text=n)

tk.Button(root,text="cal cube",command=cal).pack()



root.mainloop()