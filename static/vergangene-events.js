document.addEventListener('DOMContentLoaded', function() {
    const galleryImgs = document.querySelectorAll('.gallery-img');

    galleryImgs.forEach(img => {
        img.addEventListener("click", function() {
            // Scrolling disablen
            document.body.style.overflow = 'hidden';

            // lightbox mit angeklicktem img zeigen
            const lightbox = document.getElementById('lightbox');
            lightbox.style.display = 'grid';

            const lightboxImg = document.getElementById('lightbox-img');
            lightboxImg.src = img.src;

            // close Button Funktionalität geben
            const closeBtn = document.getElementById('lightbox-close');
            closeBtn.addEventListener("click", function() {
                lightbox.style.display = 'none';
                document.body.style.overflow = 'visible';
            })
        }); 
    });
});