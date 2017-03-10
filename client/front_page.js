
var reduce = require('lodash/reduce');

function loadFrontPage(){

   var $overlay = $('<div id="overlay"></div>');
   $overlay.click(function(){
     $overlay.empty();
     $overlay.hide();
   });


   var $image = $("<img>");
   var $iframewindow = $("<iframe>");
  //Capture the click event on a link to an image
  $("#local_certs a").click(function(event){
     event.preventDefault();
     $overlay.append($image);
     $("body").append($overlay);
     var imageLocation = $(this).attr('href');
     //Update overlay with the image linked in the link
     $image.attr("src", imageLocation);
     //Show the overlay.
     $overlay.show();
  });

  $(".edx a").click(function(event){
    event.preventDefault();
    $overlay.append($iframewindow);
    $("body").append($overlay);
    var iframeLocation = $(this).attr('href');
    // Update overlay with the image linked in the link
    $iframewindow.attr("src", iframeLocation);
    $overlay.show();
  });


  $.getJSON('https://api.github.com/users/BenRuns/events/public',
    function(data){
      //REVIEW make this into a react componet
      var html = reduce(data, function(memo, element) {
        memo += '<li>'+
          '<ul>' +
            '<li>' +
              '<img src=' + element.actor.avatar_url+'/>'+
              '<span><b> User: </b>' + element.actor.login + '</span>'+
            '</li>'+
            '<li><b> Event type: </b> ' + element.type  + '</li>'+
            '<li><b> Created: </b> ' + element.created_at + '</li>' +
          '</ul>' +
        '</li>';
        return memo;
      },'');
      $('#github-feed').append(html);
    }
   );
}


document.addEventListener("DOMContentLoaded", function() {
  loadFrontPage();
});