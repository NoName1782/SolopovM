import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        number1 = float(entry_number1.get())
        number2 = float(entry_num2.get())

        if operation_var.get() == "Сложение":
            result = number1 + number2
        elif operation_var.get() == "Вычитание":
            result = number1 - number2
        elif operation_var.get() == "Умножение":
            result = number1 * number2
        elif operation_var.get() == "Деление":
            if number2 == 0:
                messagebox.showerror("Ошибка", "Делить на ноль невозможно.")
                return
            result = number1 / number2
        else:
            messagebox.showerror("Ошибка", "Невозможно продолжить.")
            return

        result_label.config(text=f"Результат: ={result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите правильные значения.")

root = tk.Tk()
root.title("Калькулятор")

label_number1 = tk.Label(root, text="Число Х:")
label_number1.grid(row=0, column=0, padx=10, pady=10)
entry_number1 = tk.Entry(root)
entry_number1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Число Y:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operation = tk.Label(root, text="Выберите операцию:")
label_operation.grid(row=2, column=0, padx=10, pady=10)
operations = ["Сложение", "Вычитание", "Умножение", "Деление"]
operation_var = tk.StringVar(value=operations[0])
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Результат: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()