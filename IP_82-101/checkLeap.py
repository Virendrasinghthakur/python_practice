# Write a Desktop Python program to get a year from user to check it is leap year or not.


import tkinter as tk

root=tk.Tk()
root.geometry("300x500")
tk.Label(root,text="My window").pack(padx=12,pady=24)
tk.Button(root,text="close window",command=root.destroy).pack(padx=8,pady=10)


tk.Label(root,text="char").pack()
num1=tk.Entry(root)
num1.pack()



rem=tk.Label(root)
rem.pack()
def cal():
    n=int(num1.get())
    if n%4==0 and n%400==0 :
        n="Its a leap year"
    else:
        n="not a leap year"
    rem.config(text=n)

tk.Button(root,text="check",command=cal).pack()


root.mainloop()

