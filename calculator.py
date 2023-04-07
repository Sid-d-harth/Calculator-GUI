import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("330x520")
        master.resizable(0, 0)

        self.result = tk.Entry(master, width=24, font=("Arial", 14), bd=10, justify="right")
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.result.insert(0, "0")

        button_list = [
            ("C", "CE", "DEL", "/"),
            ("7", "8", "9", "*"),
            ("4", "5", "6", "-"),
            ("1", "2", "3", "+"),
            ("0", ".", "(", ")"),
            ("=",)
        ]

        for row_index, row_value in enumerate(button_list, start=1):
            for col_index, col_value in enumerate(row_value):
                button = tk.Button(
                    master, text=col_value, width=5, height=2, font=("Arial", 12), bd=5, bg="#f1f1f1",
                    command=lambda text=col_value: self.calculate(text)
                )
                button.grid(row=row_index, column=col_index, padx=5, pady=5)

    def calculate(self, text):
        if text == "=":
            try:
                result = str(eval(self.result.get()))
            except (ZeroDivisionError, SyntaxError) as e:
                result = "Error: " + str(e)
            self.result.delete(0, tk.END)
            self.result.insert(0, result)
        elif text == "C":
            self.result.delete(0, tk.END)
            self.result.insert(0, "0")
        elif text == "CE":
            self.result.delete(0, tk.END)
            self.result.insert(0, "0")
        elif text == "DEL":
            current = self.result.get()
            self.result.delete(0, tk.END)
            self.result.insert(0, current[:-1])
        else:
            current = self.result.get()
            if current == "0":
                self.result.delete(0, tk.END)
                self.result.insert(0, text)
            else:
                self.result.delete(0, tk.END)
                self.result.insert(0, current + text)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
