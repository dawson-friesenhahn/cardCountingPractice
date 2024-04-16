import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    frm= ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text= "Hello, World!").grid(column=0, row= 0)
    root.mainloop()

if __name__ == "__main__":
    main()