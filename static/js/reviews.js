$(document).ready(function () {
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