import tkinter as tk
from PIL import Image, ImageTk
import os
import language
birds = [
    {
        "name_en": "Abyssinian Long-eared Owl",
        "name_or": "Jajjuu",
        "description_en": (
            "A medium-sized owl found in highland forests and "
            "mountain areas."
        ),
        "description_or": (
            "Jajjuun simbirroo halkanii giddu-galeessa ta'ee, "
            "bosona lafa olka'aa fi naannoo gaarotaa keessatti argama."
        ),
        "image": "images/abyssinian_long_eared_owl.jpg"
    },

    {
        "name_en": "Abyssinian Woodpecker",
        "name_or": "Simbirroo muka tumu",
        "description_en": (
            "A woodpecker that lives in montane forests and "
            "woodland habitats."
        ),
        "description_or": (
            "Simbirroon muka tumu bosona gaarotaa fi lafa mukaa "
            "keessatti jiraata."
        ),
        "image": "images/abyssinian_woodpecker.jpg"
    },

    {
        "name_en": "Black-winged Lovebird",
        "name_or": "Simbirroo jaalalaa",
        "description_en": (
            "A small green parrot found mainly in the highlands "
            "of Ethiopia."
        ),
        "description_or": (
            "Simbirroon jaalalaa parrootii xiqqaa magariisaa ta'ee, "
            "baay'inaan lafa olka'aa Itoophiyaa keessatti argama."
        ),
        "image": "images/black_winged_lovebird.jpg"
    },
    {
        "name_en": "Augur Buzzard",
        "name_or": "Risaa",
        "description_en": (
            "A large bird of prey commonly seen flying over "
            "highlands and open areas."
        ),
        "description_or": (
            "Risaaan simbirroo foon nyaatuu guddaa ta'ee, "
            "lafa olka'aa fi bakkeewwan banaa irratti balali'aa mul'ata."
        ),
        "image": "images/augur_buzzard.jpg"
    },

    {
        "name_en": "African Goshawk",
        "name_or": "Risaa bosonaa",
        "description_en": (
            "A forest bird of prey that hunts small birds "
            "and other animals."
        ),
        "description_or": (
            "Risaan bosonaa simbirroo foon nyaatuu ta'ee, "
            "simbirroota xixiqqoo fi bineensota biroo adamsa."
        ),
        "image": "images/african_goshawk.jpg"
    },
    {
        "name_en": "Tawny Eagle",
        "name_or": "Risaa diimaa",
        "description_en": (
            "A large eagle that feeds on small animals and carrion."
        ),
        "description_or": (
            "Risaan diimaan risaa guddaa ta'ee, bineensota xixiqqoo "
            "fi foon bineensota du'anii nyaata."
        ),
        "image": "images/tawny_eagle.jpg"
    },

    {
        "name_en": "Common Fiscal",
        "name_or": "Simbirroo gurraacha fi adii",
        "description_en": (
            "A small black-and-white bird that feeds on insects "
            "and small animals."
        ),
        "description_or": (
            "Simbirroon gurraachaa fi adiin simbirroo xiqqaa ta'ee, "
            "ilbiisotaa fi bineensota xixiqqoo nyaata."
        ),
        "image": "images/common_fiscal.jpg"
    },
    {
        "name_en": "African Paradise Flycatcher",
        "name_or": "Simbirroo dheerina qabdu",
        "description_en": (
            "A beautiful forest bird recognized by its long tail "
            "and insect-eating habits."
        ),
        "description_or": (
            "Simbirroon dheerina qabdu simbirroo bosonaa bareedaa "
            "ta'ee, eegee dheeraa fi ilbiisota nyaachuun beekama."
        ),
        "image": "images/african_paradise_flycatcher.jpg"
    },

    {
        "name_en": "Speckled Mousebird",
        "name_or": "Simbirroo hantuutaa",
        "description_en": (
            "A common bird that feeds mainly on fruits, "
            "leaves, and buds."
        ),
        "description_or": (
            "Simbirroon hantuutaa simbirroo beekamaa ta'ee, "
            "baay'inaan firii, baala fi biqiltuu haaraa nyaata."
        ),
        "image": "images/speckled_mousebird.jpg"
    },
    {
        "name_en": "Red-billed Oxpecker",
        "name_or": "Simbirroo loon irra taa'u",
        "description_en": (
            "A bird that feeds on ticks and other parasites "
            "found on large mammals."
        ),
        "description_or": (
            "Simbirroon loon irra taa'u, harma-qabeeyyii gurguddoo "
            "irraa xixinnaa fi raammoo biroos nyaata."
        ),
        "image": "images/red_billed_oxpecker.jpg"
    },
    {
        "name_en": "African Grey Hornbill",
        "name_or": "Qamalee",
        "description_en": (
            "A medium-sized bird that feeds on fruits, insects, "
            "and small animals."
        ),
        "description_or": (
            "Qamaleen simbirroo giddu-galeessaa ta'ee, firiiwwan, "
            "ilbiisotaa fi bineensota xixiqqoo nyaata."
        ),
        "image": "images/african_grey_hornbill.jpg"
    },
    {
        "name_en": "Silvery-cheeked Hornbill",
        "name_or": "Qamalee guddaa",
        "description_en": (
            "A large forest bird with a distinctive bill "
            "and loud call."
        ),
        "description_or": (
            "Qamaleen guddaan simbirroo bosonaa guddaa ta'ee, "
            "afaan adda ta'ee fi sagalee guddaa qaba."
        ),
        "image": "images/silvery_cheeked_hornbill.jpg"
    },
    {
        "name_en": "Rüppell's Robin-Chat",
        "name_or": "Simbirroo sirbaa",
        "description_en": (
            "A small bird known for its attractive appearance "
            "and musical song."
        ),
        "description_or": (
            "Simbirroon sirbaa simbirroo xiqqaa ta'ee, "
            "bifa bareedaa fi sirba isaa miidhagaa irraa beekama."
        ),
        "image": "images/ruppells_robin_chat.jpg"
    },
    {
        "name_en": "Tacazze Sunbird",
        "name_or": "Simbirroo daraaraa",
        "description_en": (
            "A colorful small bird that feeds mainly on nectar "
            "and insects."
        ),
        "description_or": (
            "Simbirroon daraaraa simbirroo xiqqaa halluu adda addaa "
            "qabu ta'ee, baay'inaan dhangala'aa daraaraa fi ilbiisota nyaata."
        ),
        "image": "images/tacazze_sunbird.jpg"
    },
    {
        "name_en": "Variable Sunbird",
        "name_or": "Simbirroo daraaraa",
        "description_en": (
            "A small colorful bird that feeds on nectar and insects."
        ),
        "description_or": (
            "Simbirroon daraaraa simbirroo xiqqaa halluu bareedaa qabu "
            "ta'ee, dhangala'aa daraaraa fi ilbiisota nyaata."
        ),
        "image": "images/variable_sunbird.jpg"
    },
    {
        "name_en": "White-cheeked Turaco",
        "name_or": "Simbirroo magariisaa",
        "description_en": (
            "A striking green forest bird that feeds mainly "
            "on fruits and vegetation."
        ),
        "description_or": (
            "Simbirroon magariisaa simbirroo bosonaa halluu magariisaa "
            "bareedaa qabu ta'ee, baay'inaan firii fi biqiltuu nyaata."
        ),
        "image": "images/white_cheeked_turaco.jpg"
    },
    {
        "name_en": "Hamerkop",
        "name_or": "Simbirroo mataa boca",
        "description_en": (
            "A distinctive bird known for its unusual head shape "
            "and large nest."
        ),
        "description_or": (
            "Simbirroon mataa boca bifa mataa adda ta'ee fi "
            "mannaa guddaa ijaaruun beekama."
        ),
        "image": "images/hamerkop.jpg"
    },
    {
        "name_en": "Hadada Ibis",
        "name_or": "Hadaa",
        "description_en": (
            "A large ibis often heard calling loudly around "
            "forests and grasslands."
        ),
        "description_or": (
            "Hadaan simbirroo guddaa ta'ee, yeroo baay'ee "
            "naannoo bosonaa fi lafa margaa keessatti sagalee guddaan dhaga'ama."
        ),
        "image": "images/hadada_ibis.jpg"
    },
    {
        "name_en": "Black-headed Weaver",
        "name_or": "Simbirroo mana hodhu",
        "description_en": (
            "A small bird famous for weaving hanging nests "
            "from grass and plant fibers."
        ),
        "description_or": (
            "Simbirroon mana hodhu simbirroo xiqqaa ta'ee, "
            "marga fi hidda biqiltootaa fayyadamuun mana fannifamaa hodha."
        ),
        "image": "images/black_headed_weaver.jpg"
    },
    {
        "name_en": "Red-billed Firefinch",
        "name_or": "Simbirroo diimaa",
        "description_en": (
            "A small colorful finch that feeds mainly on "
            "grass seeds and insects."
        ),
        "description_or": (
            "Simbirroon diimaan simbirroo xiqqaa halluu bareedaa qabu "
            "ta'ee, sanyii margaa fi ilbiisota nyaata."
        ),
        "image": "images/red_billed_firefinch.jpg"
    }
]

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

    header_frame = tk.Frame(
        main_frame,
        bg="#e8f5e9"
    )
    header_frame.pack(
        fill="x",
        padx=30,
        pady=(15, 5)
    )

    if language.is_english():
        title_text = "🐦 Birds of Chilimo Forest"
        subtitle_text = (
            "Bird species found in and around Chilimo Forest"
        )
    else:
        title_text = "🐦 Simbirroota Bosona Chilimoo"
        subtitle_text = (
            "Gosoota simbirrootaa Bosona Chilimoo fi "
            "naannoo isaa keessatti argaman"
        )
    title = tk.Label(
        header_frame,
        text=title_text,
        font=("Arial", 24, "bold"),
        bg="#e8f5e9",
        fg="#1b5e20"
    )
    title.pack(
        pady=(0, 5)
    )
    subtitle = tk.Label(
        header_frame,
        text=subtitle_text,
        font=("Arial", 11),
        bg="#e8f5e9",
        fg="#555555"
    )
    subtitle.pack(
        pady=(0, 8)
    )
    scroll_frame = tk.Frame(
        main_frame,
        bg="#e8f5e9"
    )
    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=5
    )
    canvas = tk.Canvas(
        scroll_frame,
        bg="#e8f5e9",
        highlightthickness=0
    )
    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )
    scrollbar = tk.Scrollbar(
        scroll_frame,
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
    birds_frame = tk.Frame(
        canvas,
        bg="#e8f5e9"
    )
    canvas_window = canvas.create_window(
        (0, 0),
        window=birds_frame,
        anchor="nw"
    )
    def update_scroll(event=None):
        canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    birds_frame.bind(
        "<Configure>",
        update_scroll
    )
    def resize_frame(event):

        canvas.itemconfig(
            canvas_window,
            width=event.width
        )
    canvas.bind(
        "<Configure>",
        resize_frame
    )
    image_references = []
    for number, bird in enumerate(birds, start=1):

        bird_frame = tk.Frame(
            birds_frame,
            bg="white",
            bd=1,
            relief="solid"
        )
        bird_frame.pack(
            fill="x",
            padx=30,
            pady=8
        )
        image_frame = tk.Frame(
            bird_frame,
            bg="white",
            width=220,
            height=170
        )
        image_frame.pack(
            side="left",
            padx=15,
            pady=15
        )
        image_frame.pack_propagate(False)
        image_path = get_image_path(
            bird["image"]
        )
        print(
            "Loading:",
            bird["name_en"],
            "->",
            image_path
        )
        if os.path.isfile(image_path):
            try:
                with Image.open(image_path) as original_image:
                    image = original_image.copy()
                image.thumbnail(
                    (200, 150),
                    Image.Resampling.LANCZOS
                )
                photo = ImageTk.PhotoImage(
                    image
                )
                image_label = tk.Label(
                    image_frame,
                    image=photo,
                    bg="white"
                )
                image_label.pack(
                    fill="both",
                    expand=True
                )
                image_label.image = photo
                image_references.append(photo)
            except Exception as error:
                print(
                    "IMAGE ERROR:",
                    bird["name_en"],
                    error
                )
                image_label = tk.Label(
                    image_frame,
                    text=language.get_text("image_error"),
                    font=("Arial", 12, "bold"),
                    bg="#eeeeee",
                    fg="red"
                )
                image_label.pack(
                    fill="both",
                    expand=True
                )
        else:
            print(
                "IMAGE NOT FOUND:",
                image_path
            )
            image_label = tk.Label(
                image_frame,
                text=(
                    "📷\n" +
                    language.get_text("no_image")
                ),
                font=("Arial", 13, "bold"),
                bg="#eeeeee",
                fg="#777777"
            )

            image_label.pack(
                fill="both",
                expand=True
            )
        info_frame = tk.Frame(
            bird_frame,
            bg="white"
        )
        info_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=15
        )
        if language.is_english():
            bird_name = bird["name_en"]
            second_name = (
                f"Afaan Oromoo: {bird['name_or']}"
            )

            description = bird["description_en"]
        else:
            bird_name = bird["name_or"]
            second_name = (
                f"Maqaa Ingilizii: {bird['name_en']}"
            )
            description = bird["description_or"]
        name_label = tk.Label(
            info_frame,
            text=f"{number}. {bird_name}",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#1b5e20",
            anchor="w"
        )
        name_label.pack(
            fill="x",
            pady=(0, 8)
        )
        second_name_label = tk.Label(
            info_frame,
            text=second_name,
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#2e7d32",
            anchor="w"
        )
        second_name_label.pack(
            fill="x",
            pady=5
        )
        description_label = tk.Label(
            info_frame,
            text=description,
            font=("Arial", 11),
            bg="white",
            fg="#333333",
            anchor="w",
            justify="left",
            wraplength=650
        )
        description_label.pack(
            fill="x",
            pady=(5, 0)
        )

    def mouse_wheel(event):
        if event.delta:
            canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )
    canvas.bind(
        "<MouseWheel>",
        mouse_wheel
    )
    # Linux
    canvas.bind(
        "<Button-4>",
        lambda event: canvas.yview_scroll(
            -3,
            "units"
        )
    )
    canvas.bind(
        "<Button-5>",
        lambda event: canvas.yview_scroll(
            3,
            "units"
        )
    )