$(document).ready(function () {
    // when .job-item is hovered, make the .job-social2 li opacity 0 for that specific job-item
    $(".job-item").mouseover(function () {
        $(this).find(".job-social2 li").css("opacity", "0");
        $(this).find(".accept-div").css("opacity", "1");
        $(this).find(".buttons-row").css("opacity", "1");
        $(this).find(".buttons-row").css("pointer-events", " auto");
        $(this).find(".links").css("visibility", "visible");
        // when #vendor-link opacity is 1, background-color is #fff, color is #f1592a, border is white

        $(this).find("#vendor-link span").css("background-color", "#fff");
        $(this).find("#vendor-link span").css("color", "#f1592a");
        $(this).find("#vendor-link span").css("border", "1px solid #fff");
        $(this).find(".time").css("opacity", "1 !important");
        $(this).find(".time").css('background-color', 'transparent');
        $(this).find("#card-date").css("visibility", "hidden");


    }).mouseleave(function () {
        $(this).find(".job-social2 li").css("opacity", "1");
        $(this).find(".buttons-row").css("opacity", "0");
        $(this).find(".buttons-row").css("pointer-events", "none !important");
        $(this).find("#vendor-link span").css("background-color", "#f1592a");
        $(this).find("#vendor-link span").css("color", "#fff");
        $(this).find("#vendor-link span").css("border", "1px solid #f1592a");
        $(this).find("#card-date").css("visibility", "visible");
        $(this).find(".time").css('background-color', '#fff');
        $(this).find(".accept-div").css("opacity", "0");
        $(this).find(".links").css("visibility", " hidden");

    });

});