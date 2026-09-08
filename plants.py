import tkinter as tk
from PIL import Image, ImageTk
import os
import language
plants = [
    {
        "name_en": "Juniper",
        "name_or": "Gaattiraa",
        "description_en": (
            "An evergreen tree that is an important part of "
            "the highland forest ecosystem."
        ),
        "description_or": (
            "Gaattiraan muka yeroo hunda magariisaa ta'ee, "
            "sirna ikoo bosonaa lafa olka'aa keessatti gahee "
            "guddaa qaba."
        ),
        "image": "images/juniper.jpg"
    },
    {
        "name_en": "Hagenia",
        "name_or": "Heexoo",
        "description_en": (
            "A highland tree commonly associated with the "
            "forests and mountain areas of Ethiopia."
        ),
        "description_or": (
            "Heexoon muka lafa olka'aa keessatti argamu "
            "kan bosonaa fi naannolee gaarotaa Itoophiyaa "
            "keessatti beekamuudha."
        ),
        "image": "images/hagenia.jpg"
    },
    {
        "name_en": "Podocarpus",
        "name_or": "Birbirsa",
        "description_en": (
            "A large evergreen tree that can grow in highland "
            "forests and provides habitat for wildlife."
        ),
        "description_or": (
            "Birbirsi muka guddaa yeroo hunda magariisaa "
            "ta'ee, bosona lafa olka'aa keessatti guddachuu "
            "fi bineensota bosonaaaf bakka jireenyaa kennuu danda'a."
        ),
        "image": "images/podocarpus.jpg"
    },
    {
        "name_en": "African Olive",
        "name_or": "Ejersa",
        "description_en": (
            "An evergreen tree that grows in highland forests "
            "and woodlands and provides food and shelter "
            "for wildlife."
        ),
        "description_or": (
            "Ejersi muka yeroo hunda magariisaa ta'ee, "
            "bosonaa fi lafa mukaa lafa olka'aa keessatti "
            "guddatuudha. Bineensota bosonaatiif nyaataa fi "
            "bakka da'umsaa ni kenna."
        ),
        "image": "images/african_olive.jpg"
    },
    {
        "name_en": "Prunus africana",
        "name_or": "Hoomii",
        "description_en": (
            "A large evergreen tree found in mountain forests "
            "and valued for its ecological importance."
        ),
        "description_or": (
            "Hoomiin muka guddaa yeroo hunda magariisaa ta'ee, "
            "bosona gaarotaa keessatti argamuudha. Faayidaa isaa "
            "sirna ikoo keessatti qabuun baay'ee barbaachisaadha."
        ),
        "image": "images/prunus_africana.jpg"
    },
    {
        "name_en": "Bamboo",
        "name_or": "Leemmana",
        "description_en": (
            "A fast-growing plant that can form dense stands "
            "and provides shelter for many forest animals."
        ),
        "description_or": (
            "Leemmanni biqiltuu saffisaan guddatuudha. "
            "Garee cufaa uumuu fi bineensota bosonaa hedduudhaaf "
            "bakka da'umsaa fi dhokataa kennuu danda'a."
        ),
        "image": "images/bamboo.jpg"
    },
    {
        "name_en": "Wild Coffee",
        "name_or": "Buna",
        "description_en": (
            "A shrub that grows naturally in forest environments "
            "and produces coffee berries."
        ),
        "description_or": (
            "Bunni marga-muka xiqqaa ta'ee, naannoo bosonaa "
            "keessatti uumamaan guddatuu fi firii bunaas "
            "oomishuudha."
        ),
        "image": "images/wild_coffee.jpg"
    },
    {
        "name_en": "Ensete",
        "name_or": "Wesse",
        "description_en": (
            "A large herbaceous plant with broad leaves that "
            "is common in parts of the Ethiopian highlands."
        ),
        "description_or": (
            "Wesseen biqiltuu baala bal'aa qabu, guddaa fi "
            "marga fakkaatuudha. Kutaalee lafa olka'aa "
            "Itoophiyaa keessatti baay'ee argama."
        ),
        "image": "images/ensete.jpg"
    },
    {
        "name_en": "Stinging Nettle",
        "name_or": "Urtikaa",
        "description_en": (
            "A plant with fine stinging hairs that commonly "
            "grows in moist forest environments."
        ),
        "description_or": (
            "Urtikaan biqiltuu rifeensa xixiqqoo nama waraanu "
            "qabuudha. Yeroo baay'ee naannoo bosonaa jiidhaa "
            "keessatti guddatti."
        ),
        "image": "images/stinging_nettle.jpg"
    },
    {
        "name_en": "African Redwood",
        "name_or": "Sukkee",
        "description_en": (
            "A forest tree that contributes to the structure "
            "and biodiversity of highland ecosystems."
        ),
        "description_or": (
            "Sukkeen muka bosonaa ta'ee, caasaa bosonaa fi "
            "garaagarummaa lubbu-qabeeyyii sirna ikoo "
            "lafa olka'aa keessatti guddaa gumaacha."
        ),
        "image": "images/african_redwood.jpg"
    },
    {
        "name_en": "Acacia",
        "name_or": "Laaftoo",
        "description_en": (
            "A group of trees and shrubs that provide food "
            "and shelter for many animals and birds."
        ),
        "description_or": (
            "Laaftoon garee mukaatii fi marga-mukaa ta'ee, "
            "bineensotaa fi simbirroota hedduudhaaf nyaataa "
            "fi bakka da'umsaa kennu."
        ),
        "image": "images/acacia.jpg"
    },
    {
        "name_en": "Wild Fig",
        "name_or": "Odaa",
        "description_en": (
            "Odaa is a large,"
            "evergreen tree with dense,"
            "umbrella-like foliage that\n"
            " holds deep cultural,spiritual "
            " and political significance for"
            "the Oromo people of East Africa.\n"
            " Historically,the Odaa served"
            " as the central gathering place\n"
            "for the Gadaa system,and\n"
            "the traditional"
            " Oromo governance"
            "structure.\n Under its shade,"
            " members conducted"
            " political discussions,"
            "religious rituals,"
            " and social ceremonies.\n"
            "It is also the site for "
            "Muuda pilgrimages,\n"
            "promotions of Gadaa members,and\n"
            " community celebrations."
            " The tree symbolizes peace,"
            "unity,and Oromo identity,\n "
            "connecting present generations"
            " to their ancestors and\n"
            " serving as a sacred "
            "site for worship"
            "and ritual practices"
            " in the Waaqeffannaa religion."

        ),
        "description_or": (
            " Odaan muka guddaa, yeroo hunda magariisaa ta'ee,\n"
            " baala bal'aa akka gaaddisaatti diriirfamee qabuudha. \n"
            "Innis ummata Oromoo Baha Afrikaa biratti hiika aadaa,\n "
            "safuu fi siyaasaa guddaa qaba.\n"
               "  Seenaa keessatti,"
                "Odaan bakka walgaii guddaa sirna Gadaa ti.\n"
        ),
        "image": "images/wild_fig.jpg"
    },
    {
        "name_en": "Croton",
        "name_or": "Bakkanniisa",
        "description_en": (
            "A forest tree with broad leaves that grows in "
            "warm and moist woodland environments."
        ),
        "description_or": (
            "Bakkanniisaan muka baala bal'aa qabuudha. "
            "Naannoo lafa mukaa ho'aa fi jiidhaa keessatti "
            "guddatuudha."
        ),
        "image": "images/croton.jpg"
    },
    {
        "name_en": "Erythrina",
        "name_or": "Korch",
        "description_en": (
            "A flowering tree that provides nectar and habitat "
            "for birds and insects."
        ),
        "description_or": (
            "Korchaan muka daraaraa qabuudha. Simbirrootaa fi "
            "ilbiisotaaf dhangala'aa daraaraa fi bakka "
            "jireenyaa ni kenna."
        ),
        "image": "images/erythrina.jpg"
    },
    {
        "name_en": "African Rosewood",
        "name_or": "Birbirraa",
        "description_en": (
            "A native tree that contributes to forest structure "
            "and provides habitat for wildlife."
        ),
        "description_or": (
            "Birbirraan muka biyya keessaa ta'ee, caasaa "
            "bosonaa keessatti gumaacha qaba. Bineensota "
            "bosonaatiifis bakka jireenyaa ni kenna."
        ),
        "image": "images/african_rosewood.jpg"
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
        title_text = "🌳 Plants of Chilimo Forest"
        subtitle_text = (
            "Plant species found in and around Chilimo Forest"
        )
    else:
        title_text = "🌳 Biqiltoota Bosona Chilimoo"
        subtitle_text = (
            "Gosoota biqiltootaa Bosona Chilimoo fi "
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

    plants_frame = tk.Frame(
        canvas,
        bg="#e8f5e9"
    )
    canvas_window = canvas.create_window(
        (0, 0),
        window=plants_frame,
        anchor="nw"
    )
    def update_scroll(event=None):

        canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    plants_frame.bind(
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
    for number, plant in enumerate(plants, start=1):
        plant_frame = tk.Frame(
            plants_frame,
            bg="white",
            bd=1,
            relief="solid"
        )
        plant_frame.pack(
            fill="x",
            padx=30,
            pady=8
        )
        image_frame = tk.Frame(
            plant_frame,
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
            plant["image"]
        )
        print(
            "Loading:",
            plant["name_en"],
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
                    plant["name_en"],
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
            plant_frame,
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
            plant_name = plant["name_en"]
            second_name = (
                f"Afaan Oromoo: {plant['name_or']}"
            )
            description = plant["description_en"]
        else:
            plant_name = plant["name_or"]
            second_name = (
                f"Maqaa Ingilizii: {plant['name_en']}"
            )
            description = plant["description_or"]
        name_label = tk.Label(
            info_frame,
            text=f"{number}. {plant_name}",
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