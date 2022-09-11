
// on load scroll down 1 pixel to trigger the animation
$(document).ready(function () {
    
    $('.hideme2').each( function(i){        
        
        $(this).css({'opacity':'0.8'},900);
               
    }); 

    
    document.getElementsByTagName("body")[0].addEventListener('scroll', function(e){
        $('.hideme').each( function(i){        
                if( isInViewport(this) ) {
                    $(this).css({'opacity':'0.8'},900);
                };       
            }); 
        });      
    });

    
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    } 
    
   
    
