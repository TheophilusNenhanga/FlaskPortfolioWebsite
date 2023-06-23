// ScreenSize Block
function checkScreenSize() {
    const screenWidth = Math.min(document.body.clientWidth, window.innerWidth, document.documentElement.clientWidth);
    const warningMessage = document.getElementById('warningMessage');

    if (screenWidth < 280) {
        warningMessage.style.display = 'block';
    } else {
        warningMessage.style.display = 'none';
    }
}

window.addEventListener('resize', checkScreenSize);
checkScreenSize();


// Back to Top Button
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('backToTopButton').addEventListener('click', function () {
        window.scrollTo({top: 0, behavior: 'smooth'});
    });
});


// Knowledge Sliders
document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener("scroll", function () {
        let sliders = document.querySelectorAll(".slider, .slider-one, .slider-two, .slider-three, .slider-four");

        sliders.forEach(function (slider) {
            let sliderPosition = slider.getBoundingClientRect();
            let windowHeight = window.innerHeight;

            if (sliderPosition.top >= - 50 && sliderPosition.bottom <= windowHeight + 50) {
                slider.classList.add("active");
            }else{
                slider.classList.remove("active")
            }
        });
    });
});

