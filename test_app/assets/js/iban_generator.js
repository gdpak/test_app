$(function(){
    update_input_masks = function() {
        selected = $("#generator_country :selected");

        $("#generator_bank"   ).inputmask({mask: selected.attr("bank_mask"   )});
        $("#generator_account").inputmask({mask: selected.attr("account_mask")});
    }

    $('.random_option'           ).prop('disabled', true).prop('checked' , true);
    $('#generator_country'       ).prop('disabled', true);
    $('.randomizable_input'      ).prop('disabled', true);
    $('#generator_random_country').prop('checked' , true);

    $('#generator_random_country').click(function(){
        lock_status = $(this).is(':checked');
        $('#generator_country').prop('disabled', lock_status);

        update_input_masks();

        $('.random_option').each(function(){
            $(this).prop('disabled', lock_status);
        });
    });

    $('#generator_country').change(function(){
        update_input_masks();
    });

    $('.random_option').click(function () {
        $(this).parentsUntil('form')
            .find('.randomizable_input')
            .prop('disabled', $(this).is(':checked'));
    });
})
