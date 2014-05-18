$(document).ready(function() {
	/* Bootstrap Carousel */
	$('.carousel').carousel({
		interval: 8000,
		pause: "hover"
	});

	/* Ecommerce single item carousel */
	$('.ecarousel').carousel({
		interval: 8000,
		pause: "hover"
	});

	/* Navigation Menu */

	ddlevelsmenu.setup("ddtopmenubar", "topbar");

	/* Dropdown Select */

	/* Navigation (Select box) */

	// Create the dropdown base

	$("<select />").appendTo(".navis");

	// Create default option "Go to..."

	$("<option />", {
		"selected": "selected",
		"value": "",
		"text": "Menu"
	}).appendTo(".navis select");

	// Populate dropdown with menu items

	$(".navi a").each(function () {
		var el = $(this);
		$("<option />", {
			"value": el.attr("href"),
			"text": el.text()
		}).appendTo(".navis select");
	});

	$(".navis select").change(function () {
		window.location = $(this).find("option:selected").val();
	});


	/* Recent post carousel (CarouFredSel) */

	/* Carousel */

	if($('#carousel_container').get(0)) {
		$('#carousel_container').carouFredSel({
			responsive: true,
			width: '100%',
			direction: 'right',
			scroll: {
				items: 4,
				delay: 2000,
				duration: 500,
				pauseOnHover: "true"
			},
			prev: {
				button: "#car_prev",
				key: "left"
			},
			next: {
				button: "#car_next",
				key: "right"
			},
			items: {
				visible: {
					min: 1,
					max: 4
				}
			}
		});
	}

	/* Scroll to Top */


	$(".totop").hide();

	$(function () {
	/*	$(window).scroll(function () {
			if ($(this).scrollTop() > 300) {
				$('.totop').slideDown();
			}
			else {
				$('.totop').slideUp();
			}
		});*/

		$('.totop a').click(function (e) {
			e.preventDefault();
			$('body,html').animate({scrollTop: 0}, 500);
		});

	});


	/* Support */
	$("#slist a").click(function (e) {
		e.preventDefault();
		$(this).next('p').toggle(200);
	});

	/* Careers */

	$('#myTab a').on("click", function (e) {
		e.preventDefault();
		$(this).tab('show');
	});

	//simulate tab click
	var hash = window.location.hash;
	if(hash) {
		$('#myTab li').each(function(){
			if ($(this).children("a").attr("href") == hash) {
				$(this).children("a").trigger("click");
			}
		});
	}

	/**
	 * fancybox
	 */
	$(".fancybox").fancybox({
		'width': 600
	});
});