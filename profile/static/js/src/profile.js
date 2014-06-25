/* Javascript for ProfileXBlock. */
var profile_data = { 
    'class' : 'ProfileMainBlock', 
    'children' : [
	{'class' : 'ProfileColumn', 
	 'children' : [
	     { 'class' : 'ProfileStaticText', 
	       'source' : 'profile_overview'},
	     { 'class' : 'ProfileForm', 
	       'title' : 'Contact Information', 
	       'children' : [
		   {'class'    : 'ProfileOneLiner', 
		    'question' : 'Name', 
		    'placeholder' : 'Your name' },
		   {'class' : 'ProfileStaticText',
		    'source':'profile_details'}
	       ]},
	     { 'class' : 'ProfileStaticText', 
	       'source' : 'demographics'},
	 ]},
	{'class' : 'ProfileColumn', 
	 'children' : [
	     { 'class' : 'ProfileStaticText', 
	       'source' : 'photo'},
	     { 'class' : 'ProfileStaticText', 
	       'source' : 'background'}//]}
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
	 ]}]};
//};


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
	    options["id"] = "profile_block"; 
	    this.ProfileTemplateBlock("profile_block", options);
	}

	$.fn.ProfileForm = function( options ) {
	    this.ProfileTemplateBlock("profile_form", options);
	}

	$.fn.ProfileOneLiner = function( options ) {
	    this.ProfileTemplateBlock("profile_one_liner", options);
	}

	$.fn.ProfileTemplateBlock = function( template, options ) {
	    var i;
	    id = options.id;
	    if (typeof options.children === 'undefined') {
		options['children'] = [];
	    }
	    for(i=0; i<options.children.length; i++){
		new_id = id+'_'+i;
		options.children[i]['id'] = new_id;
		options.children[i]["render"]='<div id="'+new_id+'"/>';
	    }
	    this.html(Mustache.render($("#"+template).html(),options));
	    console.log(options.children.length);
	    for(i=0; i<options.children.length; i++){
		console.log(options.children[i].id);
		console.log(options.children[i]);
		$("#"+options.children[i].id).ProfileBlock(options.children[i]);
	    }
	}

	$.fn.ProfileColumn = function( options ) {
	    this.ProfileTemplateBlock("profile_column", options);
	}

	$.fn.ProfileStaticText = function( options ) {
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