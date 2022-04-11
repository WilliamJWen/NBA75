$(document).ready(function () {


    $("#search-form").submit(function (event) {

        var text = $.trim($("#search-box").val())
        if (text == "") {
            $("#search-box").val("")
            $("#search-box").focus()
            event.preventDefault()
        }
        else {
            event.preventDefault()
            var input = $("#search-box").val()
            window.location.href = "/search/" + input
        }
    })})
