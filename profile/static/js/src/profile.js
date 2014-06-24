/* Javascript for ProfileXBlock. */
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
	$.fn.contactinfo = function() {
	    this.html($("#contact_info").html());
	    
	    console.log(this);
	}
    }(jQuery));

    $(function ($) {
        /* Here's where you'd do things on page load. */
	console.log("Hello!");
	
	$(".contact",element).contactinfo();

    });
}