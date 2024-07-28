

function init() {
    console.log("catgeories page!!");


    document.getElementById("txtSearch").addEventListener("input", event => {
        const search= event.target.value;

        const cats = document.querySelectorAll(".category-grid a");

        cats.forEach(link => {
            // current: if the category text contains the search query text
            // go to: if the category text contains the search query, or the subcategories of the category contains the search query
            if(link.textContent.toLocaleLowerCase().indexOf(search.toLocaleLowerCase()) >= 0) {
                // show
                link.classList.remove("hide");
            }
            else {
                // hide
                link.classList.add("hide");
            }
        });
    })
}

window.onload = init;