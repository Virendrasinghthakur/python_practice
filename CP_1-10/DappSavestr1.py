# Write A Desktop Application To Get A String From User. Display Required String Sub Part Using Slicing Method.



import tkinter as tk

root=tk.Tk()
root.geometry("200x250")

tk.Label(root,text="enter string").pack()
sent=tk.Entry(root)
sent.pack()

result=tk.Label(root)
result.pack()
def slice():
    s=sent.get()
    sliced=s[1:5]
    result.config(text="Substring :" + sliced)
b=tk.Button(root,text="submit",command=slice)
b.pack()

root.mainloop()