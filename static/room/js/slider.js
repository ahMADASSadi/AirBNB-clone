
document.addEventListener('DOMContentLoaded', function () {
    const sliders = document.querySelectorAll('.slider');
    sliders.forEach((slider) => {
        let index = 0;
        const images = slider.querySelectorAll('img');

        setInterval(() => {
            images.forEach((img, i) => {
                img.style.transform = `translateX(-${index * 100}%)`;
            });
            index = (index + 1) % images.length;
        }, 300);  // Change image every 3 seconds
    });
});
