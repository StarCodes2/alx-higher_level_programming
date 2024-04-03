// Fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  $('INPUT#btn_translate').on('click', () => {
    const hello = $('DIV#hello');
    const lang = $('INPUT#language_code').val();

    if (lang !== '') {
      $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
        success: function (result) {
          hello.text(result.hello);
        }
      });
    }
  });
});
