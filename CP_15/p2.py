# Write Desktop Application in Python To Get 2 Number From The User, Find Their Square, And Add Both Result, Finally Find Cube Of Result And Display To User.

import tkinter as tk

root = tk.Tk()
root.title("Square and Cube Calculator")
root.geometry("300x250")

tk.Label(root, text="Enter First Number").pack()
n1 = tk.Entry(root)
n1.pack()

tk.Label(root, text="Enter Second Number").pack()
n2 = tk.Entry(root)
n2.pack()

result = tk.Label(root, text="")
result.pack(pady=10)

def calculate():
    num1 = int(n1.get())
    num2 = int(n2.get())

    sq1 = num1 ** 2
    sq2 = num2 ** 2

    add = sq1 + sq2
    cube = add ** 3

    result.config(
        text=f"Square1 = {sq1}\n"
             f"Square2 = {sq2}\n"
             f"Addition = {add}\n"
             f"Cube = {cube}"
    )

tk.Button(root, text="Calculate", command=calculate).pack()

root.mainloop()