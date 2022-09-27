$(document).ready(function () {
    const example5 = document.getElementById('commentBox');
    const example5sb = document.querySelector('#commentBox .scrollbox');
    let example5IsScrolling = false;

    function setFade(event) {
        if (!example5IsScrolling) {
            window.requestAnimationFrame(function () {
                if (event.target.scrollTop < 160) {
                    example5.classList.add('show-icon');
                } else {
                    example5.classList.remove('show-icon');
                }
                example5IsScrolling = false;
            });
            example5IsScrolling = true;
        }
    }

    example5sb.addEventListener('scroll', setFade);

    // when hovering #hero-text apply hover to .overlay-hero
    $("#hero-text").mouseover(function () {
        $(".overlay-hero").css("opacity", "0.7");
    }).mouseleave(function () {
        $(".overlay-hero").css("opacity", "0.9");
    });

});