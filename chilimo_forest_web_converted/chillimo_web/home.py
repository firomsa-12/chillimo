import tkinter as tk
from PIL import Image, ImageTk
import os
import language
def get_image_path(image_file):
    base_folder = os.path.dirname(
        os.path.abspath(__file__)
    )
    return os.path.join(
        base_folder,
        image_file
    )
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
    if language.is_english():
        title_text = "Welcome to Chilimo Forest"
        introduction = (
            "Welcome to the Chilimo Forest Visitor Information System.\n\n"
            "Chilimo Forest is an important natural forest in Ethiopia.\n"
            "The forest provides habitat for many plants, birds and\n"
            "wild animals.\n\n"
            "This application helps visitors discover the history,\n"
            "wildlife and plants of Chilimo Forest."
        )
        location_title = "📍 Location"
        location_text = (
            "Chilimo Forest is located in Dendi District,\n"
            "West Shewa Zone, Oromia Regional State, Ethiopia."
        )
        visitor_message = (
            "Use the Location button above to see the forest map."
        )
        image_not_found = "Forest image not found."
    else:
        title_text = "Baga Gara Bosona Chilimoo Nagaan Dhuftan"
        introduction = (
            "Baga gara Sirna Odeeffannoo Daawwattoota Bosona Chilimoo "
            "nagaan dhuftan.\n\n"

            "Bosonni Chilimoo bosona uumamaa barbaachisaa Itoophiyaa "
            "keessatti argamuudha.\n"
            "Bosonni kun biqiltoota, simbirrootaa fi bineensota "
            "bosonaa hedduudhaaf\n"
            "bakka jireenyaa ni kenna.\n\n"

            "Appilikeeshiniin kun daawwattoonni seenaa, bineensota "
            "bosonaa fi\n"
            "biqiltoota Bosona Chilimoo akka baratan gargaara."
        )
        location_title = "📍 Bakka Argamaa"
        location_text = (
            "Bosonni Chilimoo Godina Dandii,\n"
            "Godina Lixa Shawa, Naannoo Oromiyaa, Itoophiyaa keessatti "
            "argama."
        )
        visitor_message = (
            "Kaartaa bosonichaa ilaaluuf qaree Bakka Argamaa armaan "
            "olii cuqaasaa."
        )
        image_not_found = "Suuraan bosichaa hin argamne."
    title = tk.Label(
        main_frame,
        text=title_text,
        font=("Arial", 28, "bold"),
        bg="#e8f5e9",
        fg="#1b5e20"
    )
    title.pack(
        pady=15
    )
    image_path = get_image_path(
        "images/chilimo_forest.jpg"
    )
    if os.path.isfile(image_path):
        try:
            original_image = Image.open(
                image_path
            )
            image = original_image.copy()
            original_image.close()
            image = image.resize(
                (600, 280),
                Image.Resampling.LANCZOS
            )
            forest_image = ImageTk.PhotoImage(
                image
            )
            picture = tk.Label(
                main_frame,
                image=forest_image,
                bg="#e8f5e9"
            )
            picture.image = forest_image
            picture.pack(
                pady=10
            )
        except Exception:
            error = tk.Label(
                main_frame,
                text=image_not_found,
                font=("Arial", 14),
                bg="#e8f5e9",
                fg="red"
            )
            error.pack(
                pady=50
            )
    else:
        error = tk.Label(
            main_frame,
            text=image_not_found,
            font=("Arial", 14),
            bg="#e8f5e9",
            fg="red"
        )
        error.pack(
            pady=50
        )
    text = tk.Label(
        main_frame,
        text=introduction,
        font=("Arial", 13),
        bg="#e8f5e9",
        fg="#333333",
        justify="center"
    )
    text.pack(
        pady=10
    )
    location_box = tk.Frame(
        main_frame,
        bg="white",
        padx=20,
        pady=10
    )
    location_box.pack(
        padx=100,
        pady=10,
        fill="x"
    )
    location_title_label = tk.Label(
        location_box,
        text=location_title,
        font=("Arial", 15, "bold"),
        bg="white",
        fg="#1b5e20"
    )
    location_title_label.pack()
    location_text_label = tk.Label(
        location_box,
        text=location_text,
        font=("Arial", 11),
        bg="white",
        fg="#333333",
        justify="center"
    )
    location_text_label.pack(
        pady=5
    )
    message = tk.Label(
        main_frame,
        text=visitor_message,
        font=("Arial", 11, "italic"),
        bg="#e8f5e9",
        fg="#2e7d32"
    )
    message.pack(
        pady=5
    )