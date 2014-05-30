$(document).ready(function() {

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