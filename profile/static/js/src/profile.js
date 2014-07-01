/* Javascript for ProfileXBlock. */
var profile_asset_map; 

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
	    var container = this;
	    var input=$("input", this);
	    var inactive=$(".inactive-edit", this);
	    input.change(function(event) {
		$.ajax({
		    type:"POST",
		    url: runtime.handlerUrl(element, "update_profile"),
		    data: JSON.stringify({'field': options.field, 
					  'value' : input.val()})
		});
		$(".active-inactive-container",container).removeClass('active');
		inactive.text(input.val());
	    });
	    input.blur(function(event){
		$(".active-inactive-container",container).removeClass('active');
	    });
	    input.focusout(function(event){
		$(".active-inactive-container",container).removeClass('active');
	    });
	    $(".active-inactive-container",this).click(function(event) {
		event.preventDefault();
		$(".active-inactive-container",container).addClass('active');
		input.focus();
	    });
	}

	$.fn.ProfileContactBox = function( options ) {
	    this.ProfileTemplateBlock("profile_contact_box", options);
	    var inactive=$(".inactive-edit", this);
	    var input=$("input", this);
	    var container = this;
	    input.change(function(event) {
		$.ajax({
		    type:"POST",
		    url: runtime.handlerUrl(element, "update_profile"),
		    data: JSON.stringify({'field': options.field, 
					  'value' : input.val()})
		});
		$(".active-inactive-container",element).removeClass('active');
	    });
	    input.blur(function(event){
		$(".active-inactive-container",container).removeClass('active');
	    });
	    input.focusout(function(event){
		$(".active-inactive-container",container).removeClass('active');
	    });
	    $(".active-inactive-container",this).click(function(event) {
		event.preventDefault();
		$(".active-inactive-container",container).addClass('active');
		input.focus();
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
	    var container = this;
	    var input=$("textarea", this);
	    var inactive=$(".inactive-edit", this);
	    input.change(function(event) {
		$.ajax({
		    type:"POST",
		    url: runtime.handlerUrl(element, "update_profile"),
		    data: JSON.stringify({'field': options.field, 
					  'value' : input.val()})
		});
		$(".active-inactive-container",container).removeClass('active');
		inactive.text(input.val());
	    });
	    	    input.blur(function(event){
		$(".active-inactive-container",container).removeClass('active');
	    });
	    input.focusout(function(event){
		$(".active-inactive-container",container).removeClass('active');
	    });
	    $(".active-inactive-container",this).click(function(event) {
		event.preventDefault();
		$(".active-inactive-container",container).addClass('active');
		input.focus();
	    });
	}

	$.fn.ProfileTemplateBlock = function( template, options ) {
	    var i;
	    id = options.id;
	    if (typeof options.children === 'undefined') {
		options['children'] = [];
	    }
	    options['profile_data'] = data.profile_data;
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
	$(".profileblock", element).ProfileBlock( data.profile_config );
    });
}