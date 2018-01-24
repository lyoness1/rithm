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

$('.up-vote').click(e => {
	var joke_id = $(e.target).data('id');
	$.ajax({
		url: '/jokes/' + joke_id + '/up-vote',
		type: 'post',
		success: resp => {
			console.log(resp);
		},
		error: function(xhr) {
			//Do Something to handle error
		},
	});
});
