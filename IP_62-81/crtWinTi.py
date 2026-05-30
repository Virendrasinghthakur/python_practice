# Create a Desktop Python program to create a window and provide title with icon.
import tkinter as tk 

root=tk.Tk()

root.geometry("200x400")
root.resizable(False,False)
root.title("My window")
root.iconbitmap("C:/Users/Asus/Pictures/Project Sem 3/Project Internship2 2024.png")
root.mainloop()