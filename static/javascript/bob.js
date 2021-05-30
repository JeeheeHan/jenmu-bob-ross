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
      //Input quote, img and colors into page per button click
      $('#currentQuote').html(res.quote);
      // $('#new_image').html('<img id="currentImage" src='+res.new_paint+'>');
      //background image
      $('#background-image').html('<img id="currentImage" src='+res.new_paint+'>');

      $('#colorContain').empty();
      for (item of res.new_colors){
        $('#colorContain').append('<div class="col" style="background-color:'+item+';color:'+item+'">color</div>');      
      };
      $('input#paintingURL').val(res.new_paint)
      $('input#youtubeURL').val(res.vid_link)

    });
  });


});



