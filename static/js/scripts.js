$( document ).ready(function() {
    
    $(".about-card")
        .mouseenter(function() {
            $(".about-title", this).animate({
            	padding: 0            
            }, 500);
            $(".about-text", this).animate({
            	height: "toggle"              
            }, 500);
            $(this).addClass("darkgreen-bg")
        })
        .mouseleave(function() {
            $(".about-title", this).animate({
            	padding: "2.5rem 0"            
            }, 500);
            $(".about-text", this).animate({
            	height: "toggle"              
            }, 500);
            $(this).removeClass("darkgreen-bg")
        });
    
});