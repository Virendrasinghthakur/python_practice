# Create a Desktop Python program to create a window and Insert some text to window



from tkinter import *

root=Tk()

root.title("My first Window")

label=Label(root,text="Hello This is veer singh")
label.pack()

root.geometry("400x300")

root.mainloop()