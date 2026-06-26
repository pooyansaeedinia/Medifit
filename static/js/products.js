const paginationLinks = document.querySelectorAll('.pagination a');

for (let link of paginationLinks) {
    link.addEventListener('click', function(e) {
        e.preventDefault();

        for (let item of paginationLinks) {
            item.classList.remove('active');
        }

        this.classList.add('active');
    });
}