$(function(){
    var selected_accounts               = Array();
    var account_marked_for_deletion_url = null;

    $("#delete_button"        ).prop('disabled', true);
    $("#delete_inplace_button").prop('disabled', true);

    $('.selected_account').click(function(event){
        if($(this).is(':checked')){
            selected_accounts.push(this.value);
        } else {
            selected_accounts.splice(selected_accounts.indexOf(this.value), 1);
        }

        $("#delete_button"        ).prop('disabled', selected_accounts.length == 0);
        $("#delete_inplace_button").prop('disabled', selected_accounts.length == 0);
    });

    $('.delete_account_link').click(function(event){
        event.preventDefault();
        account_marked_for_deletion = event.currentTarget.href;
        $('#deletion_confirmation_modal_id').modal('show');
        return false;
    });

    $('#confirmation_submit').click(function(event){
        tmp = account_marked_for_deletion;
        account_marked_for_deletion = null;

        if(tmp){
            window.location.href = tmp;
        }
    });
});
