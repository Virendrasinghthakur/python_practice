# Write a Desktop Python program to get a string from user to reverse.



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
    n=num1.get()
    n=n[::-1]
    rem.config(text=n)

tk.Button(root,text="check",command=cal).pack()


root.mainloop()

