$(function() {
    $("input[id^='id_']").addClass("form-control");
    $(".base input[id^='id_']").addClass("new-data");

    $('.col-md-3').children('.flag').closest('.col-md-3')
        .children('input').addClass('datepicker');

    $(window).load(function(){
        $(".datepicker").datepicker({format: "yyyy-mm-dd"});
    });


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
        var value = input.val();
        if (!!value )
            $.post(window.XHR_URLS.switch_data,
                   {'_id': id, 'field': field, 'val': value, '_entity': entity},
                   function(data) {
                if (data.res == "success")
                    anchor.html(value);
            }, 'json');

        anchor.show();
        input.hide();
        $(this).hide();
    });

    var form = $("#new-entity");
    var error_place = $("#error-place");
    var buffer = $("#buffer").html();
    var rows_wrapper = $("#rows-wrapper");

    $(document.body).on('click', '#submit-form', function(e){
        e.preventDefault();
        error_place.html('');
        var data = form.serializeArray();
        $.post(window.XHR_URLS.switch_data, data, function(d) {
                if (d.res == "success") {
                    instance = $.parseJSON(d.instance);
                    rows_wrapper.append(buffer);
                    var editable = $("#rows-wrapper .editable");
                    editable.children('.col-md-1.col-md-offset-2').html(instance.id);
                    editable.children(".col-md-3").each(function(i) {
                        var key = $(this).data().key;
                        $(this).children("a.switch-data").html(instance[key]);
                        $(this).children("button").attr("data-id", instance.id);
                        $(this).children(".datepicker").datepicker({format: "yyyy-mm-dd"});
                    });

                    editable.removeClass('editable');
                } else {
                    error_place.html(d.err);
                }
            },
            "json"
        );
    });
});
