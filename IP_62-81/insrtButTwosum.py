# Create a Desktop Python Program to insert a Button in Window. When click on the button, it take two number from user to add both number in console.


import tkinter as tk 

root=tk.Tk()

root.geometry("200x400")
root.resizable(False,False)
root.title("My window")
# root.iconbitmap("C:/Users/Asus/Pictures/Project Sem 3/Project Internship2 2024.png")
def func():
    a,b=map(int,input("enter two numer:").split())
    print(a+b)
tk.Button(root,text="click me",command=func).pack()
root.mainloop()