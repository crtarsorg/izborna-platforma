
$( function() {
    $('.tabs').toggle();
    $('.election-tabs-link').click(function(){
        $('.tabs').toggle();
    })
    $( "#tabs" ).tabs({
        collapsible: true

    })

    $( "#tabs_indicators" ).tabs({
        collapsible: true

    })
    $( "#tabs_table" ).tabs({
        collapsible: true

    })

		$(".meter > span").each(function() {
				$(this)
					.data("origWidth", $(this).width())
					.width(0)
					.animate({
						width: $(this).data("origWidth")
					}, 1200);
			});

       var select = $('#select2').select2();
  /* Select2 plugin as tagpicker */
  $("#tagPicker").select2({
    closeOnSelect:false
  });

});
