# Write A Desktop application in Python Program To Get A Number From User, The System Should Add Auto Increment To That Number. Half Of User Entered Number Should Be Incremented

import tkinter as tk

def calculate():
    num = int(entry.get())

    half = num / 2
    incremented_half = half + 1

    result.config(
        text=f"Number = {num}\nHalf = {half}\nIncremented Half = {incremented_half}"
    )

root = tk.Tk()
root.title("Auto Increment")
root.geometry("300x200")

tk.Label(root, text="Enter Number").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()