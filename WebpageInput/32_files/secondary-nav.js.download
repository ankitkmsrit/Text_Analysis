function sticky_relocate() {
	var window_top = $(window).scrollTop();
	var div_top = $('#sticky-anchor').offset().top;
	if (window_top > div_top) {
		$('#sticky').addClass('stick');
		$('#sticky-anchor').height($('#sticky').outerHeight());
	} else {
		$('#sticky').removeClass('stick');
		$('#sticky-anchor').height(0);
	}
}

$(function() {
	$(window).scroll(sticky_relocate);
	sticky_relocate();
});

var dir = 1;
var MIN_TOP = 200;
var MAX_TOP = 350;

function autoscroll() {
	var window_top = $(window).scrollTop() + dir;
	if (window_top >= MAX_TOP) {
		window_top = MAX_TOP;
		dir = -1;
	} else if (window_top <= MIN_TOP) {
		window_top = MIN_TOP;
		dir = 1;
	}
	$(window).scrollTop(window_top);
	window.setTimeout(autoscroll, 100);
}

// Secondary Menu Option Selector
// Cache selectors
var lastId,
    topMenu = $("#my-stick-ul"),
    topMenuHeight = topMenu.outerHeight() + 15,
// All list items
    menuItems = topMenu.find("a"),
// Anchors corresponding to menu items
    scrollItems = menuItems.map(function() {
	var item = $($(this).attr("href"));
	if (item.length) {
		return item;
	}
});
// Bind click handler to menu items
// so we can get a fancy scroll animation
menuItems.click(function(e) {
	var href = $(this).attr("href"),
	    offsetTop = href === "#" ? 0 : $(href).offset().top - topMenuHeight + 1;
	$('html, body').stop().animate({
		scrollTop : offsetTop
	}, 300);
	e.preventDefault();
});
// Bind to scroll
$(window).scroll(function() {
	// Get container scroll position
	var fromTop = $(this).scrollTop() + topMenuHeight;
	// Get id of current scroll item
	var cur = scrollItems.map(function() {
		if ($(this).offset().top < fromTop)
			return this;
	});
	// Get the id of the current element
	cur = cur[cur.length - 1];
	var id = cur && cur.length ? cur[0].id : "";
	if (lastId !== id) {
		lastId = id;
		// Set/remove active class
		menuItems.removeClass("sticky-active").filter("[href='#" + id + "']").addClass("sticky-active");
	}
});
