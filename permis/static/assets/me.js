$(document).ready(function() {
    $('select[name="type_demande"]').on('change', function() {
        var bus = $(this).val();
        if (bus) {
            if (bus == 'N') {

            }
            if (bus == 'R') {
                // $.ajax({
                //     // https//{{domain}}{% url 'activate' uidb64=uid token=token %}
                //     // url: "{{ URL::to('trajet') }}/" + trajets,
                //     url: "{{domain}}{% url 'activate' "+trajets+"uidb64=uid token=token %}",
                //     type: "GET",
                //     dataType: "json",
                //     success: function(data) {
                //         $('select[name="trajet_id"]').empty();
                //         $.each(data, function(key, value) {
                //             $('select[name="trajet_id"]').append('<option value="' +
                //                 value + '">' + value + '</option>');
                //         });
                //     },
                // });
                $.ajax({
                    // url: "{{ URL::to('section') }}/" + bus,
                    url: "{% url 'registerr' " + bus + " %}",
                    type: "GET",
                    dataType: "json",
                    success: function(data) {
                        $('select[name="bus_id"]').empty();
                        $.each(data, function(key, value) {
                            $('select[name="bus_id"]').append('<option value="' +
                                value + '">' + value + '</option>');
                        });
                    },
                });
            }


        } else {
            console.log('AJAX load did not work');
        }
    });

});

$(document).ready(function() {
    $('select[name="bus_id"]').on('change', function() {
        var trajets = $(this).val();
        if (trajets) {
            $.ajax({
                url: "{{ URL::to('trajet') }}/" + trajets,
                type: "GET",
                dataType: "json",
                success: function(data) {
                    $('select[name="trajet_id"]').empty();
                    $.each(data, function(key, value) {
                        $('select[name="trajet_id"]').append('<option value="' +
                            value + '">' + value + '</option>');
                    });
                },
            });

        } else {
            console.log('AJAX load did not work');
        }
    });

});