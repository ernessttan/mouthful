const recipeFeed = $("#recipe-feed");


const displayRecipeFeed = (recipes) => {
    // Empty Data
    recipeFeed.empty();
    // Display New Data
    $.each(recipes, (i, recipe) => {
        let recipeCard = `<div id="${recipe["id"]}" class="recipe-card">
        <div class="image-container">
            <img class="recipe-image" src="${recipe["image"]}">
            <div class="tags-container">
                    <div class="tag difficulty">${recipe["difficulty"]}</div>
                    <div class="tag time">${recipe["totaltime"] + "m"}</div>
            </div>
        </div>
        <div class="title-container">
                <h3>${recipe["title"]}</h3>
        </div>
        <div class="subtitle-container">
                <img id="star-icon" src="/static/icons/star.svg">
                <div class="rating">${recipe["rating"]}</div>
        </div>
        </div>`;
        recipeFeed.append(recipeCard);
        $('.recipe-card').on("click", function(e) {
            e.preventDefault();
            let id = $(this).attr("id");
            console.log(id);
            let baseUrl = window.location.origin;
            window.location.replace(baseUrl + "/view_recipe/" + id);
        });
    });
    
}

$(document).ready(() => {
    displayRecipeFeed(recipes);
})