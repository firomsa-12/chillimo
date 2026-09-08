import tkinter as tk
from PIL import Image, ImageTk
def show(content):
    for widget in content.winfo_children():
        widget.destroy()
    title = tk.Label(
        content,
        text="Location of Chilimo Forest",
        font=("Arial", 26, "bold"),
        bg="#e8f5e9",
        fg="#1b5e20"
    )
    title.pack(pady=20)
    information = (
        "Chilimo Forest is located in Dendi District,\n"
        "West Shewa Zone, Oromia Regional State, Ethiopia.\n\n"
        "The forest is located near Ginchi town and is\n"
        "approximately 70–90 km west of Addis Ababa.\n\n"
        "It is a highland forest with an elevation of\n"
        "approximately 2,170–3,054 meters above sea level."
    )
    text = tk.Label(
        content,
        text=information,
        font=("Arial", 13),
        bg="#e8f5e9",
        fg="#333333",
        justify="center"
    )
    text.pack(pady=10)
    try:
        image = Image.open("images/chilimo_map.jpg")
        image = image.resize((650, 300))
        map_image = ImageTk.PhotoImage(image)
        picture = tk.Label(
            content,
            image=map_image,
            bg="#e8f5e9"
        )
        picture.image = map_image
        picture.pack(pady=10)
    except FileNotFoundError:
        error = tk.Label(
            content,
            text="Map image not found.\n"
                 "Please put chilimo_map.jpg inside the images folder.",
            font=("Arial", 13),
            fg="red",
            bg="#e8f5e9"
        )
        error.pack(pady=50)