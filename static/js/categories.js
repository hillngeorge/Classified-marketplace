function init() {
    console.log("categories page!!");

    document.getElementById("txtSearch").addEventListener("input", event => {
        const search = event.target.value.toLowerCase();
        const categories = document.querySelectorAll(".category-grid a, .category-grid .subcategories a");

        categories.forEach(link => {
            if (link.textContent.toLowerCase().includes(search)) {
                link.classList.remove("hide");
                // Show the subcategory container if it contains a matching link
                const subcategoryContainer = link.closest(".subcategories");
                if (subcategoryContainer) {
                    subcategoryContainer.classList.add("show");
                }
            } else {
                link.classList.add("hide");
            }
        });
    });
}

window.onload = init;
