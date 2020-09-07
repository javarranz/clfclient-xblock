function CLFClientXBlock(runtime, element) {
	
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