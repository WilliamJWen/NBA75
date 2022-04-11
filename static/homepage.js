function make_card(index, item) {

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

  
   title.html(item["name"])
   card_position.html(item["position"])
   card_summary.html(item["feature"])
   
   card_body.append(card_position)
   card_body.append(title)
   
   card_body.append(card_summary)
   
   card.append(card_body)

   block.append(card)
   return block
}





