async function fetchMovies() {
  const title = document.getElementById("searchTitle").value.trim();
  const genre = document.getElementById("genreSelect").value;
  const rating = document.getElementById("ratingSelect").value;
  const mpaa = document.getElementById("mpaaSelect").value;

  let url = "/search?";
  if (title) url += `title=${encodeURIComponent(title)}&`;
  if (genre) url += `genre=${encodeURIComponent(genre)}&`;
  if (rating) url += `rating=${encodeURIComponent(rating)}&`;
  if (mpaa) url += `mpaa=${encodeURIComponent(mpaa)}`;

  const res = await fetch(url);
  const data = await res.json();

  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = data.map(m => `
    <div class="movie-card">
      <h2>${m.Position}. ${m.Title}</h2>
      <p><strong>IMDB Rating:</strong> ${m["IMDb Rating"]}</p>
      <p><strong>MPAA Rating:</strong> ${m["MPAA Rating"]}</p>
      <p><strong>Genres:</strong> ${m.Genres}</p>
    </div>
  `).join("");
}

document.getElementById("searchBtn").addEventListener("click", fetchMovies);
fetchMovies();