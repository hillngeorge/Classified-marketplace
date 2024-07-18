

function init() {
    console.log("catgeories page!!");


    document.getElementById("txtSearch").addEventListener("input", event => {
        const search= event.target.value;

        const cats = document.querySelectorAll(".category-grid a");

        cats.forEach(link => {
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