
$(document).ready(function(){
    document.getElementById('data-target0').className = 'active';
  document.getElementById('carousel-item0').className = 'carousel-item active';
  $("#carousel-item0").addClass("active");
  $('#myModal').modal('show');  
});
$('.carousel').carousel({
    interval: 100000,
    pause: "false"
  });


