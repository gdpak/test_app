$(function(){
	$('.random_option'           ).prop('disabled', true).prop('checked' , true);
	$('.randomizable_input'      ).prop('disabled', true);
	$('#generator_random_country').prop('checked' , true);

	$('#generator_random_country').click(function(){
		lock_status = $(this).is(':checked');
		$('.lockable_group').each(function(){
			$(this).prop('disabled', lock_status);
		});
	});

	$('.random_option').click(function () {
		$(this).parentsUntil('form')
			.find('.randomizable_input')
			.prop('disabled', $(this).is(':checked'));
	});
})
