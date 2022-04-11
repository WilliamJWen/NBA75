function make_card_marked(index, item) {

    var block = $("<div class='col-md-4 result-item'></div>")

    var card = $("<div class='card bg-light'></div>")

    var id = item["id"]
    var image_link = $("<a href='/view/" + id + "'></a>")
    var card_img = $("<img class='card-img-top' src='" + item["headshot"] + "' alt='headshot' >")
    image_link.html(card_img)
    card.append(image_link)

    var card_body = $("<div class='card-body'>")

    var title = $("<div class='card-title'></div>")
    var card_position = $("<div class='card-text'></div>")
    var card_summary = $("<p class='card-text'></p>")

    var st = item["position_st"]
    var en = item["position_en"]
    if (item["matched"]=="name") {
        var name = item["name"]
        var title_highlight = [name.slice(0, st), "<span class='highlight-result border-secondary'>", name.slice(st, en), "</span>", name.slice(en)].join('')
        title.html(title_highlight)
        card_position.html(item["position"])
        card_summary.html(item["feature"])
    } else {
        title.html(item["name"])
        var position = item["position"]
        var position_highlight = [position.slice(0, st), "<span class='highlight-result border-secondary'>", position.slice(st, en), "</span>", position.slice(en)].join('')
        card_position.html(position_highlight)
        card_summary.html(item["feature"])
    }
    card_body.append(card_position)
    card_body.append(title)
    
    card_body.append(card_summary)
    
    card.append(card_body)

    block.append(card)
    return block
}

function display_results_marked(data) {
    $("#result_list").empty();

    var n_items = data.length
    var row1 = $("<div class='row'></div>")
    var col = $("<div class='col-md-12'></div>")
    col.html(n_items + " results found.")
    row1.append(col)
    $("#result_list").append(row1)

    var row2 = $("<div id='results' class='row'></div>")
    $("#result_list").append(row2)

    $.each(data, function (index, item) { 
        console.log(data);
        
        var result = make_card_marked(index, item)
        
        $("#results").append(result)
    });
}

$(document).ready(function () {
    if (n_items == 0) {
        $("#result_list").html("No results found.")
    } else {
        display_results_marked(results)
    }
})





