$(document).ready(function () {



  
  // when the .menu__toggle is checked, click the navbar-toggler
$('.menu__btn').click(function () {
  if ($('.menu__btn').is(':checked')) {
    $('.menu__btn').prop('checked', false);
  } else {
    $('.menu__btn').prop('checked', true);
  }
  
  $('#nav-tog').click();
});


  $('nav').click(function(e) {
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

  // when hovering #hero-text apply hover to .overlay-hero
  $("#hero-text").mouseover(function () {
    $(".overlay-hero").css("opacity", "0.7");
  }).mouseleave(function () {
    $(".overlay-hero").css("opacity", "0.9");
  });

// // on page load all tabs apart from #tab-1 have display none
//   $(".tab-pane").not("#tab-1").css("display", "none");

//   // when #product-tab-1 is clicked, apply show and active to #tab-1 and remove from #tab-2 #tab-3 #tab-4 and #tab-5
//   $("#product-tab-1").click(function () {
//     $("#tab-1").addClass("show active");
//     $("#tab-1").show();
//     $('.simple-card .tab-content').css("padding", "12px");
//     $("#tab-2").removeClass("show active").css("display", "none");
//     $("#tab-3").removeClass("show active").css("display", "none");
//     $("#tab-4").removeClass("show active").css("display", "none");
//     $("#tab-5").removeClass("show active").css("display", "none");
//   });

//   // when #product-tab-2 is clicked, apply show and active to #tab-2 and remove from #tab-1 #tab-3 #tab-4 and #tab-5
//   $("#product-tab-2").click(function () {
//     $("#tab-2").addClass("show active");
//     $("#tab-2").show();
//     $('.simple-card .tab-content').css("padding", "12px");
//     $("#tab-1").removeClass("show active").css("display", "none");
//     $("#tab-3").removeClass("show active").css("display", "none");
//     $("#tab-4").removeClass("show active").css("display", "none");
//     $("#tab-5").removeClass("show active").css("display", "none");
//   });

//   // when #product-tab-3 is clicked, apply show and active to #tab-3 and remove from #tab-1 #tab-2 #tab-4 and #tab-5
//   $("#product-tab-3").click(function () {
//     $("#tab-3").addClass("show active");
//     $("#tab-3").show();
//     $('.simple-card .tab-content').css("padding", "0");
//     $("#tab-1").removeClass("show active").css("display", "none");
//     $("#tab-2").removeClass("show active").css("display", "none");
//     $("#tab-4").removeClass("show active").css("display", "none");
//     $("#tab-5").removeClass("show active").css("display", "none");
//   });

//   // when #product-tab-4 is clicked, apply show and active to #tab-4 and remove from #tab-1 #tab-2 #tab-3 and #tab-5
//   $("#product-tab-4").click(function () {
//     $("#tab-4").addClass("show active");
//     $("#tab-4").show();
//     $('.simple-card .tab-content').css("padding", "0");
//     $("#tab-1").removeClass("show active").css("display", "none");
//     $("#tab-2").removeClass("show active").css("display", "none");
//     $("#tab-3").removeClass("show active").css("display", "none");
//     $("#tab-5").removeClass("show active").css("display", "none");
//   });

//   // when #product-tab-5 is clicked, apply show and active to #tab-5 and remove from #tab-1 #tab-2 #tab-3 and #tab-4
//   $("#product-tab-5").click(function () {
//     $("#tab-5").addClass("show active");
//     $("#tab-1").removeClass("show active");
//     $("#tab-2").removeClass("show active");
//     $("#tab-3").removeClass("show active");
//     $("#tab-4").removeClass("show active");
//   });

  


  document.getElementById('data-target0').className = 'active';
  document.getElementById('carousel-item0').className = 'carousel-item active';
  $("#carousel-item0").addClass("active");
  $('#myModal').modal('show');

 


  var observer = new IntersectionObserver(function (entries) {
    // isIntersecting is true when element and viewport are overlapping
    // isIntersecting is false when element and viewport don't overlap
    if (entries[0].isIntersecting === true)
      $('#5bar').removeClass('empty')
    $('#5bar').addClass('full5')
    $('#4bar').removeClass('empty')
    $('#4bar').addClass('full4')
    $('#3bar').removeClass('empty')
    $('#3bar').addClass('full3')
    $('#2bar').removeClass('empty')
    $('#2bar').addClass('full2')
    $('#1bar').removeClass('empty')
    $('#1bar').addClass('full1')
  }, {
    threshold: [0]
  });

  observer.observe(document.querySelector(".graphs"));

  /* code for converting star rating to input value of review*/

  document.getElementById('rating-5-click').addEventListener('click', rating5);
  document.getElementById('rating-4-click').addEventListener('click', rating4);
  document.getElementById('rating-3-click').addEventListener('click', rating3);
  document.getElementById('rating-2-click').addEventListener('click', rating2);
  document.getElementById('rating-1-click').addEventListener('click', rating1);
  document.getElementById('reviewSubmit').addEventListener('click', chooseRating);
  var ratingNumber = document.getElementById('hidden-rating');

  function rating5() {
    ratingNumber.value = '5';
    console.log('it worked');
  }

  function rating4() {
    ratingNumber.value = '4';
    console.log('it worked');

  }

  function rating3() {
    ratingNumber.value = '3';
    console.log(ratingNumber.value);


  }

  function rating2() {
    ratingNumber.value = '2';
    console.log('it worked');

  }

  function rating1() {
    ratingNumber.value = '1';
    console.log('it worked js');

  }

  function chooseRating() {
    if (ratingNumber.value == '') {
      alert("Please choose a star rating")
    }
  }
});
$('.carousel').carousel({
  interval: 100000,
  pause: "false"
});

$(".product-card").hover(function () {
  $(this).toggleClass("is-active");
});




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



