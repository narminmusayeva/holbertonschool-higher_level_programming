document.addEventListener("DOMContentLoaded", function () {
  const movieList = document.getElementById("list_movies");

  fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then((response) => response.json())
    .then((data) => {
      const films = data.results;
      films.forEach((film) => {
        const li = document.createElement("li");
        li.textContent = film.title;
        movieList.appendChild(li);
      });
    })
    .catch((error) => {
      console.error("Error fetching films:", error);
    });
});
