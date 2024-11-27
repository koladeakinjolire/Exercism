"""Functions which helps the locomotive engineer to keep track of the train."""

test_1a = (1,5,2,7,4)
test_1b = (1,5)
test_1c = (1,)
def get_list_of_wagons(args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    result = []
    for item in args:
        result.append(item)

    return result

print(get_list_of_wagons(test_1a))
print(get_list_of_wagons(test_1b))
print(get_list_of_wagons(test_1c))

test_2a = [2, 5, 1, 7, 4, 12, 6, 3, 13]
test_2b = [3, 17, 6, 15]
test_2c = [3, 27, 1, 14, 10, 4, 12, 6, 23, 17, 13, 22, 28, 19]
test_2d = [8, 10, 5, 9, 36, 7, 20]
test_2e = [4, 2, 1]
test_2f = [8, 6, 15]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """


    a, b, c, *rest = each_wagons_id
    d = missing_wagons
    combined_list = c, *d, *rest, a, b
    
    return list(combined_list)
    
    
print(fix_list_of_wagons(test_2a, test_2b))
print(fix_list_of_wagons(test_2c, test_2d))
print(fix_list_of_wagons(test_2e, test_2f))



test_3a = {'from': 'Berlin', 'to': 'Hamburg'}
test_3b = {'stop_1': 'Lepzig', 'stop_2': 'Hannover', 'stop_3': 'Frankfurt'}
test_3c = {'from': 'Paris', 'to': 'London'}, {'stop_1': 'Lille'}
test_3d = {'from': 'New York', 'to': 'Philadelphia'},{}
test_3e = {'from': 'Gothenburg', 'to': 'Copenhagen'}
test_3f = {'stop_1': 'Kungsbacka', 'stop_2': 'Varberg', 'stop_3': 'Halmstad', 'stop_4': 'Angelholm', 'stop_5': 'Lund', 'stop_6': 'Malmo'}

def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    a, b = dict(**route)
    c, d = route.values()
    city_list = []
    for city in stops.values():
        city_list.append(city)

    updated_route = {a:c, b:d, 'stops':city_list}
    return updated_route


print(add_missing_stops(test_3a, **test_3b))
print(add_missing_stops(test_3e, **test_3f))

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    new_route_info = {**route, **more_route_information}
    return new_route_info 

test_5 = [[(2, 'red'), (4, 'red'), (8, 'red')], [(5, 'blue'), (9, 'blue'), (13, 'blue')], 
[(3, 'orange'), (7, 'orange'), (11, 'orange')]]

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    result = []
    for items in zip(*wagons_rows):
        result.append(list(items))
        
    return result

print(fix_wagon_depot(test_5))
print(test_5[0])