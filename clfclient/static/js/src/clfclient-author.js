function CLFClientXBlock(runtime, element) {
	
	$('#clf-tab').bind('click', function() {
		$('a.nav-link').removeClass('active');
		$(this).addClass('active');
		$('div.tab-pane').removeClass('active');
		$('#clf-div').addClass('active');
	});	
	
	$('#groups-tab').bind('click', function() {
		$('a.nav-link').removeClass('active');
		$(this).addClass('active');
		$('div.tab-pane').removeClass('active');
		$('#groups-div').addClass('active');
	});
	
	$('#parameters-tab').bind('click', function() {
		$('a.nav-link').removeClass('active');
		$(this).addClass('active');
		$('div.tab-pane').removeClass('active');
		$('#parameters-div').addClass('active');
	});
	
	$('#indicators-tab').bind('click', function() {
		$('a.nav-link').removeClass('active');
		$(this).addClass('active');
		$('div.tab-pane').removeClass('active');
		$('#indicators-div').addClass('active');
	});
		
	$('#register-btn').bind('click', function() {
		var handlerUrl = runtime.handlerUrl(element, 'register_on_server_submit');
		var data = {
//			serverIP : $('#serverIP').val()
		};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
//			$('#bingo', element).show();
//			$('#bingo', element).html(response.xml_content);
//			$('.navigation-back-next-buttons', element).hide();
			runtime.notify('save', {state : 'end'});
		});
	});

	$(element).find('.cancel-button').bind('click', function() {
		runtime.notify('cancel', {});
	});

}