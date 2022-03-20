const searchInputCheck = () => {
    if($("#search-entry").val() === '') {
        raiseError($("#search-error"), 'Search cannot be blank')
        $("#search").css({"border": "1px solid var(--orange-500-color)"})
    } else {
        let textEntry = $("#search-entry").val().toLowerCase();
        let baseUrl = window.location.origin;
        window.location.replace(baseUrl + "/search/" + textEntry);
    }
}

const raiseError = (selector, message) => {
    selector.text(message)
    $('html, body').animate({
        scrollTop: $(selector).prev().offset().top
    }, 500);
}

const removeOrange = (selector) => {
    selector.css({"border": "none"})
}


$(document).ready(() => {
    $("#search").on('submit', (e) => {
        e.preventDefault();
        searchInputCheck();
    });

    $("#search-entry").on('keyup', function() {
        removeOrange($(this));
        $(this).next().text('');
    });
});
