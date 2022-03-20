const displayRecipe = (recipe) => {
    $("#recipe-title").append(recipe.title);
    $("#recipe-image").attr("src", recipe.image);
    $("#recipe-cuisine").append(`Cuisine Type: ${recipe.cuisine}`);
    $("#recipe-difficulty").append(`Difficulty: ${recipe.difficulty}`);
    $("#prep-time").append(`Prep: ${recipe.preptime}m`);
    $("#cook-time").append(`Cook: ${recipe.cooktime}m`);
    $("#recipe-servings").append(`Servings: ${recipe.servings}`);

    for(let i=0; i < recipe.ingredients.length; i++) {
        let ingredient = recipe.ingredients[i];
        $("#recipe-ingredients").append(`<li class="recipe-ingredient">${ingredient}</li>`)
    }

    for(let i=0; i < recipe.instructions.length; i++) {
        let instruction = recipe.instructions[i];
        $("#recipe-instructions").append(
            `<li class="recipe-instruction">
                <span class="instruction-num">${i + 1}</span>
                <span class="instruction">${instruction}</span>
            </li>`)
    }


}



$(document).ready(() => {
    displayRecipe(recipe_to_display)
})