/* This code is used for a scroll to top button that is hidden until you scroll

window.addEventListener('scroll', function () {
    let backToTopButton = document.getElementById('backToTopButton');
    if (window.scrollY > 700){
        backToTopButton.classList.add("show");
    }else{
        backToTopButton.classList.remove("show");
    }
});*/

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('backToTopButton').addEventListener('click', function () {
        window.scrollTo({top: 0, behavior: 'smooth'});
    });
});
