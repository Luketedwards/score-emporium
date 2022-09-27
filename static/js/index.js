$(document).ready(function () {


    // when hovering #hero-text apply hover to .overlay-hero
    $("#hero-text").mouseover(function () {
        $(".overlay-hero").css("opacity", "0.7");
    }).mouseleave(function () {
        $(".overlay-hero").css("opacity", "0.9");
    });

});