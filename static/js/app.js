$(document).ready(function () {

  // logic for product filter on shop page
  $('#filter-small').on('click', '.dd-button', function (e) {
    var $menu = $(this).next('.dd-menu');

    $menu.toggleClass("toggled");
    e.preventDefault();
  });

  $('#filter-small').on('click', 'label', function (e) {
    var $menu = $(this).parents('.dd-menu');
    $menu.removeClass("toggled");
    var $button = $(this).parents('.dropdown').find('.dd-button');
    $button.text($(this).text());
    $li = $(this).parent('li');
    $li.hide();
    $li.siblings().show();
  });

  $(window).click(function () {
    $('#filter-small .dd-menu').removeClass('toggled');
  });

  $('#filter-small').click(function (event) {
    event.stopPropagation();
  });

  // when the .menu__toggle is checked, click the navbar-toggler
  $('.menu__btn').click(function () {
    if ($('.menu__btn').is(':checked')) {
      $('.menu__btn').prop('checked', false);
    } else {
      $('.menu__btn').prop('checked', true);
    }

    $('#nav-tog').click();
  });


  $('nav').click(function (e) {
    if ($('.navbar-toggler').hasClass('show')) {
      $(".navbar-toggler").removeClass('show');
      $(".navbar-toggler").addClass('collapsed');
      alert('test');
    }
  })
  // when hovering purchased-img class, change overflow to visible on purchased-details
  $(".purchased-img").mouseover(function () {
    $("#purchased-details").css("overflow-y", "visible");
    $('.purchased-img').css("z-index", "1");

  }).mouseleave(function () {
    setTimeout(function () {
      $("#purchased-details").css("overflow-y", "scroll");

    }, 200);

  });

  $('#myModal').modal('show');

  // when hovering .product-card add class .is-active
  $(".product-card").hover(function () {
    $(this).toggleClass("is-active");
  });


});