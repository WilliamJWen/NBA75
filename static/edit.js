
//send data to backend
$(document).ready(function () {
    $("#discard").click(function myFunction() {
        let text = "Are you sure about leaving this website\nClick OK to leave or Cancel.";
        if (confirm(text) == true) {window.location.href = "/view/" + id
            return
        } else {
            return
        }
        
    })
    var id = one["id"]
    $("#new-form").submit(function (event) {
        event.preventDefault()
        console.log("submit")
        var item = {
            "id": id,
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
            "fmvp_origin": $("#input-fmvp").val().trim(),}

        $.ajax({
            type: "POST",
            url: "edit_item",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(item),
            success: function (response) {
                console.log(response);
                $(".form-control").val("")
                window.location.href = "/view/" + id
            },
            error: function (request, status, error) {
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });

    })


})