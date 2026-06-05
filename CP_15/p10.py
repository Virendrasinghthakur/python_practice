# Write Desktop application in  A Python Program To Add Number From List That Are Greater Than 5 And Less Than 10

import tkinter as tk

def calculate():
    nums = list(map(int, entry.get().split()))

    total = sum(num for num in nums if 5 < num < 10)

    result.config(text=f"Sum = {total}")

root = tk.Tk()
root.title("Sum Calculator")
root.geometry("300x200")

tk.Label(root, text="Enter numbers separated by space").pack()

entry = tk.Entry(root, width=30)
entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()