// Fatches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
$(function () {
  const character = $('DIV#character');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (user) {
      character.append(user.name);
    }
  });
});
