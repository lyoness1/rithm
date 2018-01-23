$('#reload-jokes').click(e => {
	$.ajax({
		url: '/jokes',
		type: 'get',
		success: resp => {
			console.log(resp);
		},
		error: function(xhr) {
			//Do Something to handle error
		},
	});
});
