import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import traceback

def send_request():
    messagebox.showinfo("Заявка принята", "Стол был успешно забронирован на указанное время")

root = tk.Tk()
root.title("Приложение для компании 'Пекарня Буханка'")

try:
    initial_width, initial_height = 1600, 940

    background_image = Image.open("D:/20485/images/Background.png")
    background_image = background_image.resize((initial_width, initial_height))
    background_img = ImageTk.PhotoImage(background_image)
    root.geometry(f"{initial_width}x{initial_height}")
    canvas = tk.Canvas(root, width=initial_width, height=initial_height)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=background_img, tags="bg_images")

    background2_image = Image.open("D:/20485/images/Logo.png")
    background2_image = background2_image.resize((500, 300))
    background2_img = ImageTk.PhotoImage(background2_image)

    background3_image = Image.open("D:/20485/images/Background2.png")
    background3_image = background3_image.resize((500, 300))
    background3_img = ImageTk.PhotoImage(background3_image)

    bottom_right_image_id = canvas.create_image(1600, 940, anchor=tk.SE, image=background2_img, tags="images")

    def change_images():
        current_image_id = bottom_right_image_id
        current_image = canvas.itemcget(current_image_id, "image")
        next_image = background3_img if current_image == str(background2_img) else background2_img
        canvas.itemconfig(current_image_id, image=next_image)
        root.after(5000, change_images)

    root.after(5000, change_images)

    form_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
    form_frame.place(x=20, y=20, width=250, height=150)

    name_label = tk.Label(form_frame, text="Имя:")
    name_label.grid(row=0, column=0, padx=5, pady=5)

    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    table_label = tk.Label(form_frame, text="Номер стола:")
    table_label.grid(row=1, column=0, padx=5, pady=5)

    table_entry = tk.Entry(form_frame)
    table_entry.grid(row=1, column=1, padx=5, pady=5)

    time_label = tk.Label(form_frame, text="Время брони:")
    time_label.grid(row=2, column=0, padx=5, pady=5)

    time_entry = tk.Entry(form_frame)
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    submit_button = tk.Button(form_frame, text="Заявка на бронирование", command=send_request)
    submit_button.grid(row=3, columnspan=3, padx=5, pady=5)

    def move_start(event):
        form_frame.x = event.x
        form_frame.y = event.y

    def move_drag(event):
        form_frame.place(x=root.winfo_pointerx() - root.winfo_rootx() - form_frame.x,
                         y=root.winfo_pointery() - root.winfo_rooty() - form_frame.y,
                         anchor=tk.NW)

    form_frame.bind("<Button-1>", move_start)
    form_frame.bind("<B1-Motion>", move_drag)

    root.mainloop()

except Exception as e:
    traceback.print_exc()
    print("Ошибка при загрузке и изменении размеров изображения фона", e)