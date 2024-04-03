// Toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
$('DIV#toggle_header').on('click', () => {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
