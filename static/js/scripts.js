$( document ).ready(function() {
    
    $(".about-card")
        .mouseenter(function() {
            $(".about-title", this).animate({
            	padding: 0            
            }, 400);
            $(".about-text", this).animate({
            	height: "toggle"              
            }, 400);
            $(this).addClass("darkgreen-bg");
        })
        .mouseleave(function() {
            $(".about-title", this).animate({
            	padding: "2.5rem 0"            
            }, 400);
            $(".about-text", this).animate({
            	height: "toggle"              
            }, 400);
            $(this).removeClass("darkgreen-bg");
        });
});