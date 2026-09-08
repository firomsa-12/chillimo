import tkinter as tk
import language
def show(content):
    for widget in content.winfo_children():
        widget.destroy()
    container = tk.Frame(
        content,
        bg="#e8f5e9"
    )
    container.pack(
        fill="both",
        expand=True
    )
    canvas = tk.Canvas(
        container,
        bg="#e8f5e9",
        highlightthickness=0
    )
    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )
    scrollbar = tk.Scrollbar(
        container,
        orient="vertical",
        command=canvas.yview
    )
    scrollbar.pack(
        side="right",
        fill="y"
    )
    canvas.configure(
        yscrollcommand=scrollbar.set
    )
    frame = tk.Frame(
        canvas,
        bg="#e8f5e9"
    )
    canvas_window = canvas.create_window(
        (0, 0),
        window=frame,
        anchor="nw"
    )
    def update_scroll_region(event=None):

        canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    frame.bind(
        "<Configure>",
        update_scroll_region
    )
    def update_frame_width(event):

        canvas.itemconfig(
            canvas_window,
            width=event.width
        )
    canvas.bind(
        "<Configure>",
        update_frame_width
    )
    def mouse_wheel(event):

        canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )
    canvas.bind_all(
        "<MouseWheel>",
        mouse_wheel
    )
    inner_frame = tk.Frame(
        frame,
        bg="#e8f5e9"
    )
    inner_frame.pack(
        fill="both",
        expand=True,
        padx=50,
        pady=30
    )
    title = tk.Label(
        inner_frame,
        text=(
            "ABOUT CHILIMO FOREST"
            if language.is_english()
            else "WAA'EE BOSONA CHILIMOO"
        ),
        font=("Arial", 28, "bold"),
        bg="#e8f5e9",
        fg="#1b5e20"
    )
    title.pack(
        pady=(20, 20)
    )
    introduction = tk.Label(
        inner_frame,
        text=(
            "Chilimo Forest Visitor Information System"
            if language.is_english()
            else "Sirna Odeeffannoo Daawwattoota Bosona Chilimoo"
        ),
        font=("Arial", 18, "bold"),
        bg="#e8f5e9",
        fg="#2e7d32"
    )

    introduction.pack(
        pady=10
    )
    if language.is_english():

        description_text = (
            "This application provides useful information "
            "about Chilimo Forest and its natural resources.\n\n"

            "Visitors can learn about the history of the forest, "
            "wild animals, birds, plants, attractions, and location.\n\n"

            "The system is designed to help visitors understand "
            "and explore the natural beauty and importance of "
            "Chilimo Forest."
        )
    else:
        description_text = (
            "Appilikeeshiniin kun waa'ee Bosona Chilimoo fi "
            "qabeenya uumamaa isaa odeeffannoo barbaachisaa kenna.\n\n"

            "Daawwattoonni seenaa bosonaa, bineensota bosonaa, "
            "simbirroota, biqiltoota, bakka hawwataa fi iddoo "
            "bosonichaa ilaalchisee barachuu danda'u.\n\n"

            "Sirni kun daawwattoonni bareedinaa fi faayidaa "
            "uumamaa Bosona Chilimoo akka hubatanii fi "
            "daawwatan gargaaruuf qophaa'e."
        )
    description = tk.Label(
        inner_frame,
        text=description_text,
        font=("Arial", 14),
        bg="#e8f5e9",
        fg="#333333",
        justify="center",
        wraplength=1000
    )

    description.pack(
        pady=20
    )
    features_title = tk.Label(
        inner_frame,
        text=(
            "System Features"
            if language.is_english()
            else "Wantoota Sirnichaa"
        ),
        font=("Arial", 18, "bold"),
        bg="#e8f5e9",
        fg="#1b5e20"
    )
    features_title.pack(
        pady=(20, 10)
    )
    if language.is_english():

        features_text = (
            "• Forest History\n"
            "• Wild Animals Information\n"
            "• Birds Information\n"
            "• Plants Information\n"
            "• Tourist Attractions\n"
            "• Forest Location\n"
            "• English and Afaan Oromoo Language Support"
        )

    else:
        features_text = (
            "• Seenaa Bosonaa\n"
            "• Odeeffannoo Bineensota Bosonaa\n"
            "• Odeeffannoo Simbirrootaa\n"
            "• Odeeffannoo Biqiltootaa\n"
            "• Bakka Hawwataa Turistootaa\n"
            "• Iddoo Bosonichaa\n"
            "• Deeggarsa Afaan Ingilizii fi Afaan Oromoo"
        )
    features = tk.Label(
        inner_frame,
        text=features_text,
        font=("Arial", 13),
        bg="#e8f5e9",
        fg="#444444",
        justify="left"
    )

    features.pack(
        pady=10
    )
    developers_title = tk.Label(
        inner_frame,
        text=(
            "Developed By"
            if language.is_english()
            else "Kan Qopheesse"
        ),
        font=("Arial", 14, "bold"),
        bg="#e8f5e9",
        fg="#1b5e20"
    )
    developers_title.pack(
        pady=(30, 5)
    )
    developers = tk.Label(
        inner_frame,
        text=(
            "Abdi Gebisa \n"
            "Firomsa Girma \n"
            "Getu Angecha \n" 
           " Jara Ayele\n" 
            "Wakjira Girma"
        ),
        font=("Arial", 12, "bold"),
        bg="#e8f5e9",
        fg="#444444",
        justify="center"
    )
    developers.pack(
        pady=5
    )
    footer = tk.Label(
        inner_frame,
        text=(
            "Chilimo Forest Visitor Information System"
            if language.is_english()
            else "Sirna Odeeffannoo Daawwattoota Bosona Chilimoo"
        ),
        font=("Arial", 11, "italic"),
        bg="#e8f5e9",
        fg="#666666"
    )
    footer.pack(
        pady=(15, 30)
    )
    canvas.update_idletasks()
    canvas.yview_moveto(0)
