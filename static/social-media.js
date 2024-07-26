document.addEventListener('DOMContentLoaded', function() {
    // Social-Media Images selektieren
    const soMeLinks = document.querySelectorAll('.so-me-link > img');
    
    // Touch Device?
    const supportsTouch = 'ontouchstart' in window || navigator.maxTouchPoints > 0;

    // Touch und mouse event listeners adden, abhängig vom Gerätetyp
    soMeLinks.forEach(img => {
        if (!supportsTouch) {
            img.addEventListener('mouseover', changeImgOnHoverOrTouch);
            img.addEventListener('mouseout', changeImgOnHoverOrTouch);
        }
        else {
            img.addEventListener('touchstart', changeImgOnHoverOrTouch);
            img.addEventListener('touchend', changeImgOnHoverOrTouch);
        }
    });

    function changeImgOnHoverOrTouch(event) {
        // Aktuelle image source
        isSrc = event.currentTarget.src;

        // Wenn wir das gefüllte Image haben, soll die source auf das ungefüllte Image geändert werden
        // Ansonsten andersherum
        if (isSrc.includes('filled')) {
            shouldSrc = isSrc.slice(0, isSrc.length - 14) + '500.png';
        }
        else {
            shouldSrc = isSrc.slice(0, isSrc.length - 7) + 'filled-500.png';
        }
        event.currentTarget.src = shouldSrc;
    }
});