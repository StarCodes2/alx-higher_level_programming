// Fetches and prints how to say “Hello” depending on the language
function ajaxGet (lang, domElement) {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
    success: function (result) {
      domElement.text(result.hello);
    }
  });
}

$(document).ready(function () {
  const hello = $('DIV#hello');
  const langInput = $('INPUT#language_code');

  $('INPUT#btn_translate').on('click', () => {
    const lang = langInput.val();

    if (lang !== '') {
      ajaxGet(lang, hello);
    }
  });

  langInput.on('keyup', (event) => {
    if (event.which === 13) {
      const lang = langInput.val();

      if (lang !== '') {
        ajaxGet(lang, hello);
      }
    }
  });
});
