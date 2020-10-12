function CLFClientXBlock(runtime, element) {

	$('#register-btn').bind('click', function() {
		var handlerUrl = runtime.handlerUrl(element, 'register_on_server_submit');
		var data = {};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			$('#packageUUID').val(response);
			$('#register-btn').hide();
			runtime.notify('save', {state : 'end'});
		});
	});
	
	$('#save-studio-settings').bind('click', function() {
		var handlerUrl = runtime.handlerUrl(element, 'submit_studio_edits');
		var data = {};
		$(element).find('.setting-input').each(function() {
			var $field = $(this);
			data[$field.attr('name')] = $field.val();
		});
		//console.log(JSON.stringify(data));
		var values = {values: data, defaults: []}
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(values)).done(function(response) {
			runtime.notify('save', {state : 'end'});
		});
	});

	$('#cancel-studio-settings').bind('click', function() {
		runtime.notify('cancel', {});
	});
}