from tkinter import *
import math

def fun(event):
    global value
    num1 = event.widget.cget("text")
    print(num1)
    if num1 == "=":
        if value.get().isdigit():
            value1 = int(value.get())
        else:
            value1 = eval(screen.get())    
        value.set(value1)    
    elif num1 == "C":
        value.set("")
        screen.update()
    elif num1 == "sin":
        value.set(math.sin(float(screen.get())))
    elif num1 == "cos":
        value.set(math.cos(float(screen.get())))
    elif num1 == "tan":
        value.set(math.tan(float(screen.get())))
    else:
        value.set(value.get()+num1)
        screen.update()

kk_root = Tk()
kk_root.geometry("420x500")
kk_root.title("Calculator")
kk_root.resizable(False, False)  # Disables resizing

value = StringVar()
value.set("")
screen = Entry(kk_root, textvar=value, font=("Arial", 20), justify="right")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, sticky="ew")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "sin", "cos", "tan"
]

row = 1
col = 0

for button in buttons:
    if button in ["=", "C", "+", "-", "*", "/"]:
        btn = Button(kk_root, text=button, padx=30, pady=20, font=("Arial", 14, "bold"),bg="orange", fg="white")
    elif button in ["sin", "cos", "tan"]:
        btn = Button(kk_root, text=button, padx=30, pady=20, font=("Arial", 12, "bold"))
    else:
        btn = Button(kk_root, text=button, padx=30, pady=20, font=("Arial", 14, "bold"))
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", fun)
    col += 1
    if col > 3:
        col = 0
        row += 1

kk_root.mainloop()
