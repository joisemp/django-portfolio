$('#card').hover(
    function(){ $(this).addClass('shadow') },
    function(){ $(this).removeClass('shadow')},
  )
  if (window.innerWidth>=1026){
  $('#card').hover(
    function(){ $('#download-btn').removeClass('hide')},
    function(){ $('#download-btn').addClass('hide')},
    console.log("hello")
  )}else{
    $('#download-btn').removeClass('hide')
    console.log('removed')
  }