import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.geometry("340x420")
        root.title("Calculator")
        root.resizable(False, False)  # Disables resizing
        root.configure(bg="lightblue")  # Set background color to light blue
        
        self.value = tk.StringVar()
        self.value.set("")
        
        self.screen = tk.Entry(root, textvar=self.value, font=("Arial", 20), justify="right")
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=10, ipadx=10, sticky="ew")

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+",
        ]

        row = 1
        col = 0

        for button in buttons:
            if button in ["=", "C", "+", "-", "*", "/"]:
                btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14, "bold"), bg="orange", fg="white")
            else:
                btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14, "bold"),bg= "lightyellow")
            btn.grid(row=row, column=col, padx=5, pady=5)
            btn.bind("<Button-1>", self.on_button_click)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, event):
        num1 = event.widget.cget("text")
        if num1 == "=":
            self.calculate_result()
        elif num1 == "C":
            self.clear_screen()
        else:
            self.update_screen(num1)

    def calculate_result(self):
        expression = self.screen.get()
        try:
            result = eval(expression)
            self.value.set(result)
        except Exception as e:
            self.value.set("Error")

    def clear_screen(self):
        self.value.set("")

    def update_screen(self, value):
        current_value = self.value.get()
        self.value.set(current_value + value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
