document.addEventListener("DOMContentLoaded", () => {

    let url = "https://omdbapi.com/?apikey=7233e730&s="

    function clearSearchSection() {
        try {
            const table = document.querySelector("table");
            table.innerHTML = "";
            return true;
        } catch (error) {
            console.log(error);
            return false;
        }
    }

    function putLoading() {
        const table = document.querySelector("table");
        table.innerHTML = "Loading...";
    }

    function addMoviesToResultSection(movies) {
        const table = document.querySelector("table");
        movies.forEach(movie => {
            const row = document.createElement("tr");
            const title = document.createElement("td");
            title.append(movie.Title);
            const year = document.createElement("td");
            year.append(movie.Year);
            const imgPoster = document.createElement("img");
            imgPoster.src = movie.Poster;
            imgPoster.alt = movie.Title;
            const poster = document.createElement("td");
            poster.append(imgPoster);

            row.append(title);
            row.append(year);
            row.append(poster);
            table.append(row);
        });
    }

    function getFilmUsingPromise(searchQuery) {
        const promise = new Promise((resolve, reject) => {
            console.log("ok");
        })
    }
    

    function addMoviesToResultSection(movies) {
        const table = document.querySelector("table");
        movies.forEach(movie => {
            const row = document.createElement("tr");
            const title = document.createElement("td");
            title.append(movie.Title);
            const year = document.createElement("td");
            year.append(movie.Year);
            const imgPoster = document.createElement("img");
            imgPoster.src = movie.Poster;
            imgPoster.alt = movie.Title;
            const poster = document.createElement("td");
            poster.append(imgPoster);

            row.append(title);
            row.append(year);
            row.append(poster);
            table.append(row);
        }); 
    }

    function getFilm(searchQuery, callbackSuccess, callbackError) {
        const ajax = new XMLHttpRequest();
        ajax.onload = function() {
            clearSearchSection();
            putLoading();

            if (this.status === 200) {
                callbackSuccess(this.responseText);
                
            } else {
                callbackError("Gagal mengambil data.");
            }
            
        }

        ajax.open("GET", `${url+searchQuery}`);
        ajax.send();
    }

    function getFilmwithErrorHandler(searchQuery) {
        const ajax = new XMLHttpRequest();
        ajax.onload = function() {
            clearSearchSection();
            putLoading();

            if (this.status === 200) {
                setTimeout(() => {
                    const response = JSON.parse(this.responseText);
                    clearSearchSection();
                    // console.log(response.Search);
                    addMoviesToResultSection(response.Search);
                }, 2000);
            } else {
                clearSearchSection();
                console.log("Error get movies!");
                alert("Error get movies!");
            }
            
        }

        // ajax.onreadystatechange = function() {
        //     if (this.readyState === 4 && this.status === 200) {

        //     }
        // }

        ajax.open("GET", `${url+searchQuery}`);
        ajax.send();
    }

    document.querySelector("button").addEventListener("click", () => {
        const sQ = document.querySelector("#search-entry").value; 
        // getFilmwithErrorHandler(sQ);
        getFilm(sQ,
            function(data){
                setTimeout(() => {
                    const response = JSON.parse(data);
                    clearSearchSection();
                    addMoviesToResultSection(response.Search);
                }, 2000);
                // console.log(data);
            },
            function(error){
                // error
                console.log(error);
                clearSearchSection();
                alert("Error get movies!");
            });
    })
})