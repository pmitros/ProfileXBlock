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
		    "field" : "name",
		    "placeholder" : "Your name" },
		   {"class" : "ProfileContactInfo", 
		    "children": [
			{"label":"Telephone", 
			 "field":"edx.phone",
			 "class":"ProfileContactBox", 
			 "placeholder" : "1(617)234-5678",
			 "icon" : "phone"
			},
			{"label":"E-mail:", 
			 "field":"edx.email",
			 "class":"ProfileContactBox", 
			 "placeholder" : "jsmith@edx.org",
			 "icon" : "email"
			},
			{"label":"Web site: ", 
			 "field":"edx.website",
			 "class":"ProfileContactBox", 
			 "placeholder" : "http://www.edx.org/",
			 "icon" : "pages"
			},
			{"label":"Skype username", 
			 "field":"edx.skype",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "skype"
			},
			{"label":"http://facebook.com/", 
			 "field":"edx.facebook",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "facebook",
			 "help" : "For help reserving a Facebook URL, see https://www.facebook.com/help/200712339971750#How-do-I-customize-my-timeline-or-Page-address?-Where-can-I-claim-a-username?"
			},
			{"label":"http://plus.google.com/", 
			 "field":"edx.googleplus",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "google-plus"
			},
			{"label":"http://github.com/", 
			 "field":"edx.github",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "github"
			},
			{"label":"http://linkedin.com/in/", 
			 "field":"edx.linkedin",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "linkedin", 
			 "help": "For help reserving a LinkedIn URL, see http://help.linkedin.com/app/answers/detail/a_id/87"
			},
			{"label":"http://twitter.com/", 
			 "field":"edx.twitter",
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
		    "field" : "location", 
		    "placeholder" : "Toronto, Canada" },
		   {"class"    : "ProfileTextArea", 
		    "question" : "What languages are you fluent in?", 
		    "placeholder" : "English", 
		    "field" : "edx.languages",
		    "rows":2},
		   {"class"    : "ProfileDropDown", 
		    "field"    : "edx.age", 
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
		    "field" : "cphys.edbackground",
		    "rows":3},
		   {"class"    : "ProfileTextArea", 
		    "question" : "What is your background in technology? Are you a neophyte? A power user? Do you program? Do you know HTML? Python? Javascript?  How well?", 
		    "field" : "cphys.techbackground",
		    "placeholder" : "Background in technology", 
		    "rows":3},
		   {"class"    : "ProfileTextArea", 
		    "question" : "Tell us a bit about yourself. Write a brief bio.", 
		    "placeholder" : "Biographical Information", 
		    "field" : "cphys.bio",
		    "rows":4}
	       ]}
	 ]}
    ]};

function ProfileXBlock(runtime, element, data) {
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
	    var input=$("input", this);
	    input.change(function(event) {
		$.ajax({
		    type:"POST",
		    url: runtime.handlerUrl(element, "update_profile"),
		    data: JSON.stringify({'field': options.field, 
					  'value' : input.val()})
		});
	    });
	}

	$.fn.ProfileContactBox = function( options ) {
	    this.ProfileTemplateBlock("profile_contact_box", options);
	    var input=$("input", this);
	    input.change(function(event) {
		$.ajax({
		    type:"POST",
		    url: runtime.handlerUrl(element, "update_profile"),
		    data: JSON.stringify({'field': options.field, 
					  'value' : input.val()})
		});
	    });
	}

	$.fn.ProfileDropDown = function( options ) {
	    for(i=0; i<options.choices.length; i++){
		if(options.choices[i].item == options.value) {
		    options.choices[i].selected = 'selected';
		} else {
		    options.choices[i].selected = '';
		}
	    }
	    this.ProfileTemplateBlock("profile_dropdown", options);
	    var select=$("select", this);
	    select.change(function(event) {
		$.ajax({
		    type:"POST",
		    url: runtime.handlerUrl(element, "update_profile"),
		    data: JSON.stringify({'field': options.field, 
					  'value' : select.val()})
		});
	    });
	}

	$.fn.ProfileTextArea = function( options ) {
	    this.ProfileTemplateBlock("profile_text_area", options);
	    var input=$("textarea", this);
	    input.change(function(event) {
		$.ajax({
		    type:"POST",
		    url: runtime.handlerUrl(element, "update_profile"),
		    data: JSON.stringify({'field': options.field, 
					  'value' : input.val()})
		});
	    });
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
		options.children[i]['value'] = data.profile_data[options.children[i].field]
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