# Write Desktop application in Python Program To Find Force Of A Man On A Object Which Have  Mass And Acceleration. Get Mass And Acceleration From User

import tkinter as tk

def calculate():
    m = float(mass.get())
    a = float(acceleration.get())

    force = m * a

    result.config(text=f"Force = {force} Newton")

root = tk.Tk()
root.title("Force Calculator")
root.geometry("300x200")

tk.Label(root, text="Mass (kg)").pack()
mass = tk.Entry(root)
mass.pack()

tk.Label(root, text="Acceleration (m/s²)").pack()
acceleration = tk.Entry(root)
acceleration.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()