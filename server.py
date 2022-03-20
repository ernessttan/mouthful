from turtle import update
from venv import create
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

recipes = {
    0: {
        "id": 0,
        "title": "Kimchi Spam Rice",
        "image": "/static/images/kimchi_rice.jpg",
        "difficulty": "Easy", 
        "rating": 4.8, 
        "preptime": 10, 
        "cooktime": 10, 
        "totaltime": 20,
        "servings": 2,
        "cuisine": "Korean",  
        "description": "If you have some kimchi and rice, try this easy kimchi fried rice recipe! Super tasty and super easy! Itll become one of your go-to easy meals. We guarantee it.", 
        "ingredients": ["Rice", "Half Block Spam", "Spring Onions", "Kimchi" ], 
        "instructions": ["Start by cooking the rice in a rice cooker.", "Chop spam, kimchi and spring onions", "Start heating a pan over high heat", "Throw in the chopped kimchi and diced spam. Stir fry it until semi-dry.", "Scoop a bowl of rice and place the kimchi and spam mix around the the center."]
    },
    1: {
        
        "id": 1,
        "title": "Udon Carbonara",
        "image": "/static/images/udon_carbonara.jpg", 
        "difficulty": "Easy",
        "rating": 4.7, 
        "preptime": 5, 
        "cooktime": 10,
        "totaltime": 15,
        "servings": 2,
        "cuisine": "Japanese",  
        "description": "Love Italian and Japanese food? Here's a recipe that'll satisfy both cravings. Easy, filling and yummy!", 
        "ingredients": ["2 Packet Udon", "4 Eggs", "1/2 cup grated parmigiano reggiano", "3 strips of sliced bacon", "seaweed" ], 
        "instructions": ["Start by separating 3 egg yolks and 1 egg into a bowl.", "Grate your cheese into another bowl and whisk together eggs, cheese, salt, and pepper.", "In a nonstick pan, fry the bacon bits until they are crispy. Set bacon aside.", "In a nonstick pan, fry the bacon bits until they are crispy. Set bacon aside.", "In a pot, throw in your udon noodles until they have loosened. Be careful not to overcook them and strain immediately..", "Set aside some of the udon water for later.", "In the same pan, mix your udon and bacon together over low heat. Turn off the heat and add in your egg mixture, mix well.", "Transfer to a serving plate and garnish with Togarashi and seaweed."]
    },
    2: {
        "id": 2,
        "title": "Chicken Alfredo Pasta",
        "image": "/static/images/chicken_alfredo.jpg",
        "difficulty": "Easy", 
        "rating": 4.5, 
        "preptime": 10, 
        "cooktime": 20,
        "totaltime": 30,
        "servings": 4,
        "cuisine": "Italian", 
        "description": "Nothing spells comfort like Italian food. This creamy, protein-packed and delicious pasta will bring you comfort at any time of the day. It's so simple that it'll only take you less than 30 minutes (that's shorter than one episode of Breaking Bad).", 
        "ingredients": ["3/4 lb. pasta fettuccine", "1 lb. chicken breast, boneless and skinless", "Salt and pepper to taste", "3 garlic cloves, minced", " 1 teaspoon dried oregano", "3 tablespoons cream cheese, softened", "1 1/2 cup heavy cream", "3/4 cup grated parmesan cheese", "1 tablespoon extra virgin olive oil ", "2 tablespoons butter, softened"], 
        "instructions": ["Season the chicken with salt and pepper to taste.", "Warm the butter and olive oil in a nonstick frying pan over medium heat and cook the chicken on each side for about 8-10 minutes. Sprinkle with dried oregano.", "Remove the chicken from the pan and let it rest covered with aluminium foil.", "Meanwhile, bring a pot with salted boiling water and cook the fettuccine for about 5 minutes or until al dente.", "In the same pan where the chicken was cooked, stir in the minced garlic, heavy cream, parmesan cheese and cream cheese.", "Mix on medium heat and whisk until all creamy and combined.", "Stir the cooked fettuccine into the sauce and cook for about 2 minutes.", "Finally, dice the chicken and arrange on top of the cooked pasta.", "Decorate with fresh basil leaves if desired.", "Serve and enjoy."]
    },
    3: {
        "id": 3,
        "title": "Chicken Parmesan Casserole",
        "image": "/static/images/chickenparm.jpg", 
        "difficulty": "Intermediate",
        "rating": "3", 
        "preptime": 20, 
        "cooktime": 10,
        "totaltime": 30, 
        "servings": 4,
        "cuisine": "Italian", 
        "description": "Yummy Chicken Parm, Super Cheesy and Comforting.", 
        "ingredients": ["1 lb. chicken breast, boneless and skinless", "Salt and pepper to taste", "1 teaspoon dried oregano", "3 oz. grated cheddar cheese", "2 oz. grated parmesan cheese", "3 tablespoons cream cheese, softened", "1 1/2 cup heavy cream"], 
        "instructions": ["Season the chicken breasts with salt and pepper to taste, garlic powder and dried oregano.","Warm the oil in a nonstick frying pan over medium heat and cook them for about 5 minutes on each side.", "Grease a casserole pan with little bit of butter and place some of the tomato sauce.","Arrange the cooked chicken breasts on top of the tomato sauce and top them with the rest of the tomato sauce.", "Sprinkle some grated cheese and grated parmesan and sprinkle dried oregano just right before baking.", "Bake in an already heated oven at 350 F or 180 C degrees for about 25-30 minutes or until the cheese is melted and golden brown in color.",  "Serve with a simple mixed greens salad mixed with lemon juice, olive oil, balsamic vinegar and salt and pepper to taste.", "Enjoy."]
    },
    4: {
        "id": 4,
        "title": "Beef Bourguignon",
        "image": "/static/images/beefbourguinon.jpg", 
        "difficulty": "Intermediate",
        "rating": "5", 
        "preptime": 20, 
        "cooktime": 30,
        "totaltime": 50, 
        "servings": 4,
        "cuisine": "French", 
        "description": "Great for a wintery day", 
        "ingredients": ["1 3/4 lb. beef meat, cut into chunks", "2 tablespoons butter", "3 oz. bacon, diced", "1 onion, diced into fine pieces", "2 oz. mushrooms, whole", "3 carrots, peeled and diced into 1 inch cubes", "3 medium sized potatoes, diced into cubes"], 
        "instructions": ["Warm the olive oil and butter in a nonstick pot over medium heat.", "Start cooking the diced onion and diced bacon together for about 5 minutes.","Stir in the diced beef and mushrooms and cook for about 10-15 minutes until the meat is golden brown in color.","Then, stir in the diced carrots, potatoes and season with salt and pepper to taste, dried oregano, paprika powder, garlic powder and tomato paste.","Mix until combined and stir in the red wine.", "Pour in the water and cook for about 25 minutes.","Mix the cornstarch with the water and pour the slurry into the stew whisking all the way through until the mixture thickness slightly.","Serve and enjoy."]
    },
    5: {
        "id": 5,
        "title": "Miso-Butter Roast Chicken With Acorn Squash Panzanella",
        "image": "/static/images/misobutterroastchicken.jpg", 
        "difficulty": "Intermediate",
        "rating": "3", 
        "preptime": 10, 
        "cooktime": 20,
        "totaltime": 30, 
        "servings": 4,
        "cuisine": "Fusion", 
        "description": "Fusion Flavors", 
        "ingredients": ['(3 1/4-lb.) whole chicken', '2 tsp. kosher salt, divided, plus more', '2 small acorn squash (about 3 lb. total)', '2 Tbsp. finely chopped sage', '1 Tbsp. finely chopped rosemary', '6 Tbsp. unsalted butter, melted, plus 3 Tbsp. room temperature', '1/4 tsp. ground allspice', 'Pinch of crushed red pepper flakes', 'Freshly ground black pepper', '1/3 loaf good-quality sturdy white bread, torn into 1" pieces (about 2 1/2 cups)', '2 medium apples (such as Gala or Pink Lady; about 14 oz. total), cored, cut into 1" pieces', '2 Tbsp. extra-virgin olive oil', '1/2 small red onion, thinly sliced', '3 Tbsp. apple cider vinegar', '1 Tbsp. white miso', '1/4 cup all-purpose flour', '2 Tbsp. unsalted butter, room temperature', ' 3/4 cup dry white wine', '2 cups unsalted chicken broth', '2 tsp. white miso', 'Kosher salt, freshly ground pepper'], 
        "instructions": ["Pat chicken dry with paper towels, season all over with 2 tsp. salt, and tie legs together with kitchen twine. Let sit at room temperature 1 hour.","Meanwhile, halve squash and scoop out seeds. Run a vegetable peeler along ridges of squash halves to remove skin. Cut each half into 1/2 inch-thick wedges; arrange on a rimmed baking sheet.","Combine sage, rosemary, and 6 Tbsp. melted butter in a large bowl; pour half of mixture over squash on baking sheet. Sprinkle squash with allspice, red pepper flakes, and 1/2 tsp. salt and season with black pepper; toss to coat.","Add bread, apples, oil, and 1/4 tsp. salt to remaining herb butter in bowl; season with black pepper and toss to combine. Set aside.","Place onion and vinegar in a small bowl; season with salt and toss to coat. Let sit, tossing occasionally, until ready to serve.""Place a rack in middle and lower third of oven; preheat to 425F. Mix miso and 3 Tbsp. room-temperature butter in a small bowl until smooth. Pat chicken dry with paper towels, then rub or brush all over with miso butter. Place chicken in a large cast-iron skillet and roast on middle rack until an instant-read thermometer inserted into the thickest part of breast registers 155F, 50 to 60 minutes. (Temperature will climb to 165F while chicken rests.) Let chicken rest in skillet at least 5 minutes, then transfer to a plate; reserve skillet.","Meanwhile, roast squash on lower rack until mostly tender, about 25 minutes. Remove from oven and scatter reserved bread mixture over, spreading into as even a layer as you can manage. Return to oven and roast until bread is golden brown and crisp and apples are tender, about 15 minutes. Remove from oven, drain pickled onions, and toss to combine. Transfer to a serving dish.","Set reserved skillet with chicken drippings over medium heat. You should have about 1/4 cup, but a little over or under is all good. (If you have significantly more, drain off and set excess aside.) Add wine and cook, stirring often and scraping up any browned bits with a wooden spoon, until bits are loosened and wine is reduced by about half (you should be able to smell the wine), about 2 minutes.", "Add butter mixture; cook, stirring often, until a smooth paste forms, about 2 minutes.", "Add broth and any reserved drippings and cook, stirring constantly, until combined and thickened, 6 to 8 minutes. Remove from heat and stir in miso. Taste and season with salt and black pepper.","Serve chicken with gravy and squash panzanella alongside."]            
    },
    6: {
        "id": 6,
        "title": "Crispy Salt and Pepper Potatoes",
        "image": "/static/images/crispysaltpotato.jpg",
        "difficulty": "Easy", 
        "rating": "3", 
        "preptime": 10, 
        "cooktime": 10,
        "totaltime": 20, 
        "servings": 4,
        "cuisine": "Snack", 
        "description": "Tastes just like fries", 
        "ingredients": ['2 large egg whites', '1 pound new potatoes (about 1 inch in diameter)', '2 teaspoons kosher salt', '3/4 teaspoon finely ground black pepper', '1 teaspoon finely chopped rosemary', '1 teaspoon finely chopped thyme', '1 teaspoon finely chopped parsley'], 
        "instructions": ["Preheat oven to 400F and line a rimmed baking sheet with parchment. In a large bowl, whisk the egg whites until foamy (there shouldn’t be any liquid whites in the bowl)." "Add the potatoes and toss until they’re well coated with the egg whites, then transfer to a strainer or colander and let the excess whites drain.", "Season the potatoes with the salt, pepper, and herbs.", "Scatter the potatoes on the baking sheet (make sure they’re not touching) and roast until the potatoes are very crispy and tender when poked with a knife, 15 to 20 minutes (depending on the size of the potatoes).","Transfer to a bowl and serve."]
    },
    7: {
        "id": 7,
        "title": "Baked Banana With Crema and Cheese",
        "image": "/static/images/bakedbanana.jpg",
        "difficulty": "Easy", 
        "rating": "4", 
        "preptime": 10, 
        "cooktime": 10,
        "totaltime": 20, 
        "servings": 3,
        "cuisine": "French", 
        "description": "Cheese Cream and Bananas, what could go wrong?", 
        "ingredients": ['1/2 cup (1 stick) unsalted butter', '1/2 cup (65 g) raw pistachios, divided', '1 large egg', '1/4 cup (packed 50 g) light brown sugar', '2 cups (250 g) all purpose flour', '1 tsp. kosher salt', '3/4 tsp. baking powder', '3 large eggs', '2/3 cup (packed; 133 g) light brown sugar', '1/4 cup sour cream', '1 Tbsp. vanilla bean paste or vanilla extract', '1 tsp. ground cardamom', '3/4 tsp. ground ginger', '3/4 tsp.(packed) finely grated orange zest', '3/4 tsp. kosher salt', '3 Tbsp (23 g) all purpose flour', '2 1/2 lb. stone fruit (such as peaches, nectarines, apricots, and plums; all about the same size), cut into sixths or eighths, depending on their size', '1 Tbsp. coarse sugar', 'Powdered sugar, whipped cream, or creme fraiche (for serving optional)', 'A 9 inch diameter springform pan'], 
        "instructions": ["Preheat the oven to 400°F.", "Place the whole bananas or plantains on a baking sheet and bake, turning them every 10 minutes, until the peel starts to split and the inside is tender when tested with a skewer, about 40 minutes.", "Remove from the oven but keep on the baking sheet. Carefully slice the peel lengthwise to just reveal the flesh and drizzle with some crema and sprinkle with cheese.", "Transfer to plates to serve individually, on a platter, or directly on the baking sheet on the table.", "Either way, people should carve out their own banana. Serve the remaining crema and cheese in bowls on the side, in case anyone wants more."]
    },
    8: { 
        "id": 8,
        "title": "Okonomiyaki",
        "image": "/static/images/okonomiyaki.jpg",
        "difficulty": "Intermediate", 
        "rating": "4", 
        "preptime": 20, 
        "cooktime": 10,
        "totaltime": 30, 
        "servings": 2,
        "cuisine": "Japanese", 
        "description": "Yummy Japanese Pancakes", 
        "ingredients": ['1 1/2 cups (180 g) all-purpose flour', '1 teaspoon baking powder', '1/4 teaspoon sea salt', '1 large egg, beaten', '1 1/4 cups (296 ml) whole milk or milk of your choice', '8 ounces (230 g) cabbage, thinly sliced', '2 scallions, white and light green parts chopped', '1/2 yellow, green, or red bell pepper, thinly sliced', '4 tablespoons vegetable oil', '8 ounces (230 g) boneless chicken, shrimp, crab, or sukiyaki-style beef or pork, cut into 1/2-inch (12 mm) pieces', '2 tablespoons mayonnaise', '2 tablespoon or more homemade or store-bought Tonkatsu Sauce', '1/2 cup (4 g) bonito flakes', '1/2 cup (4 g) crumbled nori'], 
        "instructions": ["Whisk together the flour, baking powder, and salt in a small bowl.In a medium bowl, whisk the egg and milk.", "Add the flour mixture and mix until just blended. The batter should be quite thin.", "Add the chopped vegetables to the batter and mix well.", "Heat 1 tablespoon of the oil in a medium non- stick skillet over medium-high heat.", "The batter should be quite thin. Add the chopped vegetables to the batter and mix well.Heat 1 tablespoon of the oil in a medium non- stick skillet over medium-high heat.", "Turn heat to low and cook until the bottom of the pancake is browned, the meat is thoroughly cooked, and the vegetables are tender—about 10 minutes.", "Repeat until the batter is used up.", "To serve, brush the pancake with mayonnaise and tonkatsu sauce, or soy sauce. Sprinkle with the bonito flakes and crumbled nori. Eat while piping hot."]
    },
    9: {
        "id": 9,
        "title": "Crispy Sheet-Pan Broccoli",
        "image": "/static/images/crispybroccoli.jpg", 
        "difficulty": "Easy",
        "rating": "4", 
        "preptime": 10, 
        "cooktime": 10,
        "totaltime": 20, 
        "servings": 4,
        "cuisine": "Snack", 
        "description": "Healthy and Easy", 
        "ingredients": ['3 large heads broccoli (3 1/2 to 4 pounds total), trimmed, cut into florets with some stalk attached (cut the florets in half if large)', '1/2 cup olive oil', 'Kosher salt', 'Freshly ground black pepper'], 
        "instructions": ["Set the racks in the upper and lower thirds of the oven and preheat it to 425°F.","Line two large rimmed baking sheets with parchment paper. Divide the broccoli between the sheets, arranging them in a single layer.", "Drizzle each sheet of broccoli with 1/4 cup oil, then season each with 1/2 teaspoon salt and a few grinds of pepper.", "Roast, stirring once and rotating the sheets halfway through, until the broccoli is crispy and charred in spots, 35 to 40 minutes.", "Taste and adjust the seasoning, if desired."]
    } 
}


# Home Page Route #
@app.route('/')
def home():
    return render_template('home.html', recipes=recipes)

# Search Results Route #
@app.route('/search/<search_entry>', methods=['GET', 'POST'])
def search(search_entry=None):
    search_results = {
        "message": "Showing Results For " + search_entry,
        "result": []
    }
    for key, value in recipes.items():
        recipe = value
        recipe_title = recipe["title"].lower()
        if search_entry in recipe_title:
            print(recipe)
            search_results["result"].append(recipe)
    return render_template('searchresults.html', search_results = search_results)

@app.route('/view_recipe/<id>', methods=['GET', 'POST'])
def view_recipe(id=None):
    recipe_to_display = []
    for key, value in recipes.items():
        recipe = value
        recipe_id = recipe["id"]
        if int(recipe_id) == int(id):
            recipe_to_display.append(recipe)
    return render_template("recipepage.html", recipe_to_display = recipe_to_display)


if __name__ == '__main__':
   app.run(debug = True)