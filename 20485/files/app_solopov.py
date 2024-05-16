import tkinter as tk
from tkinter import messagebox



def display_greeting():
    full_name = text.get("1.0", "end-1c")
    greeting_label.config(text=f"Здравствуй,{full_name}!")


def paste_text(event):
        text.delete("1.0","end-1c")
        text.insert("1.0",root.clipboard_get())


def confirm_exit():
      result = messagebox.askokcancel("Выход","Вы уверены что хотите выйти?")
      if result:
            root.destroy()


root = tk.Tk()
root.title("Приветствие")


greeting_label = tk.Label(root, text="Введите ваше ФИО")
greeting_label.pack(pady=10)


text = tk.Text(root, height=2, width=30)
text.pack(pady=10)


button = tk.Button(root, text="Приветствовать", command=display_greeting)
button.pack(pady=10)

exit_button = tk.Button(root, text="Выход", command=confirm_exit)
exit_button.pack(pady=10)

root.mainloop()