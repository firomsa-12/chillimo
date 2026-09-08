import tkinter as tk
from tkinter import messagebox
import home
import history
import wild_animals
import birds
import plants
import attraction
import location
import language
import about
window = tk.Tk()
window.title(
    "Chilimo Forest Visitor Information"
)
window.attributes(
    "-fullscreen",
    True
)
window.configure(
    bg="#e8f5e9"
)
def exit_fullscreen(event=None):
    window.attributes(
        "-fullscreen",
        False
    )

window.bind(
    "<Escape>",
    exit_fullscreen
)
def show_home():
    home.show(content)
def show_history():
    history.show(content)
def show_animals():
    wild_animals.show(content)
def show_birds():
    birds.show(content)
def show_plants():
    plants.show(content)
def show_attraction():
    attraction.show(content)
def show_location():
    location.show(content)
def show_about():
    about.show(content)
def exit_program():
    answer = messagebox.askyesno(
        language.get_text("exit"),
        language.get_text("exit_message")
    )
    if answer:
        window.destroy()
def change_language(choice=None):
    selected_language = language_box.get()
    if selected_language == "English":
        language.change_language(
            "english"
        )
    else:
        language.change_language(
            "oromo"
        )
    update_menu()
    refresh_current_page()
current_page = "home"
def set_page(page_name):
    global current_page
    current_page = page_name
def refresh_current_page():
    if current_page == "home":
        show_home()
    elif current_page == "history":
        show_history()
    elif current_page == "animals":
        show_animals()
    elif current_page == "birds":
        show_birds()
    elif current_page == "plants":
        show_plants()
    elif current_page == "attraction":
        show_attraction()
    elif current_page == "location":
        show_location()
    elif current_page == "about":
        show_about()
def open_home():
    set_page("home")
    show_home()
def open_history():
    set_page("history")
    show_history()
def open_animals():
    set_page("animals")
    show_animals()
def open_birds():
    set_page("birds")
    show_birds()
def open_plants():
    set_page("plants")
    show_plants()
def open_attraction():
    set_page("attraction")
    show_attraction()
def open_location():
    set_page("location")
    show_location()
def open_about():
    set_page("about")
    show_about()
def update_menu():
    home_button.config(
        text=language.get_text("home")
    )
    history_button.config(
        text=language.get_text("history")
    )
    animals_button.config(
        text=language.get_text("animals")
    )
    birds_button.config(
        text=language.get_text("birds")
    )
    plants_button.config(
        text=language.get_text("plants")
    )
    attraction_button.config(
        text=language.get_text("attractions")
    )
    location_button.config(
        text=language.get_text("location")
    )
    about_button.config(
        text=language.get_text("about")
    )
    exit_button.config(
        text=language.get_text("exit")
    )
    language_label.config(
        text=language.get_text("language")
    )
    title.config(
        text=language.get_text("title")
    )
    subtitle.config(
        text=language.get_text("visitor_system")
    )
header = tk.Frame(
    window,
    bg="#1b5e20",
    height=100
)
header.pack(
    fill="x"
)
title = tk.Label(
    header,
    text=language.get_text("title"),
    font=("Arial", 28, "bold"),
    bg="#1b5e20",
    fg="white"
)
title.pack(
    pady=(15, 2)
)
subtitle = tk.Label(
    header,
    text=language.get_text("visitor_system"),
    font=("Arial", 11),
    bg="#1b5e20",
    fg="#c8e6c9"
)
subtitle.pack()
menu = tk.Frame(
    window,
    bg="#2e7d32"
)
menu.pack(
    fill="x"
)
button_style = {
    "bg": "#2e7d32",
    "fg": "white",
    "activebackground": "#1b5e20",
    "activeforeground": "white",
    "font": ("Arial", 11, "bold"),
    "relief": "flat",
    "padx": 15,
    "pady": 12
}
home_button = tk.Button(
    menu,
    text=language.get_text("home"),
    command=open_home,
    **button_style
)
home_button.pack(
    side="left"
)
history_button = tk.Button(
    menu,
    text=language.get_text("history"),
    command=open_history,
    **button_style
)
history_button.pack(
    side="left"
)
animals_button = tk.Button(
    menu,
    text=language.get_text("animals"),
    command=open_animals,
    **button_style
)
animals_button.pack(
    side="left"
)
birds_button = tk.Button(
    menu,
    text=language.get_text("birds"),
    command=open_birds,
    **button_style
)
birds_button.pack(
    side="left"
)

plants_button = tk.Button(
    menu,
    text=language.get_text("plants"),
    command=open_plants,
    **button_style
)
plants_button.pack(
    side="left"
)
attraction_button = tk.Button(
    menu,
    text=language.get_text("attractions"),
    command=open_attraction,
    **button_style
)
attraction_button.pack(
    side="left"
)
location_button = tk.Button(
    menu,
    text=language.get_text("location"),
    command=open_location,
    **button_style
)
location_button.pack(
    side="left"
)
about_button = tk.Button(
    menu,
    text=language.get_text("about"),
    command=open_about,
    **button_style
)
about_button.pack(
    side="left"
)
exit_button = tk.Button(
    menu,
    text=language.get_text("exit"),
    command=exit_program,
    bg="#c62828",
    fg="white",
    activebackground="#8e0000",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    padx=15,
    pady=12
)
exit_button.pack(
    side="right"
)
language_frame = tk.Frame(
    menu,
    bg="#2e7d32"
)
language_frame.pack(
    side="right",
    padx=10
)
language_label = tk.Label(
    language_frame,
    text=language.get_text("language"),
    font=("Arial", 10, "bold"),
    bg="#2e7d32",
    fg="white"
)
language_label.pack(
    side="left",
    padx=5
)
language_box = tk.StringVar()

language_box.set(
    "English"
)
language_menu = tk.OptionMenu(
    language_frame,
    language_box,
    "English",
    "Afaan Oromoo",
    command=change_language
)
language_menu.config(
    bg="white",
    fg="#1b5e20",
    activebackground="#c8e6c9",
    activeforeground="#1b5e20",
    font=("Arial", 10, "bold"),
    width=12,
    relief="flat"
)
language_menu["menu"].config(
    font=("Arial", 10)
)
language_menu.pack(
    side="left"
)
content = tk.Frame(
    window,
    bg="#e8f5e9"
)
content.pack(
    fill="both",
    expand=True
)
set_page("home")
show_home()
window.mainloop()