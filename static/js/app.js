
$(document).ready(function(){
  // when hovering purchased-img class, change overflow to visible on purchased-details
$(".purchased-img").mouseover(function(){
  $("#purchased-details").css("overflow-y", "visible");
  $('.purchased-img').css("z-index", "1");
  
}).mouseleave(function(){
  setTimeout(function(){
    $("#purchased-details").css("overflow-y", "scroll");
    
 }, 200);
  
});



    document.getElementById('data-target0').className = 'active';
  document.getElementById('carousel-item0').className = 'carousel-item active';
  $("#carousel-item0").addClass("active");
  $('#myModal').modal('show');  

  

  var observer = new IntersectionObserver(function(entries) {
    // isIntersecting is true when element and viewport are overlapping
    // isIntersecting is false when element and viewport don't overlap
    if(entries[0].isIntersecting === true)
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
  }, { threshold: [0] });
  
  observer.observe(document.querySelector(".graphs"));

  /* code for converting star rating to input value of review*/

  document.getElementById('rating-5-click').addEventListener('click', rating5);
  document.getElementById('rating-4-click').addEventListener('click', rating4);
   document.getElementById('rating-3-click').addEventListener('click', rating3);
   document.getElementById('rating-2-click').addEventListener('click', rating2);
   document.getElementById('rating-1-click').addEventListener('click', rating1);
   document.getElementById('reviewSubmit').addEventListener('click', chooseRating);
  var ratingNumber = document.getElementById('hidden-rating');
  function rating5(){
  ratingNumber.value='5';
  console.log('it worked');
  }
  function rating4(){
  ratingNumber.value='4';
  console.log('it worked');
  
  }
  function rating3(){
  ratingNumber.value='3';
  console.log(ratingNumber.value);
  
  
  }
  function rating2(){
  ratingNumber.value='2';
  console.log('it worked');
  
  }
  function rating1(){
  ratingNumber.value='1';
  console.log('it worked js');
  
  }
  function chooseRating(){
    if (ratingNumber.value == ''){
      alert("Please choose a star rating")
    }
  }
});
$('.carousel').carousel({
    interval: 100000,
    pause: "false"
  });

  $(".product").hover(function(){
    $(this).toggleClass("is-active");
  });
  

  
  const example5 = document.getElementById('commentBox');
  const example5sb = document.querySelector('#commentBox .scrollbox');
  let example5IsScrolling = false;
  
  function setFade(event) {
    if (!example5IsScrolling) {
      window.requestAnimationFrame(function() {
        if (event.target.scrollTop < 160) {
          example5.classList.add('show-icon');
        }
        else {
          example5.classList.remove('show-icon');
        }
        example5IsScrolling = false;
      });
      example5IsScrolling = true;
    }
  }
  
  example5sb.addEventListener('scroll', setFade);

