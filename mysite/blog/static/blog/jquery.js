$(document).ready(function() {
	$('#homesplash_text_container').hide(0).delay(15000).fadeIn();
})



function handleRequest(){
  if(this.readyState == 4 && this.status == 200){
	  
   }
}

$.post( "http://45.79.145.31:8000/", function( data ) {
  $( "#home_content" ).html( data );
});

