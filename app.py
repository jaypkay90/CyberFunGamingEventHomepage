from cs50 import SQL
from flask import Flask, redirect, render_template, request, url_for, session
from dotenv import load_dotenv
import os
import registration
import database

# Configure application
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

# Configure usability of SQLite database
db = SQL("sqlite:///data/registrations.db")

@app.route('/')
def index():
    return render_template("index.html", schedule_bg="bg-color4")

@app.route('/programm')
def programm():
    return render_template("programm.html", schedule_bg="bg-color1")

@app.route('/spiele')
def spiele():
    return render_template("spiele.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

@app.route('/ueber-uns')
def ueber_uns():
    return render_template("ueber-uns.html")

@app.route('/social-media')
def social_media():
    return render_template("social-media.html")

@app.route('/impressum')
def impressum():
    return render_template("impressum.html")

@app.route('/vergangene-events')
def vergangene_events():
    return render_template("vergangene-events.html")

@app.route('/anmeldung', methods=['GET', 'POST'])
def anmeldung():
    if request.method == "GET":
        return render_template("anmeldung.html", method="GET")
    
    # Formular via POST gesendet
    else:
        '''User Input aus Anmeldeform auslesen'''
        userData = {
            "vorname": request.form.get('vorname').strip(),
            "nachname": request.form.get('nachname').strip(),
            "plz": request.form.get('plz').strip(),
            "ort": request.form.get('ort').strip(),
            "strasse": request.form.get('strasse').strip(),
            "hausnummer": request.form.get('hausnummer').strip(),
            "mail": request.form.get('mail').strip(),
            "telefon": request.form.get('telefon').strip(),
            "altersgruppe": request.form.get('altersgruppe').strip(),
            "ticket-select": request.form.get('ticket-select').strip(),
            "turnier-select": request.form.get('turnier-select').strip(),
            "newsletter": request.form.get('newsletter')
        }

        '''User Input auf Validität prüfen'''
        # errorFields: Array mit allen Feldern, in denen invalider Input ist
        errorFields = registration.checkUserInputValidity(userData)

        if len(errorFields) != 0:
            return render_template("anmeldung.html", method="GET", errorFields=errorFields)

        '''Input ist valide -> User Input in DB schreiben'''
        database.insertUserIntoDB(userData, db)

        '''Bestellung erfolgreich! -> session Variable erstellen und redirect'''
        session['order_success'] = True
        return redirect(url_for('orderSuccess'))

@app.route('/bestellung-erfolgreich')
def orderSuccess():
    # Nur reachable, wenn Bestellformular gerade erfolgreich übermittelt wurde
    if not session.get('order_success'):
        return redirect(url_for('index'))
    
    # Session Variable löschen
    session.pop('order_success', None)
    return render_template("bestellung-erfolgreich.html")
