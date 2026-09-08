current_language = "english"
translations = {
    "home": {
        "english": "Home",
        "oromo": "Mana"
    },
    "history": {
        "english": "History",
        "oromo": "Seenaa"
    },
    "animals": {
        "english": "Wild Animals",
        "oromo": "Bineensota"
    },
    "birds": {
        "english": "Birds",
        "oromo": "Simbirroota"
    },
    "plants": {
        "english": "Plants",
        "oromo": "Biqiltoota"
    },
    "attractions": {
        "english": "Attractions",
        "oromo": "Hawwata"
    },
    "location": {
        "english": "Location",
        "oromo": " Bakka"
    },
    "about": {
        "english": "About",
        "oromo": "Waa'ee"
    },
    "exit": {
        "english": "Exit",
        "oromo": "Ba'i"
    },
    "language": {
        "english": "Language",
        "oromo": "Afaan"
    },
    "english": {
        "english": "English",
        "oromo": "English"
    },
    "oromo": {
        "english": "Afan Oromo",
        "oromo": "Afaan Oromoo"
    },
    "title": {
        "english": "🌳 CHILIMO FOREST",
        "oromo": "🌳 BOSONA CHILIMOO"
    },
    "visitor_system": {
        "english": "Chilimo Forest Visitor Information System",
        "oromo": "Sirna Odeeffannoo Daawwattoota Bosona Chilimoo"
    },
    "exit_message": {
        "english": "Are you sure you want to exit?",
        "oromo": "Dhugumaan ba'uu barbaaddaa?"
    },
    "yes": {
        "english": "Yes",
        "oromo": "Eeyyee"
    },
    "no": {
        "english": "No",
        "oromo": "Lakki"
    },
    "back": {
        "english": "Back",
        "oromo": "Duubatti"
    },
    "next": {
        "english": "Next",
        "oromo": "Itti Aanu"
    },
    "previous": {
        "english": "Previous",
        "oromo": "Kan Duraa"
    },
    "read_more": {
        "english": "Read More",
        "oromo": "Dabalataan Dubbisi"
    },
    "description": {
        "english": "Description",
        "oromo": "Ibsa"
    },
    "name": {
        "english": "Name",
        "oromo": "Maqaa"
    },
    "no_image": {
        "english": "No Photo",
        "oromo": "Suurri Hin Jiru"
    },
    "image_error": {
        "english": "Image Error",
        "oromo": "Dogoggora Suuraa"
    }
}
def change_language(lang):
    global current_language
    if lang in ("english", "oromo"):
        current_language = lang
def get_language():
    return current_language
def get_text(key):
    if key not in translations:
        return key
    return translations[key].get(
        current_language,
        translations[key]["english"]
    )
def is_english():

    return current_language == "english"
def is_oromo():
    return current_language == "oromo"
