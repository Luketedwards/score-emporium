  //on load
  $(document).ready(function () {
      // on screen resize if #rotate display is not none reload page and scroll to top
      $(window).resize(function () {
          if ($("#rotate").css("display") != "none") {
              location.reload();
              $(document).ready(function () {
                  $(window).scrollTop(0);
                  $("body").css("overflow", "hidden");
              });

          } else {
              $("body").css("overflow-y", "scroll");
          }
      });

      // if #rotate display is not none disable scroll
        if ($("#rotate").css("display") != "none") {
            $("body").css("overflow", "hidden");
        } else {
            $("body").css("overflow-y", "scroll");
        }
  });