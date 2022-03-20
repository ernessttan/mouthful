$(document).ready(() => {
    $("#search").on('submit', (e) => {
        e.preventDefault();
        let textEntry = $("#search-entry").val().toLowerCase();
        let baseUrl = window.location.origin;
        window.location.replace(baseUrl + "/search/" + textEntry);
    });
});
