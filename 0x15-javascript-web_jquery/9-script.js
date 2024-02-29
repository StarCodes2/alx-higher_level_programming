// Fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
$(function () {
  const hello = $('DIV#hello');
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (result) {
      hello.text(result.hello);
    }
  });
});
