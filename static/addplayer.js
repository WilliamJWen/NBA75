//preparation
function get_feedback(feedback) {
    var template = $("<div class='invalid-feedback'></div>")
    template.html(feedback)
    return template
}
//validate spacing
function validate_string(input_s, parent_s, name) {
    var val = $(input_s).val().trim()
    var valid = true

    if (val == "") {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Please provide a " + name + "."))
        valid = false;
        $(input_s).focus()
    }

    return valid
}

//validate birthyear
function validate_int(input_s, parent_s, name) {
    var val = $(input_s).val()
    var valid = true

    if (val.length == 0) {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Please provide a " + name + "."))
        valid = false;
        $(input_s).focus()
    } else {
        var val = Number(val)

        if (val < 1900 || val > 2022) {
            $(input_s).addClass("is-invalid")
            $(parent_s).append(get_feedback("Please use a number between 1900 and 2022."))
            $(input_s).focus()
            valid = false;
        }
    }
    return valid
}

//validate 24
function validate_long(input_s, parent_s) {
    var val = $(input_s).val()
    var valid = true

    if (val == "") {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Please provide a number of times."))
        $(input_s).focus()
        valid = false;
    } else {
        var val = Number(val)

        if (val < 0 || val > 24) {
            $(input_s).addClass("is-invalid")
            $(parent_s).append(get_feedback("Please use a number between 0 and 24."))
            $(input_s).focus()
            valid = false;
        }
    }
    return valid
}



//validate
function validate_inputs() {
    var valid = true

    // validate name
    name = $("#input-name").val().trim()
    var included = false

    $.each(names, function (index, name_used) {
        name_used = name_used.toLowerCase()
        if (name.toLowerCase() == name_used) {
            included = true
        }
    });

    if (included) {
        $("#input-name").addClass("is-invalid")
        $("#form-name").append(get_feedback("Name have already been created. Please use a different name."))
        valid = false;
    } else if (!validate_string("#input-name", "#form-name", "name")) {
        valid = false
    }

    // validate attack
    if (!validate_int("#input-birth", "#form-birth", "birthyear")) {
        valid = false
    }

    // validate durability
    if (!validate_string("#input-position", "#form-position", "position")) {
        valid = false
    }

    // validate headshot url
    if (!validate_string("#input-headshot", "#form-headshot", "headshot link")) {
        valid = false
    }

    // validate image url
    if (!validate_string("#input-image", "#form-image", "image link")) {
        valid = false
    }

    // validate teams
    if (!validate_string("#input-team", "#form-team", "team")) {
        valid = false
    }

    // validate points
    if (!validate_string("#input-points", "#form-points", "number")) {
        valid = false
    }
    // validate rebounds
    if (!validate_string("#input-rebounds", "#form-rebounds", "number")) {
        valid = false
    }
    // validate assists
    if (!validate_string("#input-assists", "#form-assists", "number")) {
        valid = false
    }

    // validate summary
    if (!validate_string("#input-summary", "#form-summary", "summary")) {
        valid = false
    }

    // validate description
    if (!validate_string("#input-description", "#form-description", "description")) {
        valid = false
    }


    // validate champ
    if (!validate_string("#input-champ", "#form-champ", "year")) {
        valid = false
    }
    // validate mvp
    if (!validate_string("#input-mvp", "#form-mvp", "year")) {
        valid = false
    }

    // validate fmvp
    if (!validate_string("#input-fmvp", "#form-fmvp", "year")) {
        valid = false
    }


    // validate allstar
    if (!validate_long("#input-allstar", "#form-allstar")) {
        valid = false
    }
    // validate allnba
    if (!validate_long("#input-allnba", "#form-allnab")) {
        valid = false
    }

    return valid
}

//send data to backend
$(document).ready(function () {

    $('.alert').hide()

    $("#new-form").submit(function (event) {
        event.preventDefault()

        console.log("submit");

        $(".form-control").removeClass("is-invalid")
        $(".invalid-feedback").remove()
        var valid = validate_inputs()
        console.log(valid);

        if (valid) {
            var item = {
                "name": $("#input-name").val().trim(),
                "headshot": $("#input-headshot").val(),
                "image": $("#input-image").val(),
                "birthyear": $("#input-birth").val().trim(),
                "position": $("#input-position").val().trim(),
                "feature": $("#input-summary").val().trim().toUpperCase(),
                "overview": $("#input-description").val().trim(),
                "points": $("#input-points").val().trim(),
                "rebounds": $("#input-rebounds").val().trim(),
                "assists": $("#input-assists").val().trim(),
                "allstar": $("#input-allstar").val().trim(),
                "allnba": $("#input-allnba").val().trim(),
                "years_origin": $("#input-team").val().trim(),
                "champ_origin": $("#input-champ").val().trim(),
                "mvp_origin": $("#input-mvp").val().trim(),
                "fmvp_origin": $("#input-fmvp").val().trim(),

            }

            $.ajax({
                type: "POST",
                url: "add_item",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(item),
                success: function (response) {
                    console.log("success");
                    $('.alert').show()
                    $("#success-notification").empty()
                    $("#success-notification").html("New player successfully created. <a href='" + response["url"] + "'>Go to see the new player<\a>")
                    $(".form-control").val("")
                    $("#input-name").focus();
                },
                error: function (request, status, error) {
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            });
        }

    })

});