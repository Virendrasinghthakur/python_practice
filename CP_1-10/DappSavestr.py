# Write A Desktop Application To Get A String From User To Save In Text File.

import tkinter as tk

root=tk.Tk()
root.geometry("200x250")

tk.Label(root,text="enter string").pack()
sent=tk.Entry(root)
sent.pack()

result=tk.Label(root)
result.pack()
def save():
    s=sent.get()
    with open("t1.txt",'w') as f:
        f.write(s)
    result.config(text="data saved succesfuly")
b=tk.Button(root,text="submit",command=save)
b.pack()

root.mainloop()