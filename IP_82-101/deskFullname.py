# Write a Desktop Python program to get first and last name from user to display full name to user.
import tkinter as tk

root=tk.Tk()
root.geometry("300x500")
tk.Label(root,text="My window").pack(padx=12,pady=24)
tk.Button(root,text="close window",command=root.destroy).pack(padx=8,pady=10)



tk.Label(root,text="First Name").pack()
first=tk.Entry(root)
first.pack(padx=10,pady=12)

tk.Label(root,text="last Name").pack()
last=tk.Entry(root)
last.pack(padx=12,pady=12)

full_name=tk.Label(root,text="")
full_name.pack()


def show_input():
    full=first.get()+" "+last.get()
    full_name.config(text="full name : "+full)

tk.Button(root,text="submit",command=show_input).pack(padx=14,pady=12)


root.mainloop()