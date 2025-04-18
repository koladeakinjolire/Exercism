"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

from sets_categories_data import (VEGAN_INTERSECTIONS,
                                  VEGETARIAN_INTERSECTIONS,
                                  PALEO_INTERSECTIONS,
                                  KETO_INTERSECTIONS,
                                  OMNIVORE_INTERSECTIONS)
dish_1 = 'Punjabi-Style Chole'
dish_ing1 = ['onions','fish','onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste',
            'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 
            'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric',
            'garam masala', 'chickpeas', 'ginger', 'cilantro']

def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    ingredients = set(dish_ingredients)
    result = (dish_name, ingredients)
    return result

#print(clean_ingredients(dish_1, dish_ing1))

test_2a = 'Honeydew Cucumber'
test_2b =  ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']
test_2c = 'Shirley Tonic'
test_2d = ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 
           'sugar', 'club soda']

def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on 
    `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) 
    and drink
    name followed by "Cocktail" (includes alcohol).

    """
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return str(drink_name + ' Mocktail')
    else:
        return str(drink_name + ' Cocktail')

print(check_drinks(test_2a, test_2b))
print(check_drinks(test_2c, test_2d))

def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    categories = (VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE)
    cat1, cat2, cat3, cat4, cat5 = categories
    for ingredients in categories:
        if dish_ingredients.issubset(cat1):
            return dish_name +': ' + 'VEGAN'
        elif dish_ingredients.issubset(cat2):
            return dish_name +': ' + 'VEGETARIAN'
        elif dish_ingredients.issubset(cat3):
            return dish_name +': ' + 'PALEO'
        elif dish_ingredients.issubset(cat4):
            return dish_name +': ' + 'KETO'
        else:
            return dish_name +': ' + 'OMNIVORE'

meal = ('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic',
                                        'brown sugar', 'sesame seeds', 'lemon juice'])
a, b = meal
#print(a)
def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    x, y = dish
    special_ingredients = SPECIAL_INGREDIENTS.intersection(y)
    return (x, special_ingredients)

print(tag_special_ingredients(meal))


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """

    master_set = set() 
    for ingredient_set in dishes:
        master_set.update(ingredient_set)
        master_set.union(ingredient_set)
        
    return master_set


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    not_appetizers = set(dishes).difference(appetizers)
    return list(not_appetizers)


example_dishes = [
                  {'salt', 'breadcrumbs', 'water', 'flour', 'celeriac', 'chickpea flour', 'soy sauce', 'parsley',
                   'sunflower oil', 'lemon', 'black pepper'},

                  {'cornstarch', 'salt', 'vegetable oil', 'sugar', 'vegetable stock', 'water', 'tofu', 'soy sauce',
                   'lemon zest', 'lemon juice', 'black pepper', 'ginger', 'garlic'},

                  {'salt', 'mixed herbs', 'silken tofu', 'smoked tofu', 'nutritional yeast', 'turmeric', 'soy sauce',
                   'garlic', 'lemon juice', 'olive oil', 'black pepper', 'spaghetti'},

                  {'salt', 'mushrooms', 'sugar', 'barley malt', 'nutritional yeast', 'fresh basil', 'olive oil',
                   'honey', 'yeast', 'red onion', 'bell pepper', 'cashews', 'oregano', 'rosemary', 'garlic powder',
                   'tomatoes', 'water', 'flour', 'red pepper flakes', 'garlic'},

                  {'mango powder', 'oil', 'salt', 'cardamom powder', 'fresh red chili', 'sugar', 'fresh ginger',
                   'turmeric', 'red chili powder', 'curry leaves', 'garlic paste', 'mustard seeds', 'vinegar',
                   'mashed potatoes', 'garam masala', 'mangoes', 'nigella seeds', 'clove powder', 'serrano chili',
                   'cumin powder', 'onion', 'water', 'chickpea flour', 'coriander seeds', 'turmeric powder', 'hing',
                   'coriander powder', 'cinnamon powder', 'cilantro', 'garlic'},

                  {'mango powder', 'oil', 'salt', 'cardamom powder', 'fresh red chili', 'sugar', 'fresh ginger',
                   'turmeric', 'red chili powder', 'curry leaves', 'garlic paste', 'mustard seeds', 'vinegar',
                   'mashed potatoes', 'garam masala', 'mangoes', 'nigella seeds', 'clove powder', 'serrano chili',
                   'cumin powder', 'onion', 'water', 'chickpea flour', 'coriander seeds', 'turmeric powder', 'hing',
                   'coriander powder', 'cinnamon powder', 'cilantro', 'garlic'}
                  ]


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    singleton_ingredients = set()
    for dish in dishes:
        singleton_ingredients.update(dish - intersection)

    return singleton_ingredients 

print(singleton_ingredients(example_dishes, VEGAN_INTERSECTIONS))
    
