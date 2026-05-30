# Write a Desktop Python program to create a Checkboxes.

import tkinter as tk

root=tk.Tk()
root.geometry("300x500")
label=tk.Label(root,text="My window")
label.pack(padx=12,pady=24)
close=tk.Button(root,text="close window",command=root.destroy)
close.pack(padx=8,pady=10)

ck=tk.Checkbutton(root,text="this is to check")
ck.pack(padx=13,pady=16)

root.mainloop()