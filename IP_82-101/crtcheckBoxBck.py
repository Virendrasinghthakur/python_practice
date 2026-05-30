# Write a Desktop Python program to create a Checkboxes to change background color, cursor, font, fg, border etc.


import tkinter as tk

root=tk.Tk()
root.geometry("300x500")
label=tk.Label(root,text="My window")
label.pack(padx=12,pady=24)
close=tk.Button(root,text="close window",command=root.destroy)
close.pack(padx=8,pady=10)

bg_var=tk.IntVar()
fg_var=tk.IntVar()
font_var=tk.IntVar()
cursor_var=tk.IntVar()
border_var=tk.IntVar()

def update_style():
    if bg_var.get():
        label.config(bg="yellow")
    else:
        label.config(bg=root.cget("bg"))

    if fg_var.get():
        label.config(fg="red")
    else:
        label.config(fg="black")
    
    if font_var.get():
        label.config(font=("Arial",14,"bold"))
    else:
        label.config(font=("Arial",14))
    
    if cursor_var.get():
        label.config(cursor="hand2")
    else:
        label.config(cursor="arrow")
    
    if border_var.get():
        label.config(relief="raised",bd=5)
    else:
        label.config(relief="flat",bd=0)

tk.Checkbutton(root,text="change bg color",variable=fg_var,command=update_style).pack(anchor="w")
tk.Checkbutton(root,text="change fg color",variable=bg_var,command=update_style).pack(anchor="w")
tk.Checkbutton(root,text="change font",variable=font_var,command=update_style).pack(anchor="w")
tk.Checkbutton(root,text="change cursor",variable=cursor_var,command=update_style).pack(anchor="w")
tk.Checkbutton(root,text="change border",variable=border_var,command=update_style).pack(anchor="w")



root.mainloop()