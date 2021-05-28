$(window).on('load', ()=>{
  //To wait until the whole window loads including images
  
  $('#morequotes').on('click',(e)=>{
    e.preventDefault();
    const morequotes = $.ajax({
      url:'/bobquotes',
      type:"GET",
      datatype: 'JSON',
    });
    
    morequotes.done( (res)=>{
      $('#currentQuote').html(res.quote)
      
    });
 });



});
