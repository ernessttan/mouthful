let recipeToSave = {
    id: 0,
    title: "",
    description: "",
    image: "",
    difficulty: "",
    rating: 4.0,
    preptime: "",
    cooktime: "",
    servings: "",
    cuisine: "",
    ingredients: [],
    instructions: []
}

/*    Function to Fill recipeToSave object   */
const fillRecipeToSave = (recipe) => {
    recipeToSave.id = recipe["id"]
    recipeToSave.title = recipe["title"];
    recipeToSave.description = recipe["description"];
    recipeToSave.image = recipe["image"]
    recipeToSave.servings = recipe["servings"]
    recipeToSave.preptime = recipe["preptime"]
    recipeToSave.cooktime = recipe["cooktime"]
    recipeToSave.cuisine = recipe["cuisine"]
    recipeToSave.difficulty = recipe["difficulty"];
    recipeToSave.ingredients = recipe["ingredients"];
    recipeToSave.instructions = recipe["instructions"];
    
    displayFields();
}


/*    Function to display the Recipe   */
const displayFields = () => {
    $("#title-input").val(recipeToSave.title);
    $("#description-input").val(recipeToSave.description);
    $("#recipe-image-preview").attr("src", recipeToSave.image);
    $("#recipe-image-preview").css({"object-fit": "cover", "width": "inherit", "height": "100%"});
    $("#servings-input").val(recipeToSave.servings);
    $("#prep-input").val(recipeToSave.preptime);
    $("#cook-input").val(recipeToSave.cooktime);
    $("#cuisine-input").val(recipeToSave.cuisine);
    displayAddedIngredients(recipeToSave.ingredients);
    displayAddedInstructions(recipeToSave.instructions);
}

/*    Function For Previewing Recipe Image    */
function previewImage(input) {
    if (input.files && input.files[0]) {
        // FileReader Object allows web applications to asynchronously read the contents of files
        let reader = new FileReader();

        // Fired when a read has been completed
        reader.onload = function(e) {
            let imageUrl = e.target.result;
            recipeToSave.image = imageUrl;
            // Update Image src with file url
            $("#recipe-image-preview").attr("src", imageUrl);
            // Hide Placeholder Image
            $("#recipe-image-preview").hide();
            $("#recipe-image-preview").fadeIn(650);
            $("#recipe-image-preview").css({"width": "100%", "height": "100%"});
        }
        reader.readAsDataURL(input.files[0]);
    }
}

