# Create a Desktop Python program to create a window and set geometry that should be fixed. And Disable resize functionality

import tkinter as tk 

root=tk.Tk()

root.geometry("200x400")
root.resizable(False,False)

root.mainloop()