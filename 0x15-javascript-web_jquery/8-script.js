// Fatches and lists the title for all movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
$(function () {
  const movieList = $('UL#list_movies');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (movies) {
      $.each(movies.results, function (i, movie) {
        movieList.append('<li>' + movie.title + '</li>');
      });
    }
  });
});
