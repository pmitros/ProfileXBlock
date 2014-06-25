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
		   {'class' : 'ProfileContactInfo'}
	       ]},
	     { 'class' : 'ProfileForm', 
	       'title' : 'Demographics', 
	       'children' : [
		   {'class'    : 'ProfileOneLiner', 
		    'question' : 'Where do you live?', 
		    'placeholder' : 'Toronto, Canada' },
		   {'class'    : 'ProfileTextArea', 
		    'question' : 'What languages are you fluent in?', 
		    'placeholder' : 'English' },
		   {'class'    : 'ProfileDropDown', 
		    'question' : 'How old are you?', 
		    'choices' : ['Under 13', '14-17', '18-24', '25-35', '35-50', 'Over 50'] },
	       ]},
	 ]},
	{'class' : 'ProfileColumn', 
	 'children' : [
	     { 'class' : 'ProfileStaticText', 
	       'source' : 'photo'},
	     { 'class' : 'ProfileForm', 
	       'title' : 'Background', 
	       'children' : [
		   {'class'    : 'ProfileTextArea', 
		    'question' : 'What is your background in education? Have you taught? Taught physics? Are you involved in education research? Ed-tech? Etc?', 
		    'placeholder' : 'Background in education and physics education' },
		   {'class'    : 'ProfileTextArea', 
		    'question' : 'What is your background in technology? Are you a neophyte? A power user? Do you program? Do you know HTML? Python? Javascript?  How well?', 
		    'placeholder' : 'Background in technology' },
		   {'class'    : 'ProfileTextArea', 
		    'question' : 'Tell us a bit about yourself. Write a brief bio.', 
		    'placeholder' : 'Biographical Information' },
	       ]},
	 ]}
    ]};


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

	$.fn.ProfileDropDown = function( options ) {
	    this.ProfileTemplateBlock("profile_dropdown", options);
	}

	$.fn.ProfileTextArea = function( options ) {
	    this.ProfileTemplateBlock("profile_text_area", options);
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
	    for(i=0; i<options.children.length; i++){
		$("#"+options.children[i].id).ProfileBlock(options.children[i]);
	    }
	}

	$.fn.ProfileColumn = function( options ) {
	    this.ProfileTemplateBlock("profile_column", options);
	}

	$.fn.ProfileStaticText = function( options ) {
	    this.html(Mustache.render($("#"+options.source).html(),options));
	}

	$.fn.ProfileContactInfo = function( options ) {
	    this.ProfileTemplateBlock("contact_info", options);
	}
/*	$.fn.ProfileSection = function( options ) {
	    this.html($("#profile_block").html()); 
	}
	$.fn.ProfileContactInfo = function( options ) {
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