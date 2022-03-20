const recipeFeed = $("#recipe-feed");


function displayRecipeFeed(recipes) {
    // Empty Data
    recipeFeed.empty();
    // Display New Data
    $.each(recipes, (i, recipe) => {
        let recipeCard = `<a class="recipe-card">
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
        </a>`;
        recipeFeed.append(recipeCard);
    });
    
}

$(document).ready(() => {
    displayRecipeFeed(recipes);
})