/*    Function to save recipe to database   */
const saveRecipe = () => {
    let totalTime = parseInt($("#prep-input").val()) + parseInt($("#cook-input").val());
    recipeToSave.title = $("#title-input").val();
    recipeToSave.servings = $("#servings-input").val();
    recipeToSave.preptime = $("#prep-input").val();
    recipeToSave.cooktime = $("#cook-input").val();
    recipeToSave.cuisine = $("#cuisine-input").val();
    recipeToSave.totaltime = totalTime;
    $.ajax({
        type: "POST",
        url: "add_recipe",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(recipeToSave),
        success: function(results) {
            viewRecipe(results["id"])
            clearForm();
            displaySuccess();
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}
/*    Function to validate recipe input   */
function recipeInputCheck() {
    let recipeTitle = $("#title-input").val().trim();
    let recipeDescription = $("#description-input").val().trim();
    let recipeServings = $("#servings-input").val().trim();
    let recipePrepTime = $("#prep-input").val().trim();
    let recipeCookTime = $("#cook-input").val().trim();
    let recipeCuisine = $("#cuisine-input").val().trim();
    let recipeImage = recipeToSave.image;
    let recipeDifficulty = recipeToSave.difficulty;
 
    if(recipeTitle === '') {
        raiseError($("#title-error"), 'Title cannot be blank')
        $("#title-input").css({"border": "1px solid var(--orange-500-color)"})
    }
    if(recipeDescription === '') {
        raiseError($("#description-error"), 'Description cannot be blank');
        $("#description-input").css({"border": "1px solid var(--orange-500-color)"});
        return false
    }
    if(recipeServings === '') {
        raiseError($("#servings-error"), 'Servings cannot be blank')
        $("#servings-input").css({"border": "1px solid var(--orange-500-color)"})
        return false
    }
    if(recipePrepTime === '') {
        raiseError($("#prep-error"), 'Servings cannot be blank')
        $("#prep-input").css({"border": "1px solid var(--orange-500-color)"})
        return false
    }
    if(recipeCookTime === '') {
        raiseError($("#cook-error"), 'Servings cannot be blank')
        $("#cook-input").css({"border": "1px solid var(--orange-500-color)"})
        return false
    }
    if(recipeCuisine === '') {
        raiseError($("#cuisine-error"), 'Cuisine cannot be blank')
        $("#cuisine-input").css({"border": "1px solid var(--orange-500-color)"})
        return false
    }
    if(recipeDifficulty === '') {
        alert("Please select a recipe difficulty")
        return false
    }
    if(recipeImage === '') {
        alert("Please add a recipe image")
        return false
    }
    if(recipeToSave.ingredients.length === 0) {
        alert("Please add an ingredient")
        return false
    }
    if(recipeToSave.instructions.length === 0) {
        alert("Please add an instruction")
        return false
    }
    else {
        return true;
    }
}

/*    Function to clear input fields   */
function clearForm() {
    $("#title-input").val('')
    $("#description-input").val('');
    $("#servings-input").val('')
    $("#prep-input").val('')
    $("#cook-input").val('');
    $("#cuisine-input").val('');
    $("#recipe-image-preview").attr("src", "/static/images/image_placeholder.svg");
    $("#recipe-image-preview").css({width: "auto", height: "auto"})
    $("#added-ingredients").empty();
    $("#added-instructions").empty();
}

/*    Function to Add Ingredient   */
const addIngredient = () => {
    let ingredientName = $("#ingredient-name").val();
    let ingredientAmount = $("#ingredient-amount").val();
    let ingredientUnit = $("#ingredient-unit").val();
    let ingredient = ingredientAmount + ingredientUnit + " " + ingredientName;
    recipeToSave.ingredients.push(ingredient);
    $("#ingredient-name").val("");;
    $("#ingredient-amount").val("");
    $("#ingredient-unit").val("")
}

/*    Function to Display Already Added Ingredients    */
const displayAddedIngredients = (ingredients) => {
    $("#added-ingredients").empty();

    for(let i=0; i < ingredients.length; i++) {
        let ingredient = ingredients[i]

        let newIngredient = `<li class="ingredient-entry">
        <div>${ingredient}</div> 
        <button type='button' class='delete-ingredient'><img class='trash-icon' src='/static/icons/trashred.svg'></button>
        </li>`

        $("#added-ingredients").append(newIngredient);

        $(".delete-ingredient").on("click", function(e) {
            e.preventDefault();
            let ingredientToRemove = $(this).prev().html();
            deleteAddedIngredient(ingredientToRemove);
            displayAddedIngredients(ingredients);
        });
    }
}

/*    Function to Delete Added Ingredients    */
const deleteAddedIngredient = (ingredientToRemove) => {
    let index = ingredients.indexOf(ingredientToRemove);

    if (index > -1) {
        ingredients.splice(index, 1)
    }
}

/*    Function to Add new instructions   */
const addInstruction = () => { 
    let instruction = $("#instruction-text").val();
    $("#instruction-text").val("");
    instructions.push(instruction);
}

/*    Function to Display already added instructions   */
const displayAddedInstructions = (instructions) => {
    $("#added-instructions").empty();

    for(let i=0; i < instructions.length; i++) {
        let instruction = instructions[i];

        let newInstruction = `<li class="instruction-entry">
        <div><span class="instruction-num">${i + 1}</span><span class="instruction">${instruction}</span></div> 
        <button type='button' class='delete-instruction'><img class='trash-icon' src='/static/icons/trashred.svg'></button>
        </li>`

        $("#added-instructions").append(newInstruction);

        $(".delete-instruction").on("click", function(e) {
            e.preventDefault();
            let instructionToRemove = $(this).prev().find(".instruction").html();
            console.log(instructionToRemove);
            deleteInstruction(instructionToRemove);
            displayAddedInstructions(instructions);
        });
    }   
}

/*    Function to Delete already added instructions   */
const deleteInstruction = (instructionToRemove) => {
    let index = instructions.indexOf(instructionToRemove);

    if (index > -1) {
        instructions.splice(index, 1)
    }
}

/*    Function to validate instruction input   */
const instructionInputCheck = () => {
    let instruction = $("#instruction-text").val();

    if(instruction === '') {
        raiseError($("#instruction-error"), "Instruction cannot be blank")
        $("#instruction-text").css({"border": "1px solid var(--orange-500-color)"})
    } else {
        addInstruction();
        displayAddedInstructions(instructions)
        $(".modal").css({"display": "none"});
    }
}

/*    Success Functions    */

const displaySuccess = () => {
    $("#success-message").css({"display": "block"});
}

const viewRecipe = (id) => {
    let baseUrl = window.location.origin;
    let recipeUrl = baseUrl + "/view_recipe/" + id
    $("#view-recipe").attr("href", recipeUrl)
}



$(document).ready(function() {
    fillRecipeToSave(recipe_to_display);

    $("#image-input").on("change", function() {
        previewImage(this);
    });

    /* Modal Listeners */
    $(".close-btn").on("click", function() {
        $(".modal").css({"display": "none"});
    });

     /* Add Difficulty Listeners */
     $("#easy, #intermediate, #hard").on("click", function(e) {
         e.preventDefault()
         recipeToSave.difficulty = $(this).html()
        //  $(this).toggleClass("selected");
     });

     /* Add Ingredient Listeners */
    $("#add-ingredient").on("click", function(e) {
        e.preventDefault();
        $("#ingredient-modal").css({"display": "block"});
    });

    $("#ingredient-save").on("click", function(e) {
        e.preventDefault();
        ingredientInputCheck();
    });

    $("#ingredient-name, #ingredient-amount, #ingredient-unit, #instruction-text").on("keyup", function() {
        removeOrange($(this));
        $(this).next().text('');
    });

    /* Add Instruction Listeners */
    $("#add-instruction").on("click", function(e){
        e.preventDefault();
        $("#instruction-modal").css({"display": "block"});
    });

    $("#instruction-save").on("click", function(e){
        e.preventDefault();
        instructionInputCheck();
    });

    /*   Submit Listeners  */
    $("#recipe-submit").on("click", function(e) {
        e.preventDefault();
        if(recipeInputCheck()) {
            saveRecipe();
        };
    });
    $("#title-input, #description-input, #servings-input, #prep-input, #cook-input, #cuisine-input").on("keyup", function() {
        removeOrange($(this));
        $(this).next().text('');
    })
});

