$(document).ready(function() {
    "use strict";

    $(".carousel").owlCarousel({
                                   autoplay:true,
                                   autoplayTimeout:3000,
                                   smartSpeed:2000,
                                   loop:false,
                                   dots:false,
                                   nav:true,
                                   margin:0,
                                   items:1,
                                   singleItem:true
                               });

    $(".carousel-client").owlCarousel({
                                          autoplay:true,
                                          autoplayTimeout:3000,
                                          smartSpeed:2000,
                                          loop:false,
                                          dots:false,
                                          nav:true,
                                          margin:30,
                                          items:5,
                                          singleItem:true,
                                          responsiveClass:true,
                                          responsive:{
                                              0:{
                                                  items:1,
                                                  nav:true
                                              },
                                              600:{
                                                  items:3,
                                                  nav:true
                                              },
                                              1000:{
                                                  items:5,
                                                  nav:true,
                                                  loop:false
                                              }
                                          }
                                      });
});