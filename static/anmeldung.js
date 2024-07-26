document.addEventListener('DOMContentLoaded', function() {
    const ticketSelect = document.getElementById('ticket-select');

    // Seite wurde gerade aufgerufen -> Welches Ticket ist ausgewählt? -> Notwendig, wenn Form mit inkorrekten Daten übermittelt wurde
    updateElementsAccordingToTicket(ticketSelect.value)

    // Eventlistener -> Notwendig, wenn User die Ticketauswahl ändert
    ticketSelect.addEventListener('change', function() {
        updateElementsAccordingToTicket(this.value);
    });

    // Roter Border für Felder, bei denen ein Error aufgetreten ist, wenn die Form mit inkorrekten Daten übermittelt wurde
    if (errorFields.length != 0) {
        errorFields.forEach(element => {
            document.getElementById(element).classList.add('border-error');
        })
        document.getElementById('error-message').style.display = 'block';
    }

    // Submitten des Formulars mit ungültigen Daten unterdrücken
    const registrationForm = document.getElementById('anmeldung-form');
    registrationForm.addEventListener('submit', function(event) {
        event.preventDefault();
        checkInputValidity();
    })

    function checkInputValidity() {
        // Array mit allen input und select Elementen
        const formElements = Array.from(registrationForm.querySelectorAll('input, select'));

        // Submitbutton aus dem Array entfernen
        if (formElements[formElements.length - 1].classList.contains('registration-submit')) {
            formElements.pop();
        }

        // Für jedes Element im Array: Wenn nicht valide ausgefüllt, roten Border hinzufügen
        let firstErrorElement = null;
        formElements.forEach(element => {
            if (!element.checkValidity()) {
                element.classList.add('border-error');

                if (!firstErrorElement) {
                    firstErrorElement = element;
                }
            }
            else {
                element.classList.remove('border-error');
            }
        });

        // Wenn min. ein Error-Element gefunden: errorMessage anzeigen, zum ersten Error-Element scrollen
        if (firstErrorElement) {
            document.getElementById('error-message').style.display = 'block';
            firstErrorElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        else {
            registrationForm.submit();
        }
    }

    function  updateElementsAccordingToTicket(selectedTicket) {
        // Turnierauswahl div soll nur bei Gold Pass und Group Gold Pass sichtbar sein
        // Preis soll entsprechend des Tickets angepasst werden
        const tournamentSelectFieldset = document.getElementById('turnier-select-fieldset');
        const ticketPriceTag = document.getElementById('ticket-price-tag');

        if (selectedTicket === 'silverPass') {
            tournamentSelectFieldset.style.display = 'none';
            ticketPriceTag.textContent = 'nur € 50';
            return;
        }

        tournamentSelectFieldset.style.display = 'block';
        if (selectedTicket === 'goldPass') {
            ticketPriceTag.textContent = 'nur € 80';
        }
        else {
            ticketPriceTag.textContent = 'nur € 200'; 
        }
    }
});
