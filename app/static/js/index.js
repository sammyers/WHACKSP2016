/*
FILE NAME: index.js
WRITTEN BY: Table 20
DATE: 2/16/2015
PURPOSE: JS for Index.htmml
*/

//slideshow for the frontpage.

var slides = [
    "confused.jpg",
    "idea.jpg",
    "scenery.jpg",
    "balloon.jpg"];

var currentSlideIndex = 0;


function displaySlide() {

    var filename = slides[ currentSlideIndex ];
    var url = "../static/images/" + filename;
    $("#slideshow img").attr("src", url);
    //$("#slideshow img").animate("opacity: 0.0", 2000);

}

function nextSlide() {
    currentSlideIndex++;
    if( currentSlideIndex >= slides.length ) {
        currentSlideIndex = 0;
    }

    displaySlide();
}

setInterval(nextSlide, 3000);

displaySlide;
