$(window).on('load', ()=>{
  //To wait until the whole window loads including images
  
  $('#more').on('click', (e) => {
    e.preventDefault();
    const morequotes = $.ajax({
      url: '/bobquotes',
      type: "GET",
      datatype: 'JSON',
    });

    morequotes.done((res) => {
      $('#currentQuote').html(res.quote)
      $('#new_image').html('<img id="currentImage" src="{res.new_paint}">')

      res.new_colors (string of a list)

  

    });
  });

  

  


});
