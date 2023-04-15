document.addEventListener("DOMContentLoaded", function(){
 
    let url = "https://www.omdbapi.com/?apikey=26ced797&s=star%20wars"
 
    function clearSearchSection(){
        try {
            const table = document.querySelector("table");
            table.innerHTML = "";
            return true;
        } catch (error) {
            console.log(error);
            return false;
        }
 
    }
 
    function addMoviesToResultSection(movies){
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
 
    function getFilm(searchQuery, callbackSuccess, callbackError){
 
        const ajax = new XMLHttpRequest();
        ajax.onload = function() {
            if (this.status === 200){
                callbackSuccess(this.responseText);
            } else {
                callbackError(Error("Failed get data."));
            }
        }
        ajax.open("GET", '${url+searchQuery}');
        ajax.send();
    }
 
    function getFilmWithErrorHandler(searchQuery){
 
        const ajax = new XMLHttpRequest();
        ajax.onload = function(){
            clearSearchSection();
            putLoading();
            if (this.status === 200){ // 200 is OK
                setTimeout(()=>{
                    const response = JSON.parse(this.responseText);
                    clearSearchSection();
                    addMoviesToResultSection(response.Search);
                }, 2000);
            } else {
                console.log("Error get movies!");
                alert("Error get movies!");
            }
 
        }
        // ajax.onreadystatechange = function(){
        //     if (this.readyState === 4 && this.status === 200){
 
        //     }
        // }
        ajax.open("GET", `${url+searchQuery}`);
        ajax.send();


 
    }

    function getFilmWithPromise(searchQuery){

        const promise = new Promise( (resolve, reject) => {

            const ajax = new XMLHttpRequest();
            ajax.onload = function () {
                if (this.status === 200){
                    resolve(this.responseText);
                } else {
                    reject(Error("Failed to get data."));
                }
            };
            ajax.open("GET", `${url+searchQuery}`);
            ajax.send();
        });

        promise
            .then(data => JSON.parse(data))
            .then(data => data = data.Search)
            .then(data => addMoviesToResultSection(data))
            .catch(error => console.log(error));
    }
    

    function getFilmWithFetch(searchQuery){
        fetch('$(url+searchQuery')
            .then(data => data.json())
            .then(data => addMoviesToResultSection(data.Search))
            .catch(Error("Failed get data."))
    }

    async function getFilmAsync(searchQuery){

        try{
            const response = await fetch('$(url+searchQuery');
            const movies = await response.json();
            return movies.Search;

        } catch {
            console.log(error);
            alert("Error get movies!");
        } finally {
            console.log("Finally");
        }

        const response = await fetch('$url+searchQuery');
        const movies = await response,json();
        return movies.Search;
    }
 
 
    document.querySelector("button").addEventListener("click", () => {
        const sQ = document.querySelector("#search-entry").value;
        getFilmWithFetch(sQ);
        // getFilmWithPromise(sQ);

        // getFilm(sQ, 
        //     function(data){
        //         //success
        //         setTimeout(() => {
        //             const response = JSON.parse(data);
        //             clearSearchSection();
        //             addMoviesToResultSection(response.Search);
        //         }, 2000);
        //     },
        //     function(error){
        //         console.log(error);
        //         clearSearchSection();
        //         alert("Error get movies")
        //     });
        // getFilmWithErrorHandler(sQ);
        // getFilmWithJquery(sQ);

        getFilmAsync(sQ).then(movies => addMoviesToResultSection(movies));

    })
 
})