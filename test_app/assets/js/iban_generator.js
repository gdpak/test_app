$(function(){
    $('#generator_id').on('shown.bs.modal', function () {
        $("#generator_bank"   ).val('');
        $("#generator_account").val('');

        $('.random_option'           ).prop('disabled', true).prop('checked' , true);
        $('#generator_country'       ).prop('disabled', true);
        $('.randomizable_input'      ).prop('disabled', true);
        $('#generator_random_country').prop('checked' , true);
    });


    update_input_masks = function() {
        selected = $("#generator_country :selected");

        $("#generator_bank"   ).val('');
        $("#generator_account").val('');

        bank_input    = $("#generator_bank"   ).data('bs.inputmask');
        account_input = $("#generator_account").data('bs.inputmask');

        if(bank_input) {
            bank_input.mask = selected.attr("bank_mask");
            bank_input.init();
        } else {
            $("#generator_bank").inputmask({mask: selected.attr("bank_mask")})
        }

        if(account_input) {
            account_input.mask = selected.attr("account_mask");
            account_input.init();
        } else {
            $("#generator_account").inputmask({mask: selected.attr("account_mask")})
        }
    }

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

    $('#generator_submit').click(function(event){
        $.ajax({
            url    : generator_url,
            data   : $('#generator_form').serializeArray(),
            method : "POST",
            success: function(data){
                console.log(data);
                $('#IBAN_account').val(data.generated_iban);
                $('#generator_id').modal('hide');
    }})});
});
