/* Javascript for ProfileXBlock. */
var profile_asset_map; 

var profile_data = { 
    "class" : "ProfileMainBlock", 
    "children" : [
	{"class" : "ProfileColumn", 
	 "children" : [
	     { "class" : "ProfileStaticText", 
	       "source" : "profile_overview"},
	     { "class" : "ProfileForm", 
	       "title" : "Contact Information", 
	       "children" : [
		   {"class"    : "ProfileOneLiner", 
		    "question" : "Name", 
		    "placeholder" : "Your name" },
		   {"class" : "ProfileContactInfo", 
		    "children": [
			{"label":"Telephone", 
			 "class":"ProfileContactBox", 
			 "placeholder" : "1(617)234-5678",
			 "icon" : "phone"
			},
			{"label":"E-mail:", 
			 "class":"ProfileContactBox", 
			 "placeholder" : "jsmith@edx.org",
			 "icon" : "email"
			},
			{"label":"Web site: ", 
			 "class":"ProfileContactBox", 
			 "placeholder" : "http://www.edx.org/",
			 "icon" : "pages"
			},
			{"label":"Skype username", 
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "skype"
			},
			{"label":"http://facebook.com/", 
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "facebook",
			 "help" : "For help reserving a Facebook URL, see https://www.facebook.com/help/200712339971750#How-do-I-customize-my-timeline-or-Page-address?-Where-can-I-claim-a-username?"
			},
			{"label":"http://plus.google.com/", 
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "google-plus"
			},
			{"label":"http://github.com/", 
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "github"
			},
			{"label":"http://linkedin.com/in/", 
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "linkedin", 
			 "help": "For help reserving a LinkedIn URL, see http://help.linkedin.com/app/answers/detail/a_id/87"
			},
			{"label":"http://twitter.com/", 
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "twitter"
			}
		   ]}
	       ]},
	     { "class" : "ProfileForm", 
	       "title" : "Demographics", 
	       "children" : [
		   {"class"    : "ProfileOneLiner", 
		    "question" : "Where do you live?", 
		    "placeholder" : "Toronto, Canada" },
		   {"class"    : "ProfileTextArea", 
		    "question" : "What languages are you fluent in?", 
		    "placeholder" : "English", 
		    "rows":2},
		   {"class"    : "ProfileDropDown", 
		    "question" : "How old are you?", 
		    "choices" : [{"item": "Prefer not to say"}, {"item":"Under 13"}, {"item":"14-17"}, {"item":"18-24"}, {"item":"25-35"}, {"item":"35-50"}, {"item":"Over 50"}]}
	       ]}
	 ]},
	{"class" : "ProfileColumn", 
	 "children" : [
	     { "class" : "ProfileStaticText", 
	       "source" : "photo"},
	     { "class" : "ProfileForm", 
	       "title" : "Background", 
	       "children" : [
		   {"class"    : "ProfileTextArea", 
		    "question" : "What is your background in education? Have you taught? Taught physics? Are you involved in education research? Ed-tech? Etc?", 
		    "placeholder" : "Background in education and physics education", 
		    "rows":3},
		   {"class"    : "ProfileTextArea", 
		    "question" : "What is your background in technology? Are you a neophyte? A power user? Do you program? Do you know HTML? Python? Javascript?  How well?", 
		    "placeholder" : "Background in technology", 
		    "rows":3},
		   {"class"    : "ProfileTextArea", 
		    "question" : "Tell us a bit about yourself. Write a brief bio.", 
		    "placeholder" : "Biographical Information", 
		    "rows":4}
	       ]}
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

	$.fn.ProfileContactBox = function( options ) {
	    this.ProfileTemplateBlock("profile_contact_box", options);
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
	    for(i = 0; i<options.children.length; i++) {
		if (typeof profile_asset_map[options.children[i].icon] != 'undefined') {
		    options.children[i].icon = profile_asset_map[options.children[i].icon];
		}
	    }
	    this.ProfileTemplateBlock("profile_contact_info", options);
	}
    }(jQuery));

    $(function ($) {
        /* Here's where you'd do things on page load. */
	profile_asset_map = JSON.parse($("#profile_asset_map").text());
	$(".profileblock", element).ProfileBlock( profile_data );
    });
}