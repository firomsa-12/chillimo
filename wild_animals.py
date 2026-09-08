import tkinter as tk
from PIL import Image, ImageTk
import os
import language
animals = [
    {
        "name_en": "Common Warthog",
        "name_or": "Booyyee Bosonaa",
        "description_en": (
            "A wild pig that lives in grassland, woodland, "
            "and forest-edge habitats."
        ),
        "description_or": (
            "Booyyeen bosonaa bineensa bosonaa ta'ee, "
            "lafa margaa, lafa mukaa fi qarqara bosonaa "
            "keessatti argama."
        ),
        "image": "images/warthog.jpg"
    },
    {
        "name_en": "Olive Baboon",
        "name_or": "Jaldeessa",
        "description_en": (
            "A social monkey that lives in groups and feeds "
            "on fruits, plants, seeds, and insects."
        ),
        "description_or": (
            "Jaldeessaan bineensa gareedhaan jiraatu ta'ee, "
            "firii, biqiltoota, sanyii fi ilbiisota nyaata."
        ),
        "image": "images/olive_baboon.jpg"
    },
    {
        "name_en": "Bushbuck",
        "name_or": "Bosonuu/Dulbee",
        "description_en": (
            "A shy antelope that lives mainly in forest, "
            "woodland, and areas with dense vegetation."
        ),
        "description_or": (
            "Bosonuun ykn Dulbeen bineensa bosonaa sodaataa "
            "ta'ee, bosona, lafa mukaa fi naannoo biqiltoonni "
            "baay'atan keessatti jiraata."
        ),
        "image": "images/bushbuck.jpg"
    },
    {
        "name_en": "Common Duiker",
        "name_or": "Kuroo",
        "description_en": (
            "A small antelope that feeds on leaves, fruits, "
            "flowers, and other vegetation."
        ),
        "description_or": (
            "Kuroon bineensa bosonaa xiqqaa ta'ee, baala, "
            "firii, daraaraa fi biqiltoota biroo nyaata."
        ),
        "image": "images/common_duiker.jpg"
    },
    {
        "name_en": "Grivet Monkey",
        "name_or": "Jaldeessa",
        "description_en": (
            "A small African monkey commonly found in "
            "woodland and forest habitats."
        ),
        "description_or": (
            "Jaldeessaan bineensa Afrikaa xiqqaa ta'ee, "
            "lafa mukaa fi naannoo bosonaa keessatti "
            "yeroo baay'ee argama."
        ),
        "image": "images/grivet_monkey.jpg"
    },

    {
        "name_en": "Leopard",
        "name_or": "Qeerransa",
        "description_en": (
            "A powerful and elusive big cat that can live "
            "in forests, woodlands, and other habitats."
        ),
        "description_or": (
            "Qeerransi bineensa adamsaa cimaa fi dhokataa "
            "ta'ee, bosona, lafa mukaa fi naannolee biroo "
            "keessatti jiraachuu danda'a."
        ),
        "image": "images/leopard.jpg"
    },

    {
        "name_en": "Hyena",
        "name_or": "Waraabessa",
        "description_en": (
            "A strong carnivore that is an important part "
            "of the African ecosystem."
        ),
        "description_or": (
            "Waraabessi bineensa foon nyaatu cimaa ta'ee, "
            "sirna ikoo Afrikaa keessatti gahee barbaachisaa qaba."
        ),
        "image": "images/hyena.jpg"
    },

    {
        "name_en": "Aardvark",
        "name_or": "Awwaaldiigessa/Olokee",
        "description_en": (
            "A nocturnal mammal that uses its powerful claws "
            "to dig for ants and termites."
        ),
        "description_or": (
            "Awwaaldiigessi bineensa halkanii ta'ee, "
            "qeensa isaa cimaa fayyadamuun goondaa fi "
            "raammoo nyaatuuf qota."
        ),
        "image": "images/aardvark.jpg"
    },
    {
        "name_en": "Porcupine",
        "name_or": "Xaddee",
        "description_en": (
            "A nocturnal rodent covered with sharp quills "
            "that provide protection from predators."
        ),
        "description_or": (
            "Xaddeen bineensa halkanii qoree qara qabu "
            "kan bineensota isa adamsan irraa of eeguudha."
        ),
        "image": "images/porcupine.jpg"
    },
    {
        "name_en": "Guereza",
        "name_or": "Jaldeessa gurraacha fi adii",
        "description_en": (
            "A black-and-white monkey that spends much "
            "of its time in trees."
        ),
        "description_or": (
            "Jaldeessi gurraacha fi adiin bineensa halluu "
            "gurraachaa fi adii qabu ta'ee, yeroo isaa hedduu "
            "mukarra dabarsa."
        ),
        "image": "images/guereza.jpg"
    },
    {
        "name_en": "Giant Forest Hog",
        "name_or": "Booyyee bosonaa guddaa",
        "description_en": (
            "A large wild pig that lives in forests "
            "and feeds mainly on vegetation."
        ),
        "description_or": (
            "Booyyeen bosonaa guddaan bineensa bosonaa guddaa "
            "ta'ee, baay'inaan biqiltoota nyaata."
        ),
        "image": "images/giant_forest_hog.jpg"
    },
    {
        "name_en": "African Civet",
        "name_or": "Xirinyii",
        "description_en": (
            "A mostly nocturnal mammal that feeds on fruits, "
            "insects, small animals, and other foods."
        ),
        "description_or": (
            "Xirinyii bineensa irra caalaan halkanii ta'ee, "
            "firii, ilbiisota, bineensota xixiqqoo fi nyaata "
            "biroo nyaata."
        ),
        "image": "images/african_civet.jpg"
    },
    {
        "name_en": "Genet",
        "name_or": "Hamaagota/Amaagaaguraa/Moree",
        "description_en": (
            "A small, agile mammal that is mainly "
            "active at night."
        ),
        "description_or": (
            "Hamaagoti bineensa xiqqaa fi socho'aa ta'ee, "
            "baay'inaan halkan socho'a."
        ),
        "image": "images/genet.jpg"
    },
    {
        "name_en": "Klipspringer",
        "name_or": "Kuroo gaaraa",
        "description_en": (
            "A small antelope adapted to rocky hills "
            "and mountainous areas."
        ),
        "description_or": (
            "Kuroon gaarraa bineensa xiqqaa ta'ee, "
            "gaara dhagaa fi naannoo gaarotaa keessa "
            "jiraachuuf kan madaqeudha."
        ),
        "image": "images/klipspringer.jpg"
    },
    {
        "name_en": "Mountain Reedbuck",
        "name_or": "Borofa/Godaa",
        "description_en": (
            "A medium-sized antelope associated with "
            "mountainous grasslands and rocky habitats."
        ),
        "description_or": (
            "Borofaan ykn Godaan bineensa giddu-galeessaa "
            "ta'ee, lafa margaa gaarotaa fi naannoo dhagaa "
            "keessatti argama."
        ),
        "image": "images/mountain_reedbuck.jpg"
    },
    {
        "name_en": "Serval",
        "name_or": "Adurree diidaa",
        "description_en": (
            "A medium-sized wild cat with long legs that "
            "hunts mainly small mammals and birds."
        ),
        "description_or": (
            "Adurreen diidaa bineensa adamsaa giddu-galeessaa "
            "miila dheeraa qabu ta'ee, baay'inaan bineensota "
            "harma qaban xixiqqoo fi simbirroota adamsa."
        ),
        "image": "images/serval.jpg"
    },
    {
        "name_en": "Jackal",
        "name_or": "Yeeyyii",
        "description_en": (
            "A small wild canine that feeds on a wide "
            "variety of animals and plant material."
        ),
        "description_or": (
            "Yeeyyiin bineensa saree fakkaatu xiqqaa ta'ee, "
            "bineensota adda addaa fi biqiltoota garaagaraa nyaata."
        ),
        "image": "images/jackal.jpg"
    },
    {
        "name_en": "Anubis Baboon",
        "name_or": "Jaldeessa Anubis",
        "description_en": (
            "A social primate that lives in groups and is "
            "adapted to a variety of habitats."
        ),
        "description_or": (
            "Jaldeessi Anubis bineensa gareedhaan jiraatu "
            "ta'ee, naannolee jireenyaa garaagaraatti madaqa."
        ),
        "image": "images/anubis_baboon.jpg"
    },
    {
        "name_en": "Colobus Monkey",
        "name_or": "Weennii",
        "description_en": (
            "A tree-dwelling monkey that feeds largely "
            "on leaves and other plant material."
        ),
        "description_or": (
            "Weenniin bineensa mukarra jiraatu ta'ee, "
            "baay'inaan baala fi biqiltoota biroo nyaata."
        ),
        "image": "images/colobus_monkey.jpg"
    },
    {
        "name_en": "Ethiopian Wolf",
        "name_or": "Jeedala diimaa",
        "description_en": (
            "A rare Ethiopian carnivore that mainly feeds "
            "on rodents and lives in highland habitats."
        ),
        "description_or": (
            "Jeedalli diimaan bineensa Itoophiyaa keessatti "
            "baay'ee muraasa ta'ee, baay'inaan bineensota "
            "xixiqqoo akka hantuutaa nyaata fi naannoo "
            "lafa olka'aa keessa jiraata."
        ),
        "image": "images/ethiopian_wolf.jpg"
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
        title_text = "🦁 Wild Animals of Chilimo Forest"
        subtitle_text = (
            "Wild animal species found in and around Chilimo Forest"
        )
    else:
        title_text = "🦁 Bineensota Bosaa Bosona Chilimoo"

        subtitle_text = (
            "Gosoota bineensota bosaa Bosona Chilimoo fi "
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
    animals_frame = tk.Frame(
        canvas,
        bg="#e8f5e9"
    )
    canvas_window = canvas.create_window(
        (0, 0),
        window=animals_frame,
        anchor="nw"
    )
    def update_scroll(event=None):
        canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    animals_frame.bind(
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
    for number, animal in enumerate(animals, start=1):
        animal_frame = tk.Frame(
            animals_frame,
            bg="white",
            bd=1,
            relief="solid"
        )
        animal_frame.pack(
            fill="x",
            padx=30,
            pady=8
        )
        image_frame = tk.Frame(
            animal_frame,
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
            animal["image"]
        )
        print(
            "Loading:",
            animal["name_en"],
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
                    animal["name_en"],
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
            animal_frame,
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
            animal_name = animal["name_en"]
            second_name = (
                f"Afaan Oromoo: {animal['name_or']}"
            )
            description = animal["description_en"]
        else:
            animal_name = animal["name_or"]
            second_name = (
                f"Maqaa Ingilizii: {animal['name_en']}"
            )
            description = animal["description_or"]
        name_label = tk.Label(
            info_frame,
            text=f"{number}. {animal_name}",
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