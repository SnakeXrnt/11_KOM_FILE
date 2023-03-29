// retrieve the search form and search results table elements
const searchForm = document.querySelector('#search-form');
const searchResults = document.querySelector('#search-results tbody');

// add a listener for form submission
searchForm.addEventListener('submit', event => {
  // prevent the default form submission behavior
  event.preventDefault();
  // get the user's search query from the input field
  const searchEntry = document.querySelector('#search-entry').value;
  // construct the URL for the OMDB API search request
  const url = `https://www.omdbapi.com/?apikey=2288de7d&s=${searchEntry}`;
  // make the API request using fetch
  fetch(url)
    .then(response => response.json())
    .then(data => {
      // clear any existing search results from the table
      searchResults.innerHTML = '';
      // iterate over each search result and create a new table row for it
      data.Search.forEach(result => {
        const row = document.createElement('tr');
        // create a new cell for the title and add it to the row
        const titleCell = document.createElement('td');
        titleCell.textContent = result.Title;
        row.appendChild(titleCell);
        // create a new cell for the year and add it to the row
        const yearCell = document.createElement('td');
        yearCell.textContent = result.Year;
        row.appendChild(yearCell);
        // create a new cell for the poster image and add it to the row
        const posterCell = document.createElement('td');
        const posterImage = document.createElement('img');
        posterImage.src = result.Poster;
        posterCell.appendChild(posterImage);
        row.appendChild(posterCell);
        // add the completed row to the search results table
        searchResults.appendChild(row);
      });
    })
    .catch(error => {
      // if there was an error fetching data from the API, log the error to the console
      console.error(error);
    });
});
