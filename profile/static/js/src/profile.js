/* Javascript for ProfileXBlock. */
var profile_data = { 
    'class' : 'ProfileMainBlock', 
    'children' : [
	{ 'class' : 'ProfileStaticText', 
	  'source' : 'profile_overview'},
	{ 'class' : 'ProfileStaticText', 
	  'source' : 'contact_information'},
	{ 'class' : 'ProfileStaticText', 
	  'source' : 'demographics'},
	{ 'class' : 'ProfileStaticText', 
	  'source' : 'photo'},
	{ 'class' : 'ProfileStaticText', 
	  'source' : 'background'}
	/*    { 'class' : 'profile_block', 
	      'title' : 'Contact Information',
	      'contents' : {}},
	      { 'class' : 'profile_block', 
	      'title' : 'Demographics',
	      'contents' : {}}, 
	      { 'class' : 'break' }, 
	      { 'class' : 'photo_block' }, 
	      { 'class' : 'profile_block', 
	      'title' : 'Background' }*/
    ]
};


function ProfileXBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });

    (function ( $ ) {
	$.fn.ProfileBlock = function( options ) {
	    this[options['class']](options);
	}	
	$.fn.ProfileMainBlock = function( options ) {
	    this.html(Mustache.render($("#profile_block").html(),options));
	}
/*	$.fn.ProfileSection = function( options ) {
	    this.html($("#profile_block").html()); 
	}
	$.fn.ContactInfo = function( options ) {
	    this.html($("#contact_info").html());
	    
	    console.log(this);
	}*/
    }(jQuery));

    $(function ($) {
        /* Here's where you'd do things on page load. */
	console.log("Hello!");
	
	$(".profileblock", element).ProfileBlock( profile_data );
/*	$(".contact",element).ContactInfo( {} );*/

    });
}