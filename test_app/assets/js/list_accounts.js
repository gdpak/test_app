$(function(){
    var delete_in_place                 = false;
    var selected_accounts               = Array();
    var account_marked_for_deletion     = null;
    var account_marked_for_deletion_url = null;

    function toggle_delete_buttons(status){
        $("#delete_button"        ).prop('disabled', status);
        $("#delete_inplace_button").prop('disabled', status);
    }

    toggle_delete_buttons(true);
    $(".selected_account").prop('checked', false);

    $('.selected_account').click(function(event){
        if($(this).is(':checked')){
            selected_accounts.push(this.value);
            $(this).closest('tr').addClass('selected_row');
        } else {
            $(this).closest('tr').removeClass('selected_row');
            selected_accounts.splice(selected_accounts.indexOf(this.value), 1);
        }

        toggle_delete_buttons(selected_accounts.length == 0);

        form_action = delete_accounts_url;
        for(account of selected_accounts){
            form_action += account + '/';
        }

        $("#list_accounts_form").prop('action', form_action);
    });

    $('.delete_account_link').click(function(event){
        event.preventDefault();
        account_marked_for_deletion = event.currentTarget.href;
        $('#deletion_confirmation_modal_id').modal('show');
        return false;
    });

    $("#delete_button").click(function(event){
        delete_in_place = false;
        $('#deletion_confirmation_modal_id').modal('show');
    });

    $("#delete_inplace_button").click(function(event){
        delete_in_place = true;
        $('#deletion_confirmation_modal_id').modal('show');
    });

    $('#confirmation_submit').click(function(event){
        tmp = account_marked_for_deletion;
        account_marked_for_deletion = null;

        if(tmp){
            window.location.href = tmp;
        }else if (selected_accounts.length > 0){
            if (delete_in_place) {
                $.ajax({
                    url    : delete_accounts_in_place_url,
                    data   : { accounts: JSON.stringify(selected_accounts) },
                    method : "POST",
                    success: function(data){
                        if(data.status){
                            $('.selected_row').remove();
                            if($("#list_accounts_form tbody tr").length == 0){
                                $("#list_accounts_form").next()
                                    .before("<p>No more accounts in the list!</p>")
                                $("#list_accounts_form").remove();
                            }
                        } else {
                            $('#deletion_error_modal').modal('show');
                        }
                        toggle_delete_buttons(false);
                        $(".selected_account").prop('checked', true);
                        $('#deletion_confirmation_modal_id').modal('hide');
                    }});
            } else {
                $("#list_accounts_form").submit();
            }
        }
        $('#deletion_confirmation_modal_id').modal('hide');
    });
});
