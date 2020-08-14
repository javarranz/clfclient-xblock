function CLFClientXBlock(runtime, element) {

	$(element).find('.save-button').bind('click', function() {
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
			runtime.notify('save', {
				state : 'end'
			});
		});
	});

	$(element).find('.cancel-button').bind('click', function() {
		runtime.notify('cancel', {});
	});
}