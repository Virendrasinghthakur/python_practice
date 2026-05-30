# Create a Desktop Python Program to insert a Button in Window. Window should be close when user click on the button.
import tkinter as tk

root=tk.Tk()
root.geometry("400x300")
label=tk.Label(root,text="New Window")
label.pack()


button=tk.Button(root,text="Close Window ",command=root.destroy)
button.pack(padx=10,pady=20)


root.mainloop()