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
      $('#new_image').html('<img id="currentImage" src='+res.new_paint+'>');
      $('#colorContain').empty();
      for (item of res.new_colors){
        $('#colorContain').append('<div class="col" style="background-color:'+item+';color:'+item+'">color</div>');      
      };
      $('input#paintingURL').val(res.new_paint)
      $('input#youtubeURL').val(res.vid_link)

    });
  });

  

});

function _(selector){
  return document.querySelector(selector);
}
function setup(){
  let canvas = createCanvas(650, 600);
  canvas.parent("canvas-wrapper");
  background(255);
}
function mouseDragged(){
  let type = _("#pen-pencil").checked?"pencil":"brush";
  let size = parseInt(_("#pen-size").value);
  let color =  _("#pen-color").value;
  fill(color);
  stroke(color);
  if(type == "pencil"){
line(pmouseX, pmouseY, mouseX, mouseY);
  } else {
    ellipse(mouseX, mouseY, size, size)
  }
}

_("#reset-canvas").addEventListener("click",function(){
  background(255);
});

_("#save-canvas").addEventListener("click", function(){
  saveCanvas(canvas, "sketch", "png");
});


