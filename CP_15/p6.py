# Write A Desktop application in  Python Program To Find Acceleration Of An Object Having Velocity v in t Time.

import tkinter as tk

def calculate():
    v = float(velocity.get())
    t = float(time.get())

    a = v / t

    result.config(text=f"Acceleration = {a} m/s²")

root = tk.Tk()
root.title("Acceleration Calculator")
root.geometry("300x200")

tk.Label(root, text="Velocity (m/s)").pack()
velocity = tk.Entry(root)
velocity.pack()

tk.Label(root, text="Time (s)").pack()
time = tk.Entry(root)
time.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()