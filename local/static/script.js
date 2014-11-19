// test 
function test(){
alert('ahed')
}

$(function() {
    $( document  ).tooltip({
        position: {
            my: "center bottom-20",
    at: "center top",
    using: function( position, feedback  ) {
        $( this  ).css( position  );
        $( "<div>"  )
        .addClass( "arrow"  )
        .addClass( feedback.vertical  )
        .addClass( feedback.horizontal  )
        .appendTo( this  );
    }
        }
    });
});


$(document).ready(function() {
	
	$('#container').fullPaged({
		'direction' : 'bottom'
	});

var myInterval = setInterval(function(){
$.ajax({
    url:"http://cherrypy-ahed.rhcloud.com/api/states/LED1"
    }).success (function(responseText) {
   var array = responseText.split(',')
   $("#led1").html(array[0]) 
$("#led2").html(array[1]) 
$("#pot").html(array[2]) 
       })

   },1000)
});

