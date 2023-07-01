

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
            } // else{slider.classList.remove("active")}
        });
    });
});

// ScreenSize Block
// Putting this block of code above the knowledge sliders block of code stops the knowledge sliders block of code from working.
function checkScreenSize() {
    let screenWidth = Math.min(document.body.clientWidth, window.innerWidth, document.documentElement.clientWidth);
    let screenHeight = Math.min(document.body.clientHeight, window.innerHeight, document.documentElement.clientHeight);
    let warningMessage = document.getElementById('warningMessage');

    if (screenWidth < 280 || screenWidth < 300 && screenHeight < 640) {
        warningMessage.style.display = 'block';
    } else {
        warningMessage.style.display = 'none';
    }
}

window.addEventListener('resize', checkScreenSize);
checkScreenSize();
