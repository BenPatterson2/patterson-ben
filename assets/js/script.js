
var $overlay = $('<div id="overlay"></div>');
var $image = $("<img>");
var $iframewindow = $("<iframe>")
var $blog = ('<div>')


//An image to overlay
// $overlay.append($image);

//Add overlay

  //A caption

//Capture the click event on a link to an image
$("#local_certs a").click(function(event){
  event.preventDefault();
  $overlay.append($image)
  $("body").append($overlay);
  var imageLocation = $(this).attr('href');
  //Update overlay with the image linked in the link
  $image.attr("src", imageLocation);
  
  //Show the overlay.
  $overlay.show();

});

$(".edx a").click(function(event){
  event.preventDefault();
  $overlay.append($iframewindow)
  $("body").append($overlay);
  var iframeLocation = $(this).attr('href');
  //Update overlay with the image linked in the link
  $iframewindow.attr("src", iframeLocation);
  
  //Show the overlay.
  $overlay.show();

});


//When overlay is clicked
$overlay.click(function(){
  //Hide the overlay
  $overlay.empty()
  $overlay.hide();
});

//add overlay
//append iframe

// get the attribute
$('.container').click(function(){
  $('nav').height('30px');
  $('nav').css('padding-top','10px')
   });

$('#blogs-nav a').click( function(event){
   event.preventDefault();
   var link_to = $(this).attr('href') + '.json'
   $.getJSON( link_to ,
    function(data){ console.log(data['content']); 
    var $blog = $("<div class='entry' id="+ link_to + ">" + '<a href="' +  data['link'] + '" class="entry-title">' + data['subject'] + '</a>' +
                    '<span class="entry-date"> Created ' +  data['created'] + '</span>' +
                    '<div class="entry-body">' + data["htmlcontent"] + '</div>' + "</div>" );
    $('.blogs').prepend($blog);
      location.hash = '#' + link_to;
     } );
   });

  $.getJSON('https://api.github.com/users/BenRuns/events/public', 
    function(data){ 
      console.log(data);
     
      $.each(data, function(index, element) {
        $('#github-feed').append($('<li> <img src=' + element.actor.avatar_url 
        +'/><b> User: </b>' + element.actor.login + '</li><li><b> Event type: </b> ' + element.type  + '</li> <li><b> commits: </b>' + '</li>' + '<li><b> Created: </b> ' + element.created_at + '</li>')); 
      });
    }
);






