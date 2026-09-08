import tkinter as tk
import language
history_text_en = """
KBA STATUS
Confirmed
Year of last assessment:
2011
National site name:
Chilimo-Gaji Forest
Central coordinates:
Latitude: 9.0900
Longitude: 38.1690
System:
Terrestrial
Elevation:
2,300 to 3,000 meters

Area of KBA:
239.41351 km²

KBA Classification:
Global/Regional TBD

Legacy Site:
Yes


SITE DETAILS
------------

Chilimo Forest is located in the Western Shoa Zone, close to Ghinchi town,
the capital of Dendi District, approximately 90 km west of Finfine.

The area is at the western end of a chain of hills and ridges that stretches
approximately 200 km from north of Addis Ababa westwards to the Ghedo Highlands.
River valleys and gorges cut through the hills.

Chilimo Forest is one of the few remaining remnants of dry Afro-montane forest
on the Ethiopian Central Plateau.

The vegetation in this area has been subject to human impact for more than
2,000 years. The rate of deforestation has been extremely high, with significant
changes in forest cover observed since the 1970s.

The forest is montane mixed broadleaf-coniferous forest, although conifers
predominate.

The main canopy species include:

• Juniperus procera
• Podocarpus falcatus
• Prunus africana
• Olea europaea cuspidata
• Apodytes dimidiata
• Ficus species

Historically, the entire upland area is thought to have been covered by
Juniperus-Podocarpus forest. However, much of the forest has been cleared
for agriculture, and this encroachment continues.

Selective cutting of trees for commercial use stopped around 1973, but
illegal cutting by local people continues.

Various types of shrubland now dominate parts of the landscape.

The forest is also important to local communities for grazing livestock.

Some shrub species are particularly common, including Myrsine africana.
Other species, such as Maytenus arbutifolia and Rubus apetalus, are abundant
indicators of forest disturbance.

Small patches of plantation forest, initiated by the State Forestry Department
in 1976, are also present.

Both indigenous and exotic tree species have been planted.

Important exotic species include:

• Eucalyptus saligna
• Eucalyptus camaldulensis
• Pinus patula
• Cupressus lusitanica

Indigenous plantation species include:

• Juniperus procera
• Hagenia abyssinica
• Podocarpus falcatus

Chilimo Forest is threatened by excessive exploitation and conversion
to other land uses.


WHY CHILIMO FOREST IS IMPORTANT
--------------------------------

Chilimo Forest qualifies as a Key Biodiversity Area (KBA) of international
significance because it meets one or more established criteria and thresholds
for identifying sites of biodiversity importance.

The KBA identification was part of the process of compiling the CEPF
Ecosystem Profile of the East Afromontane Hotspot.

Species taxonomy and threat categories were based on the IUCN Red List
2010-4.

BIODIVERSITY
------------
A total of approximately 150 bird species has been recorded at the site.
Five of these are Ethiopian endemic species, and many others are species
associated with the Afrotropical Highlands biome.
Important bird species recorded at Chilimo Forest include:
• Bostrychia carunculata
• Agapornis taranta
• Tauraco leucotis
• Lybius undatus
• Zoothera piaggiae
• Pseudoalcippe abyssinica
• Parophasma galinieri
• Parus leuconotus
• Oriolus monacha
• Corvus crassirostris
• Poeoptera stuhlmanni
• Onychognathus tenuirostris
• Cinnyricinclus sharpii
• Cryptospiza salvadorii
• Serinus nigriceps

Other important birds include:
• Accipiter melanoleucus
• Accipiter tachiro
• Buteo buteo
• Buteo oreophilus
• Aquila pomarina
• Aquila verreauxii
• Kaupifalco monogrammicus
• Stephanoaetus coronatus

NON-BIRD BIODIVERSITY
---------------------
The endemic Tragelaphus scriptus meneliki occurs in the area.
The forest also supports a significant number of Afro-montane endemic
tree and shrub species.

Ethiopian endemic plants include:
• Erythrina brucei
• Acanthus sennii

DELINEATION
-----------
On 10 July 2013, following the CEPF East Afromontane ecosystem profiling
process, the reported IBA area of 2,400 ha was changed to approximately
24,000 ha based on GIS measurements from the latest boundary polygon.

HABITATS
--------
Land uses include:
• Agriculture
• Forestry
• Nature conservation and research
• Water management
IUCN Habitat:
Forest
Coverage:
100%
THREATS
-------
Chilimo Forest was heavily exploited during the 1940s.

There were approximately six sawmills in the area, including sawmills at
Jumjum, Gaji, Bejiro and Chilimo.

As a consequence, very little forest remains at some of these sites except
for Chilimo and part of Gaji.

In 1982, a large area including Chilimo, nearby Gaji Forest and surrounding
woodlands was designated as a Chilimo-Gaji National Forest Priority Area.

However, conversion of forest to other land uses and illegal cutting of
trees for local use and timber remain major threats.

In 1982, the forest area was surveyed at approximately 22,000 ha.

A later inventory in the late 1990s by the Forest Inventory Team of the
Oromiya Natural Resources Development and Environmental Protection (NRDEP)
Bureau suggested that the total area had been reduced to approximately
12,000 ha.

Comparison of aerial photographs from 1980 and 1994 also revealed a loss
of approximately 50% of forested land.

The actual forest cover of the Chilimo area was reported as approximately
2,400 ha.

REFERENCES
----------
• Demel (1996)
• Ethiopian Wildlife and Natural History Society Survey Team (1996)
• FARM Africa (1996)
• Tadesse (1998)
• Tadesse et al. (1999)
• Tamrat (1993, 1994)
• Zerihun and Backäus (1991)
"""
history_text_or = """
HAALA KBA
----------
Mirkanaa'e

Waggaa madaallii dhumaa:
2011

Maqaa bakka biyyaalessaa:
Bosona Chilimoo-Gaajii

Qindoomina giddugaleessaa:
Latitude: 9.0900
Longitude: 38.1690

Sirna:
Lafa irratti hundaa'e

Olka'iinsa:
Meetira 2,300 hanga 3,000

Bal'ina KBA:
239.41351 km²

Ramaddii KBA:
Global/Regional TBD
Bakka durii:
Eeyyee

IBSA BAKKAA
-----------
Bosonni Chilimoo Godina Shawaa Lixaa keessatti, magaalaa Ginciitti dhihoo,
magaalaa guddoo Aanaa Dandii, Finfinnee irraa gara dhihaatti tilmaamaan
kiiloo meetira 90 fagaatee argama.
Naannoon kun dhuma dhihaa sansalata tulluu fi gaara dheerina tilmaamaan
kiiloo meetira 200 qabu irratti argama. Sansalati kun kaaba Finfinnee irraa
gara dhihaatti hanga Baddaa Ghedoo diriira.
Sululawwan lagaa fi qoorawwan tulluuwwan kana keessa darbu.

Bosonni Chilimoo haftee bosona Afro-montane gogaa kan Baha Afrikaa keessatti
argamu keessaa tokko ta'ee, Dirree Olka'aa Itoophiyaa keessatti bakka
muraasa hafan keessaa isa tokko.

Biqiltoonni naannoo kanaa waggoota 2,000 olf darbe keessatti dhiibbaa namaa
jala turaniiru.

Saffisni bosona mancaasuu baay'ee olka'aa ture. Keessumaa bara 1970moota
irraa eegalee jijjiiramni guddaan haguuggii bosonaa irratti mul'ateera.

Bosonni kun bosona gaaraa makaa baala bal'aa fi muka qoree qabuudha.
Haa ta'u malee, mukoonni qoree baay'inaan argamu.

Gosoonni muka gubbaa bosonaa keessaa ijoo:

• Juniperus procera
• Podocarpus falcatus
• Prunus africana
• Olea europaea cuspidata
• Apodytes dimidiata
• Gosoota Ficus

Seenaa keessatti, naannoon olka'aan kun guutummaan guutuutti bosona
Juniperus-Podocarpus tiin haguugamee ture jedhamee yaadama.

Haa ta'u malee, bosona keessaa baay'een isaa qonnaaf qulqulleeffameera.
Qonnaaf babal'achuun ammas itti fufeera.

Muka daldalaaf muruu filachuun naannoo bara 1973tti dhaabbateera.
Garuu, namoonni naannoo sanaa seeraan ala muka muruu isaanii itti fufaniiru.

Gosoonni bosonaa xiqqaa adda addaa amma kutaa lafa sanaa irratti
baay'inaan mul'atu.

Bosonni kun hawaasa naannoof horii dheedhisiisuufis barbaachisaadha.
Gosoonni biqiltootaa muraasni, Myrsine africana dabalatee, baay'ee
argamu.
Gosoonni akka Maytenus arbutifolia fi Rubus apetalus immoo mallattoo
bosonni miidhamuu isaanii agarsiisan.
Kutaan bosona dhaabaa xiqqaan bara 1976tti Kutaan Bosonaa Mootummaa
jalqabsiise ammas ni jira.
Muka biyya keessaa fi muka biyya alaa irraa dhufan lamaan isaanii
dhaabamaniiru.
Gosoota muka biyya alaa keessaa:
• Eucalyptus saligna
• Eucalyptus camaldulensis
• Pinus patula
• Cupressus lusitanica

Gosoota muka biyya keessaa keessaa:
• Juniperus procera
• Hagenia abyssinica
• Podocarpus falcatus
Bosonni Chilimoo itti fayyadama humnaa ol, mancaatii fi gara itti
fayyadama lafa biraatti jijjiiramuu irraa balaadhaaf saaxilamaa jira.

MAALIIF BOSONNI CHILIMOO BARBAACHISAA DHA?
-------------------------------------------
Bosonni Chilimoo akka Key Biodiversity Area (KBA), jechuun Bakka
Barbaachisaa Garaagarummaa Lubbu-qabeeyyii, sadarkaa idil-addunyaa irratti
barbaachisaa ta'etti ramadama.
Kunis ulaagaalee fi daangaa beekamoo garaagarummaa lubbu-qabeeyyii
eeguuf barbaachisan keessaa tokko ykn isaa ol waan guutuufi.
Mirkaneessi KBA kun adeemsa qophii East Afromontane Hotspot keessatti
CEPF Ecosystem Profile qopheessuu keessaa tokko ture.
Ramaddiin gosoota lubbu-qabeeyyii fi sadarkaan balaa isaanii
IUCN Red List 2010-4 irratti hundaa'e.

GARAAGARUMMAA LUBBU-QABEEYYII
-----------------------------
Bakki kun tilmaamaan gosoota simbirroo 150 qaba.
Isaan keessaa shan gosoota Itoophiyaa keessatti qofa argamaniidha.
Gosoonni biroon hedduun ammoo Afrotropical Highlands biome waliin
walqabatu.
Gosoota simbirroo barbaachisoo Chilimoo keessatti galmaa'an keessaa:
• Bostrychia carunculata
• Agapornis taranta
• Tauraco leucotis
• Lybius undatus
• Zoothera piaggiae
• Pseudoalcippe abyssinica
• Parophasma galinieri
• Parus leuconotus
• Oriolus monacha
• Corvus crassirostris
• Poeoptera stuhlmanni
• Onychognathus tenuirostris
• Cinnyricinclus sharpii
• Cryptospiza salvadorii
• Serinus nigriceps

Simbirroota barbaachisoo biroo:
• Accipiter melanoleucus
• Accipiter tachiro
• Buteo buteo
• Buteo oreophilus
• Aquila pomarina
• Aquila verreauxii
• Kaupifalco monogrammicus
• Stephanoaetus coronatus


GARAAGARUMMAA LUBBU-QABEEYYII SIMBIRROO ALAA
--------------------------------------------
Tragelaphus scriptus meneliki, kan naannoo kana keessatti uumamaan
argamu, jira.
Bosonni kun gosoota muka fi biqiltoota xiqqaa Afro-montane keessatti
qofa argaman hedduus ni deeggera.
Biqiltoota Itoophiyaa keessatti qofa argaman keessaa:
• Erythrina brucei
• Acanthus sennii

DAANGESSUU
----------
Guyyaa 10 Adoolessa 2013, adeemsa qophii East Afromontane ecosystem
CEPF hordofuun, bal'inni IBA duraan hektara 2,400 jedhamee gabaafame
gara tilmaamaan hektara 24,000tti jijjiirame.
Jijjiiramni kun safartuu GIS daangaa haaraa irratti hundaa'e.

BAKKAWWAN JIREENYAA
--------------------
Itti fayyadamni lafaa:
• Qonna
• Bosona
• Eegumsa uumamaa fi qorannoo
• Bulchiinsa bishaanii
IUCN Habitat:
Bosona
Uwwisa:
100%

BALAWWAN
--------
Bosonni Chilimoo bara 1940moota keessa haalaan itti fayyadamaa ture.
Naannoo sana keessa mana muka itti sawan gara jaha turan.
Isaan keessaa Jumjum, Gaajii, Bejiroo fi Chilimoo keessatti argamu turan.
Kana irraa kan ka'e, bakka tokko tokko Chilimoo fi kutaa Gaajii malee
bosonni baay'ee xiqqoo hafe.

Bara 1982tti naannoon bal'aan Chilimoo, Bosona Gaajii fi lafa mukaa
naannoo isaa dabalatee, Chilimo-Gaji National Forest Priority Area
jedhamee ramadame.
Haa ta'u malee, bosona gara itti fayyadama lafa biraatti jijjiiruu fi
muka naannoo fi daldalaaf seeraan ala muruu ammas balaa guddaa dha.
Bara 1982tti bal'inni bosonaa tilmaamaan hektara 22,000 ture.
Qorannoon bara 1990moota dhuma keessa taasifame akka agarsiisutti,
bal'inni kun gara hektara 12,000tti hir'ateera.
Suuraawwan qilleensaa bara 1980 fi 1994 walbira qabuunis,
lafa bosonaa tilmaamaan dhibbeentaa 50 akka bade agarsiiseera.
Haguuggiin bosonaa naannoo Chilimoo keessatti dhumaa irratti
tilmaamaan hektara 2,400 jedhamee gabaafameera.

WABIILEE
--------

• Demel (1996)
• Ethiopian Wildlife and Natural History Society Survey Team (1996)
• FARM Africa (1996)
• Tadesse (1998)
• Tadesse et al. (1999)
• Tamrat (1993, 1994)
• Zerihun and Backäus (1991)
"""
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
        title_text = "🌳 History of Chilimo Forest"
        subtitle_text = (
            "History, biodiversity, habitat and "
            "conservation information"
        )
        history_text = history_text_en
    else:
        title_text = "🌳 Seenaa Bosona Chilimoo"
        subtitle_text = (
            "Seenaa, garaagarummaa lubbu-qabeeyyii, "
            "bakkawwan jireenyaa fi odeeffannoo eegumsa bosonaa"
        )
        history_text = history_text_or
    header_frame = tk.Frame(
        main_frame,
        bg="#e8f5e9"
    )
    header_frame.pack(
        fill="x",
        padx=30,
        pady=(15, 5)
    )
    title = tk.Label(
        header_frame,
        text=title_text,
        font=("Arial", 26, "bold"),
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
        pady=(0, 10)
    )
    scroll_frame = tk.Frame(
        main_frame,
        bg="#e8f5e9"
    )
    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=40,
        pady=10
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

    
    history_frame = tk.Frame(
        canvas,
        bg="white"
    )
    canvas_window = canvas.create_window(
        (0, 0),
        window=history_frame,
        anchor="nw"
    )
    history_box = tk.Label(
        history_frame,
        text=history_text,
        font=("Arial", 12),
        bg="white",
        fg="#333333",
        justify="left",
        anchor="nw",
        padx=35,
        pady=30,
        wraplength=900
    )
    history_box.pack(
        fill="both",
        expand=True
    )
    def update_scroll(event=None):

        canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    history_frame.bind(
        "<Configure>",
        update_scroll
    )
    def resize_frame(event):
        canvas.itemconfig(
            canvas_window,
            width=event.width
        )
        history_box.config(
            wraplength=max(
                event.width - 70,
                400
            )
        )
    canvas.bind(
        "<Configure>",
        resize_frame
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