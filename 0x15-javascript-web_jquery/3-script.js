// Adds the class red to the <header> element when the user clicks on the tag DIV#red_header
$('DIV#red_header').on('click', () => {
  if (!$('header').hasClass('red')) {
    $('header').addClass('red');
  }
});
