import tkinter as tk
from PIL import Image, ImageTk
import os
def show(content):
    for widget in content.winfo_children():
        widget.destroy()
    main_frame = tk.Frame(
        content,
        bg="#e8f5e9"
    )
    main_frame.pack(
        fill="both",
        expand=True
    )
    title = tk.Label(
        main_frame,
        text="📍 Attractions of Chilimo Forest",
        font=("Arial", 26, "bold"),
        bg="#e8f5e9",
        fg="#1b5e20"
    )
    title.pack(
        pady=30
    )
    attraction_box = tk.Frame(
        main_frame,
        bg="white",
        bd=1,
        relief="solid"
    )
    attraction_box.pack(
        fill="x",
        padx=50,
        pady=10
    )
    slideshow_label = tk.Label(
        attraction_box,
        bg="white"
    )
    slideshow_label.pack(
        padx=20,
        pady=(20, 10)
    )
    image_folder = os.path.join(
        os.path.dirname(__file__),
        "images"
    )
    image_files = []
    for number in range(1, 8):
        image_file = os.path.join(
            image_folder,
            f"image_{number}.jpg"
        )
        if os.path.isfile(image_file):
            image_files.append(
                image_file
            )
    photos = []
    for file in image_files:
        try:
            image = Image.open(
                file
            )
            image.thumbnail(
                (850, 400)
            )
            photo = ImageTk.PhotoImage(
                image
            )
            photos.append(
                photo
            )
        except Exception as e:
            print(
                "Could not load:",
                file
            )
            print(e)
    current_image = 0
    def change_image():
        nonlocal current_image
        if not photos:
            slideshow_label.config(
                text="No images found",
                font=("Arial", 14),
                fg="red"
            )
            return
        slideshow_label.config(
            image=photos[current_image],
            text=""
        )
        slideshow_label.image = photos[current_image]
        current_image += 1
        if current_image >= len(photos):
            current_image = 0
        slideshow_label.after(
            3000,
            change_image
        )
    change_image()
    name = tk.Label(
        attraction_box,
        text="🌳 Chilimo Forest",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="#1b5e20"
    )

    name.pack(
        anchor="w",
        padx=20,
        pady=(10, 5)
    )
    description = tk.Label(
        attraction_box,
        text=(
            "Chilimo Forest is an important Afro-montane forest "
            "area with beautiful landscapes, wildlife, birds and "
            "native plants. Visitors can enjoy the natural "
            "environment and learn about forest biodiversity "
            "and conservation."
        ),
        font=("Arial", 12),
        bg="white",
        fg="#333333",
        justify="left",
        wraplength=850
    )

    description.pack(
        anchor="w",
        padx=20,
        pady=(5, 20)
    )
