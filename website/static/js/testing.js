$(document).ready(function(){
    if ($("#TestForm input:checked").size() == 0) {
        $("#TestForm input:submit").attr('disabled', 'disabled');
        $("#TestForm .RoundedCorners").addClass("Disabled");
    }
    $("#TestForm input:radio, #TestForm input:checkbox").click(function(){
        if ($("#TestForm input:checked").size() == 0){
            $("#TestForm input:submit").attr('disabled', 'disabled');
            $(".RoundedCorners").addClass("Disabled");
        }
        else {
            $("#TestForm input:submit").removeAttr('disabled');
            $("#TestForm .RoundedCorners").removeClass("Disabled");
        }
    });
});

