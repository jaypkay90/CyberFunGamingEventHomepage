'''Methoden zur Überprüfung des User-Inputs in das Registration Formular'''

import re

# Anmeldeform: Methoden zum Überprüfen der Validität des Inputs
def hasOnlyLettersAndSpaces(input):
    # Nur Buchstaben, Leerzeichen und Bindestriche erlaubt
    return bool(re.match(r'^[A-Za-zäöüÄÖÜ]+[A-Za-zäöüÄÖÜ\s\-]+$', input))

def isValidStreetName(strName):
    return bool(re.match(r'^[A-Za-zäöüÄÖÜ]+[A-Za-zäöüÄÖÜ\s\-.]+$', strName))

def isValidPlz(plz):
    # 5 Zeichen, nur Ziffern
    return bool(re.match(r'^\d{5}$', plz))

def isValidMailAddress(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

def isValidPhoneNumber(tel):
    return bool(re.match(r'^\+?\d[0-9\s\-]+$', tel))

def isValidStreetNr(strNr):
    # 1 Zahl + optional ein Buchstabe
    return bool(re.match(r'^\d+\s?[A-Za-z]?$', strNr))

def isValidAgeGroup(ageGroup):
    valid = ['16 - 30', '30 - 45', '45+', 'Keine Angabe']
    return inputInValidInputsDict(ageGroup, valid)

def isValidTicket(ticket):
    valid = ['silverPass', 'goldPass', 'groupGoldPass']
    return inputInValidInputsDict(ticket, valid)

def isValidTournament(tournament):
    valid = ['FC 24', 'Fortnite', 'Super Mario 64']
    return inputInValidInputsDict(tournament, valid)

def inputInValidInputsDict(input, valid):
    if input in valid:
        return True
    return False

def checkUserInputValidity(userData):
    # Dictionary mit keys aus dem userData Dict, Value: Methoden zur Überprüfung der Validität des Inputs
    validators = {
        'vorname': hasOnlyLettersAndSpaces(userData.get('vorname')),
        'nachname': hasOnlyLettersAndSpaces(userData.get('nachname')),
        'ort': hasOnlyLettersAndSpaces(userData.get('ort')),
        'strasse': isValidStreetName(userData.get('strasse')),
        'plz': isValidPlz(userData.get('plz')),
        'hausnummer': isValidStreetNr(userData.get('hausnummer')),
        'mail': isValidMailAddress(userData.get('mail')),
        'telefon': isValidPhoneNumber(userData.get('telefon')),
        'altersgruppe': isValidAgeGroup(userData.get('altersgruppe')),
        'ticket-select': isValidTicket(userData.get('ticket-select')),
        'turnier-select': isValidTournament(userData.get('turnier-select'))
    }
    
    # Validität prüfen
    # Array mit allen Error-Feldern
    errorFields = []
    for field, validator in validators.items():
        if validator == False:
            errorFields.append(field)

    return errorFields