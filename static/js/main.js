$(function() {
    $("input").addClass("form-control");
    $(".base input").addClass("new-data");
    $('.col-md-3').children('.flag').closest('.col-md-3').children('input').addClass('datepicker');
    $(".datepicker").datepicker({dateFormat: 'yy-mm-dd'});

    $(document.body).on('click', 'a.switch-data', function(e){
        e.preventDefault();
        $(this).hide();
        $(this).closest('.col-md-3').children('.new-data').show();
    });

    $(document.body).on('click', 'button.new-data', function(e){
        e.preventDefault();
        var input = $(this).closest('.col-md-3').children('input.new-data');
        var anchor = $(this).closest('.col-md-3').children('.switch-data');
        var id = $(this).data().id;
        var field = $(this).data().field;
        var entity = $('#container').data().entity;

        $.post(window.XHR_URLS.switch_data,
               {'id': id, 'field': field, 'value': input.val(), 'entity': entity},
               function(data) {
            if (data.res == "success")
                anchor.html(data.data);
        });
        console.log(id, field, input.val());

        anchor.show();
        input.hide();
        $(this).hide();
    });

});
