$(document).ready(function () {

    var observer = new IntersectionObserver(function (entries) {
        // isIntersecting is true when element and viewport are overlapping
        // isIntersecting is false when element and viewport don't overlap
        if (entries[0].isIntersecting === true)
            $('#5bar').removeClass('empty');
        $('#5bar').addClass('full5');
        $('#4bar').removeClass('empty');
        $('#4bar').addClass('full4');
        $('#3bar').removeClass('empty');
        $('#3bar').addClass('full3');
        $('#2bar').removeClass('empty');
        $('#2bar').addClass('full2');
        $('#1bar').removeClass('empty');
        $('#1bar').addClass('full1');
    }, {
        threshold: [0]
    });

    observer.observe(document.querySelector(".graphs"));

});