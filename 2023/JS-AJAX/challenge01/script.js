document.addEventListener("DOMContentLoaded", () => {
    
    document.querySelector("button").addEventListener("click", () => {
        
        const request = new XMLHttpRequest();
        request.onload = function(){
            const data = JSON.parse(this.responseText);
            keys = Object.keys(data[0].name);
            console.log(keys);
            for (let i = 0; i < data.length; i++){
                const tr = document.createElement("tr");
                const name = document.createElement("td");
                const alpha_two_code = document.createElement("td");
                const web_page = document.createElement("td");

                
                
                const web_page_link = document.createElement("a");
                web_page_link.setAttribute("href", data[i].web_pages);
                web_page_link.setAttribute("target", "_blank");
                web_page_link.innerHTML = data[i].web_pages;

                name.innerHTML = data[i].name;
                alpha_two_code.innerHTML = data[i].alpha_two_code;
                web_page.appendChild(web_page_link);


                tr.appendChild(name);
                tr.appendChild(alpha_two_code);
                tr.append(web_page);
                document.querySelector(".result").appendChild(tr);
            }
        
        }
        var country = document.getElementById("country").value;
        request.open("GET", "http://universities.hipolabs.com/search?country=" + country);
        var Table = document.querySelector(".result");
        Table.innerHTML = "";
        request.send();




    })

})