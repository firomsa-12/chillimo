from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
from pathlib import Path
from content import BIRDS, PLANTS, ANIMALS, HISTORY_EN, HISTORY_OR

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder="static", static_url_path="/static")
app.secret_key = "chilimo-forest-web-app-change-this-if-needed"
@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory("images", filename)
TRANSLATIONS = {
    "title": {"en": "🌳 CHILIMO FOREST", "or": "🌳 BOSONA CHILIMOO"},
    "visitor_system": {"en": "Chilimo Forest Visitor Information System", "or": "Sirna Odeeffannoo Daawwattoota Bosona Chilimoo"},
    "home": {"en": "Home", "or": "Mana"},
    "history": {"en": "History", "or": "Seenaa"},
    "animals": {"en": "Wild Animals", "or": "Bineensota"},
    "birds": {"en": "Birds", "or": "Simbirroota"},
    "plants": {"en": "Plants", "or": "Biqiltoota"},
    "attractions": {"en": "Attractions", "or": "Hawwata"},
    "location": {"en": "Location", "or": "Bakka"},
    "about": {"en": "About", "or": "Waa'ee"},
    "language": {"en": "Language", "or": "Afaan"},
    "english": {"en": "English", "or": "English"},
    "oromo": {"en": "Afaan Oromoo", "or": "Afaan Oromoo"},
    "read_more": {"en": "Read More", "or": "Dabalataan Dubbisi"},
}

PAGE_TITLES = {
    "home": {"en": "Welcome to Chilimo Forest", "or": "Baga Gara Bosona Chilimoo Nagaan Dhuftan"},
    "history": {"en": "🌳 History of Chilimo Forest", "or": "🌳 Seenaa Bosona Chilimoo"},
    "animals": {"en": "🦁 Wild Animals of Chilimo Forest", "or": "🦁 Bineensota Bosaa Bosona Chilimoo"},
    "birds": {"en": "🐦 Birds of Chilimo Forest", "or": "🐦 Simbirroota Bosona Chilimoo"},
    "plants": {"en": "🌳 Plants of Chilimo Forest", "or": "🌳 Biqiltoota Bosona Chilimoo"},
    "attractions": {"en": "📍 Attractions of Chilimo Forest", "or": "📍 Hawwata Bosona Chilimoo"},
    "location": {"en": "Location of Chilimo Forest", "or": "Bakka Bosona Chilimoo"},
    "about": {"en": "ABOUT CHILIMO FOREST", "or": "WAA'EE BOSONA CHILIMOO"},
}

SUBTITLES = {
    "history": {"en": "History, biodiversity, habitat and conservation information", "or": "Seenaa, garaagarummaa lubbu-qabeeyyii, bakkawwan jireenyaa fi odeeffannoo eegumsa bosonaa"},
    "animals": {"en": "Wild animal species found in and around Chilimo Forest", "or": "Gosoota bineensota bosaa Bosona Chilimoo fi naannoo isaa keessatti argaman"},
    "birds": {"en": "Bird species found in and around Chilimo Forest", "or": "Gosoota simbirrootaa Bosona Chilimoo fi naannoo isaa keessatti argaman"},
    "plants": {"en": "Plant species found in and around Chilimo Forest", "or": "Gosoota biqiltootaa Bosona Chilimoo fi naannoo isaa keessatti argaman"},
}

@app.context_processor
def inject_globals():
    lang = session.get("lang", "en")
    def t(key):
        return TRANSLATIONS.get(key, {}).get(lang, key)
    return {"lang": lang, "t": t, "page_titles": PAGE_TITLES, "subtitles": SUBTITLES}

@app.get("/")
def home():
    return render_template("home.html", page="home")

@app.get("/history")
def history():
    return render_template("history.html", page="history", history_text=HISTORY_EN if session.get("lang", "en") == "en" else HISTORY_OR)

@app.get("/animals")
def animals():
    return render_template("species.html", page="animals", species=ANIMALS, icon="🦁")

@app.get("/birds")
def birds():
    return render_template("species.html", page="birds", species=BIRDS, icon="🐦")

@app.get("/plants")
def plants():
    return render_template("species.html", page="plants", species=PLANTS, icon="🌳")

@app.get("/attractions")
def attractions():
    image_names = [f"image_{i}.jpg" for i in range(1, 8)]
    image_names = [x for x in image_names if (BASE_DIR / "images" / x).is_file()]
    return render_template("attractions.html", page="attractions", image_names=image_names)

@app.get("/location")
def location():
    return render_template("location.html", page="location")

@app.get("/about")
def about():
    return render_template("about.html", page="about")

@app.get("/language/<lang>")
def set_language(lang):
    if lang in ("en", "or"):
        session["lang"] = lang
    return redirect(request.referrer or url_for("home"))

if __name__ == "__main__":
    # Local development only. Render uses Gunicorn.
    app.run(host="0.0.0.0", port=5000, debug=True)
