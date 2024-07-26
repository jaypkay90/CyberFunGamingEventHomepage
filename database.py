'''Methoden zum Interagieren mit der Datenbank'''

def insertUserIntoDB(userData, db):
    '''Daten für die Datenbank vorbereiten'''
    # Turnier darf bei Silver Pass nicht ausgewählt werden
    if userData['ticket-select'] == 'silverPass':
        userData['turnier-select'] = 'None'

    # Ticketname für Datenbank anpassen
    ticketNames = {
        'silverPass': 'Silver Pass',
        'goldPass': 'Gold Pass',
        'groupGoldPass': 'Group Gold Pass'
    }
    userData['ticket-select'] = ticketNames[userData['ticket-select']]

    # Newsletter Feld für Datenbank anpassen
    if userData['newsletter'] == 'on':
        userData['newsletter'] = 'Ja'
    else:
        userData['newsletter'] = 'Nein'

    
    '''Daten in Datenbank schreiben'''
    db.execute("INSERT INTO registrations (vorname, nachname, plz, ort, strasse, hausnummer, email, telefon, altersgruppe, ticket, turnier, newsletter) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", userData['vorname'], userData['nachname'], userData['plz'], userData['ort'], userData['strasse'], userData['hausnummer'], userData['mail'], userData['telefon'], userData['altersgruppe'], userData['ticket-select'], userData['turnier-select'], userData['newsletter'])