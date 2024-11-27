"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    new_cart = current_cart.copy()
    for item in items_to_add:
        if item in new_cart:
            new_cart[item] += 1
        else:
            new_cart[item] = 1
    return new_cart 

test_notes = ('Apple', 'Banana','Banana','Banana','Banana')
test_notes_2 = ['Orange', 'Raspberry', 'Blueberries','Orange','Blueberries']
test_notes_3 = ('Broccoli', 'Kiwi','Broccoli','Kiwi', 'Melon', 'Apple', 'Melon','Melon','Banana')
test_notes_4 = ['Mango','Cherry','Guava','Tangerine','Pear']

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    result_dict = {}
    for item in notes:
       if isinstance(item, list):
            item = tuple(item)
    for item in notes:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] =  1


    return result_dict

print(read_notes(test_notes_2))

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart

cart_test = {'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2}
aisle_map_test = {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False],
                  'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_dict = {}
    for item, count in cart.items():
        aisle_info = aisle_mapping.get(item, [])
        fulfillment_dict[item] = [count] + aisle_info

    fulfillment_dict = dict(sorted(fulfillment_dict.items(), reverse=True))
    return fulfillment_dict

print(send_to_store(cart_test, aisle_map_test))

fulfillment_cart_test = {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True],
                  'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]}
store_inventory_test = {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False],
                  'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    updated_inventory = {}
    for key, location in store_inventory.items():
        if key in fulfillment_cart:
            new_quantity = store_inventory[key][0] - fulfillment_cart[key][0]
            updated_inventory[key] = [new_quantity] + location[1:]
        else:
                updated_inventory[key] = store_inventory[key]
    for key, location in updated_inventory.items():
        if location[0] == 0:
            location[0] = 'Out of Stock'

    
    return updated_inventory

print(update_store_inventory(fulfillment_cart_test, store_inventory_test))
