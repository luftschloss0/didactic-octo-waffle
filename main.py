import tkinter as tk
import math

# Define font settings
LARGE_FONT = ("Verdana", 14)
SMALL_FONT = ("Verdana", 10)

# Define calculator class
class Calculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set window properties
        self.title("Scientific Calculator")
        self.geometry("400x500")
        self.configure(bg="#303030")

        # Define input field
        self.entry = tk.Entry(self, width=30, font=LARGE_FONT, bd=0, justify="right", bg="#383838", fg="white")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define number buttons
        self.btn_1 = tk.Button(self, text="1", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(1))
        self.btn_2 = tk.Button(self, text="2", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(2))
        self.btn_3 = tk.Button(self, text="3", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(3))
        self.btn_4 = tk.Button(self, text="4", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(4))
        self.btn_5 = tk.Button(self, text="5", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(5))
        self.btn_6 = tk.Button(self, text="6", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(6))
        self.btn_7 = tk.Button(self, text="7", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(7))
        self.btn_8 = tk.Button(self, text="8", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(8))
        self.btn_9 = tk.Button(self, text="9", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(9))
        self.btn_0 = tk.Button(self, text="0", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click(0))
        self.btn_dot = tk.Button(self, text=".", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click("."))

        # Define operator buttons
        self.btn_add = tk.Button(self, text="+", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click("+"))
        self.btn_subtract = tk.Button(self, text="-", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command=lambda: self.btn_click("-"))
        self.btn_multiply = tk.Button(self, text="*", font=LARGE_FONT, bd=0, bg="#303030", fg="white", command
