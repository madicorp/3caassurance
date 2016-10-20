$(".carousel").owlCarousel({
	autoplay:true,
	autoplayTimeout:3000,
	smartSpeed:2000,
	loop:false,
	dots:true,
	nav:false,
	margin:0,
	items:1,
	singleItem:true
	});

jQuery(document).ready(function(){
    "use strict";

    $(".popup-client > span").on("click", function(){
        $(".account-popup-sec").addClass("active");
        $("html").addClass("no-scroll");
    });

    $(".close-popup").on("click", function(){
        $(".account-popup-sec").removeClass("active");
        $("html").removeClass("no-scroll");
    });

    $('.menu-toggle').on("click", function(){
        $(".menu nav").slideToggle();
    });

    // Get Header Height //
    var stick = $(".simple-header.for-sticky").height();
    $(".simple-header.for-sticky").parent().css({
                                                    "padding-top": stick
                                                });


    $("header").on("click",function(e){
        e.stopPropagation();
    });
    $(".menu-item-has-children > a").on("click",function(){
        $(this).parent().siblings().children("ul").slideUp();
        $(this).parent().siblings().removeClass("active");
        $(this).parent().children("ul").slideToggle();
        $(this).parent().toggleClass("active");
        return false;
    });


    /*** FIXED Menu APPEARS ON SCROLL DOWN ***/
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll >= 50) {
            $(".for-sticky").addClass("sticky");
        }
        else{
            $(".for-sticky").removeClass("sticky");
            $("for-sticky").addClass("");
        }
    });


    /*=================== Parallax ===================*/
    $('.parallax').scrolly({bgParallax: true});

});

function submitForm(form, onEnd) {
    var url = form.action;
    var method = form.method;
    try {
        var data = Array.prototype.reduce.call(form.querySelectorAll('input[name], textarea[name]'), setFormData, {});
        var request;
        if ("post" === method) {
            request = superagent.post(url).set('X-CSRFToken', data['csrfmiddlewaretoken']);
        }
        if (request) {
            request.send(data)
                   .withCredentials()
                   .end(onEndDecorated);
        } else {
            console.error('Method ' + method + 'is not supported');
        }
    } catch (err) {
        console.error(err);
    }

    function setFormData(data, element) {
        if (element.name) {
            data[element.name] = element.value
        }
        return data;
    }

    function onEndDecorated(err, res) {
        if (err) {
            console.error(err);
        }
        onEnd(err, res);
    }
}

// Thanks to http://stackoverflow.com/questions/6121203/how-to-do-fade-in-and-fade-out-with-javascript-and-css
function fadeHiddenElement(element) {
    var op = 1;  // initial opacity
    element.style.visibility = 'visible';
    var timer = setInterval(function () {
        if (op <= 0.05){
            clearInterval(timer);
            element.style.visibility = 'hidden';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.05;
    }, 50);
}