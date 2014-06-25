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
	    options["id"] = "profile_block"; 
	    this[options['class']](options);
	}	
	$.fn.ProfileMainBlock = function( options ) {
	    var id = options.id;
	    for(i=0; i<options.children.length; i++){
		var new_id = id+'_'+i;
		$.extend(options.children[i], {'id': new_id});
		options.children[i]["render"]='<div id="'+new_id+'"/>';
	    }	
	    this.html(Mustache.render($("#profile_block").html(),options));
	    for(i=0; i<options.children.length; i++){
		$("#"+options.children[i].id).ProfileBlock(options.children[i]);
	    }
	}
	$.fn.ProfileStaticText = function( options ) {
	    console.log($("#"+options.source).html());
	    this.html(Mustache.render($("#"+options.source).html(),options));
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
	$(".profileblock", element).ProfileBlock( profile_data );
/*	$(".contact",element).ContactInfo( {} );*/

    });
}