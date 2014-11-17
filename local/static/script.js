function test(){
alert('ahed')
}

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

