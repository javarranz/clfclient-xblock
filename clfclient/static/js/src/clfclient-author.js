function CLFClientXBlock(runtime, element) {

	///////////////////////////////////////////////////////////////////////////////
	// GENERAL TABS
	///////////////////////////////////////////////////////////////////////////////
	
	$('#clf_tab').bind('click', function() {
		$('.clf_tab').removeClass('active');
		$(this).addClass('active');
		$('div.tab-pane').removeClass('active');
		$('#clf_div').addClass('active');
		return false;
	});	
	
	$('#groups_tab').bind('click', function() {
		$('.clf_tab').removeClass('active');
		$(this).addClass('active');
		$('div.tab-pane').removeClass('active');
		$('#groups_div').addClass('active');
		return false;
	});
	
	$('#parameters_tab').bind('click', function() {
		$('.clf_tab').removeClass('active');
		$(this).addClass('active');
		$('div.tab-pane').removeClass('active');
		$('#parameters_div').addClass('active');
		return false;
	});
	
	$('#indicators_tab').bind('click', function() {
		$('.clf_tab').removeClass('active');
		$(this).addClass('active');
		$('div.tab-pane').removeClass('active');
		$('#indicators_div').addClass('active');
		return false;
	});
	
	///////////////////////////////////////////////////////////////////////////////
	// CLF PHASES TASKS
	///////////////////////////////////////////////////////////////////////////////
	
	var phase_form_reset = function() {
		$('#phase_form').trigger("reset");
		$('#phase_form textarea').html("");
		//$('#phase_type_calc2').attr('checked', 'checked');
	}
	
	$('#phase_new').bind('click', function() {
		$('#phase_view').show();
		$('#clf_tabs').hide();
		$('#phase_view_title').html('New Phase');
		phase_form_reset();
		$('#phase_new_send').show();
		$('#phase_edit_send').hide();
		$('#phase_delete_send').hide();
		$('#phase_view_error').hide();
	});
	
	$('#phase_view_close').bind('click', function() {
		$('#phase_view').hide();
		$('#clf_tabs').show();
	});
	
	///////////////////////////////////////////////////////////////////////////////
	// IDICATORS
	///////////////////////////////////////////////////////////////////////////////
	
	$('#ind_active_tab').bind('click', function() {
		$('.ind_tab').removeClass('active');
		$(this).addClass('active');
		$('.Passive').hide();
		$('.Active').show();
		return false;
	});
	
	$('#ind_passive_tab').bind('click', function() {
		$('.ind_tab').removeClass('active');
		$(this).addClass('active');
		$('.Passive').show();
		$('.Active').hide();
		return false;
	});
	
	var ind_form_fill = function(ind_data) {
		$('#ind_id').val(ind_data.id);
		$('#ind_weka_model').val(ind_data.wekaModel);
		$('#ind_name').val(ind_data.name);
		$('#ind_description').val(ind_data.description);
		$('#ind_type').val(ind_data.type);
		$('#ind_manual_rule').val(ind_data.manualRule);
		$("input[name=ind_type_calc][value=" + ind_data.typeCalculation + "]").attr('checked', 'checked');
	}
	
	var ind_form_reset = function() {
		$('#ind_form').trigger("reset");
		$('#ind_form textarea').html("");
		$('#ind_type_calc2').attr('checked', 'checked');
	}
	
	$('.ind_view_link').bind('click', function() {
		var handlerUrl = runtime.handlerUrl(element, 'indicator_manage');
		var data = {action: 'view', ind_id: $(this).attr('id'), ind_data: {}};
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			$('#ind_view').show();
			$('#ind_tabs').hide();
			$('#ind_view_title').html('View Indicator');
			ind_form_fill(response.ind_data);
			$('#ind_new_send').hide();
			$('#ind_edit_send').hide();
			$('#ind_delete_send').hide();
			$('#ind_view_error').hide();
		});
		return false;
	});
	
	var ind_rules_funtion = function() {
		var handlerUrl = runtime.handlerUrl(element, 'indicator_manage');
		var data = {action: 'toggle_calc', ind_id: $(this).attr('id'), ind_data: {'typeCalculation': 1}};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			var id = response.ind_data.ind_id;
			$('#' + id + '.ind_calc').attr({"title" : "Weka Calculation"});
			$('#' + id + '.ind_calc').html("<i class='fab fa-weebly'></i>");
			$('#' + id + '.ind_calc').addClass('ind_weka_link');
			$('#' + id + '.ind_calc').removeClass('ind_rules_link');
			$('#' + id + '.ind_calc').unbind('click');
			$('#' + id + '.ind_calc').bind('click', ind_weka_function);
			runtime.notify('save', {state : 'end'});
		});
		return false;
	};
	$('.ind_rules_link').bind('click', ind_rules_funtion);
	
	var ind_weka_function = function() {
		var handlerUrl = runtime.handlerUrl(element, 'indicator_manage');
		var data = {action: 'toggle_calc', ind_id: $(this).attr('id'), ind_data: {'typeCalculation': 0}};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			var id = response.ind_data.ind_id;
			$('#' + id + '.ind_calc').attr({"title" : "Muanual Rules"});
			$('#' + id + '.ind_calc').html("<i class='far fa-hand-paper'></i>");
			$('#' + id + '.ind_calc').addClass('ind_rules_link');
			$('#' + id + '.ind_calc').removeClass('ind_weka_link');
			$('#' + id + '.ind_calc').unbind('click');
			$('#' + id + '.ind_calc').bind('click', ind_rules_funtion);
			runtime.notify('save', {state : 'end'});
		});
		return false;
	};
	$('.ind_weka_link').bind('click', ind_weka_function);
	
	var ind_edit_function = function() {
		var handlerUrl = runtime.handlerUrl(element, 'indicator_manage');
		var data = {action: 'view', ind_id: $(this).attr('id'), ind_data: {}};
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			$('#ind_view').show();
			$('#ind_tabs').hide();
			$('#ind_view_title').html('Edit Indicator');
			ind_form_fill(response.ind_data);
			$('#ind_new_send').hide();
			$('#ind_edit_send').show();
			$('#ind_delete_send').show();
			$('#ind_view_error').hide();
		});
		return false;
	};
	$('.ind_edit_link').bind('click', ind_edit_function);
	
	$('#ind_new').bind('click', function() {
		$('#ind_view').show();
		$('#ind_tabs').hide();
		$('#ind_view_title').html('New Indicator');
		ind_form_reset();
		$('#ind_new_send').show();
		$('#ind_edit_send').hide();
		$('#ind_delete_send').hide();
		$('#ind_view_error').hide();
	});
	
	var ind_add_row = function(ind_data) {
		var ind_row = '<tr class=';
		if (ind_data.type == '0') {
			ind_row += 'Active';
		} else {
			ind_row += 'Passive';
		}
		ind_row += " id=" + ind_data.id + '>' +
	      '<td>' + ind_data.name + '</td>' +
	      '<td>' + ind_data.description + '</td>';
		if (ind_data.type == '0') {
			ind_row += '<td>Active</td>';
		} else if (ind_data.target == '1') {
			ind_row += '<td>Passive</td>';
		} 
		ind_row += '<td style="width:70px">';
		ind_row += '<a href="#" id="' + ind_data.id + '" class="ind_edit_link" title="Edit">' + 
			'<i class="fas fa-edit"></i>&nbsp;</a>&nbsp;';
		ind_row += '<a href="#" id="' + ind_data.id + '" class="ind_params_link" title="Parameters">' + 
			'<i class="fas fa-chart-bar"></i>&nbsp;</a>&nbsp;';
		if (ind_data.typeCalculation == '1') {
			ind_row += '<a href="#" id="' + ind_data.id + '" class="ind_rules_link" title="Muanual Rules">' + 
			'<i class="far fa-hand-paper"></i>&nbsp;</a>';
		} else {
			ind_row += '<a href="#" id="' + ind_data.id + '" class="ind_weka_link" title="Weka Calculation">' + 
			'<i class="fab fa-weebly"></i>&nbsp;</a>';
		}
		ind_row += '</td></tr>';
		$('#ind_tbody tr:first').before(ind_row);
		$('.ind_edit_link').bind('click', ind_edit_function);
	}
	
	var ind_get_data = function() {
		var ind_data = {
			id: $('#ind_id').val(),
			name: $('#ind_name').val(),
			description: $('#ind_description').val(),
			wekaModel: $('#ind_weka_model').val(),
			type: $('#ind_type').val(),
			manualRule: $('#ind_manual_rule').val(),
			typeCalculation: $('input[name="ind_type_calc"]:checked').val()
		}
		//console.log($('input[name="ind_type_calc"]:checked').val()); 
		return ind_data;
	}
	
	$('#ind_new_send').bind('click', function() {
		if ($('#ind_form')[0].checkValidity() === false) {
			return;
		}
		var handlerUrl = runtime.handlerUrl(element, 'indicator_manage');
		var data = {action: 'new', ind_id: '', ind_data: ind_get_data()};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			if (response.result == 'success') {
				ind_add_row(response.ind_data);
				$('#ind_view').hide();
				$('#ind_tabs').show();
			} else {
				$('#ind_view_error').show();
				$('#ind_view_error').html('Error: ' + response.ind_data.faultstring);
			}
			runtime.notify('save', {state : 'end'});
		});
	});
	
	$('#ind_edit_send').bind('click', function() {
		if ($('#ind_form')[0].checkValidity() === false) {
			return;
		}
		var handlerUrl = runtime.handlerUrl(element, 'indicator_manage');
		var data = {action: 'edit', ind_id: '', ind_data: ind_get_data()};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			if (response.result == 'success') {
				$('#ind_tbody tr#'+response.ind_data.id).remove();
				ind_add_row(response.ind_data);
				$('#ind_view').hide();
				$('#ind_tabs').show();
			} else {
				$('#ind_view_error').show();
				$('#ind_view_error').html('Error: ' + response.ind_data.faultstring);
			}
			runtime.notify('save', {state : 'end'});
		});
	});
	
	$('#ind_delete_send').bind('click', function() {
		var handlerUrl = runtime.handlerUrl(element, 'indicator_manage');
		var data = {action: 'delete', ind_id: '', ind_data: ind_get_data()};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			if (response.result == 'success') {
				$('#ind_tbody tr#'+response.ind_data.id).remove();
				$('#ind_view').hide();
				$('#ind_tabs').show();
			} else {
				$('#ind_view_error').show();
				$('#ind_view_error').html('Error: ' + response.ind_data.faultstring);
			}
			runtime.notify('save', {state : 'end'});
		});
	});
	
	$('#ind_view_close').bind('click', function() {
		$('#ind_view').hide();
		$('#ind_tabs').show();
	});
	
	
	///////////////////////////////////////////////////////////////////////////////
	// PARAMETERS
	///////////////////////////////////////////////////////////////////////////////
	
	$('#param_active_tab').bind('click', function() {
		$('.param_tab').removeClass('active');
		$(this).addClass('active');
		$('.Passive').hide();
		$('.Active').show();
		return false;
	});
	
	$('#param_passive_tab').bind('click', function() {
		$('.param_tab').removeClass('active');
		$(this).addClass('active');
		$('.Passive').show();
		$('.Active').hide();
		return false;
	});
	
	var param_form_fill = function(param_data) {
		$('#param_id').val(param_data.id);
		$('#param_name').val(param_data.name);
		$('#param_description').val(param_data.description);
		$('#param_alias').val(param_data.metricAlias);
		$('#param_type').val(param_data.metricType);
		$('#param_data_type').val(param_data.dataType);
		$('#param_target').val(param_data.target);
		$('#param_query').val(param_data.query);
	}
	
	var param_form_reset = function() {
		$('#param_form').trigger("reset");
		$('#param_form textarea').html("");
	}
	
	$('.param_view_link').bind('click', function() {
		var handlerUrl = runtime.handlerUrl(element, 'parameter_manage');
		var data = {action: 'view', param_id: $(this).attr('id'), param_data: {}};
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			$('#param_view').show();
			$('#param_tabs').hide();
			$('#param_view_title').html('View Parameter');
			param_form_fill(response.param_data);
			$('#param_new_send').hide();
			$('#param_edit_send').hide();
			$('#param_delete_send').hide();
			$('#param_view_error').hide();
		});
		return false;
	});
	
	var param_edit_function = function() {
		var handlerUrl = runtime.handlerUrl(element, 'parameter_manage');
		var data = {action: 'view', param_id: $(this).attr('id'), param_data: {}};
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			$('#param_view').show();
			$('#param_tabs').hide();
			$('#param_view_title').html('Edit Parameter');
			param_form_fill(response.param_data);
			$('#param_new_send').hide();
			$('#param_edit_send').show();
			$('#param_delete_send').show();
			$('#param_view_error').hide();
		});
		return false;
	};
	$('.param_edit_link').bind('click', param_edit_function);
	
	$('#param_new').bind('click', function() {
		$('#param_view').show();
		$('#param_tabs').hide();
		$('#param_view_title').html('New Parameter');
		param_form_reset();
		$('#param_new_send').show();
		$('#param_edit_send').hide();
		$('#param_delete_send').hide();
		$('#param_view_error').hide();
	});
	
	var param_add_row = function(param_data) {
		var param_row = '<tr class=' + param_data.metricType + " id=" + param_data.id + '>' +
	      '<td><b>'+ param_data.metricAlias + '</b></td>' +
	      '<td>' + param_data.name + '</td>' +
	      '<td>' + param_data.description + '</td>';
		if (param_data.target == '0') {
			param_row += '<td>Versions</td>';
		} else if (param_data.target == '1') {
			param_row += '<td>Forums</td>';
		} else if (param_data.target == '2') {
			param_row += '<td>Ratings</td>';
		} else if (param_data.target == '3') {
			param_row += '<td>Generic</td>';
		} 
		param_row += '<td><a href="#" id="' + param_data.id + '" class="param_edit_link" title="Edit">' + 
			'<i class="fas fa-edit"></i></a></td></tr>';
		$('#param_tbody tr:first').before(param_row);
		$('.param_edit_link').bind('click', param_edit_function);
	}
	
	var param_get_data = function() {
		var param_data = {
			id: $('#param_id').val(),
			name: $('#param_name').val(),
			description: $('#param_description').val(),
			metricAlias: $('#param_alias').val().toUpperCase(),
			dataType: $('#param_data_type').val(),
			metricType: $('#param_type').val(),
			target: $('#param_target').val(),
			query: $('#param_query').val()
		}
		return param_data;
	}
	
	$('#param_new_send').bind('click', function() {
		if ($('#param_form')[0].checkValidity() === false) {
			return;
		}
		var handlerUrl = runtime.handlerUrl(element, 'parameter_manage');
		var data = {action: 'new', param_id: '', param_data: param_get_data()};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			if (response.result == 'success') {
				param_add_row(response.param_data);
				$('#param_view').hide();
				$('#param_tabs').show();
			} else {
				$('#param_view_error').show();
				$('#param_view_error').html('Error: ' + response.param_data.faultstring);
			}
			runtime.notify('save', {state : 'end'});
		});
	});
	
	$('#param_edit_send').bind('click', function() {
		if ($('#param_form')[0].checkValidity() === false) {
			return;
		}
		var handlerUrl = runtime.handlerUrl(element, 'parameter_manage');
		var data = {action: 'edit', param_id: '', param_data: param_get_data()};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			if (response.result == 'success') {
				$('#param_tbody tr#'+response.param_data.id).remove();
				param_add_row(response.param_data);
				$('#param_view').hide();
				$('#param_tabs').show();
			} else {
				$('#param_view_error').show();
				$('#param_view_error').html('Error: ' + response.param_data.faultstring);
			}
			runtime.notify('save', {state : 'end'});
		});
	});
	
	$('#param_delete_send').bind('click', function() {
		var handlerUrl = runtime.handlerUrl(element, 'parameter_manage');
		var data = {action: 'delete', param_id: '', param_data: param_get_data()};
		runtime.notify('save', {state : 'start'});
		$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
			if (response.result == 'success') {
				$('#param_tbody tr#'+response.param_data.id).remove();
				$('#param_view').hide();
				$('#param_tabs').show();
			} else {
				$('#param_view_error').show();
				$('#param_view_error').html('Error: ' + response.param_data.faultstring);
			}
			runtime.notify('save', {state : 'end'});
		});
	});
	
	$('#param_view_close').bind('click', function() {
		$('#param_view').hide();
		$('#param_tabs').show();
	});

/*	$(element).find('.cancel-button').bind('click', function() {
		runtime.notify('save', {state : 'start'});
		runtime.notify('save', {state : 'end'});
		runtime.notify('cancel', {});
		runtime.notify('error', {title: 'Title', message: 'Content'})
	});*/

}