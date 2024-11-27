def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    for i in range(number):
        yield chr(ord('A') + i % 4)
    
         
seat_letters = generate_seat_letters(9)
print(next(seat_letters))

number = 21
number_list = [1]
number_list += [i for i in range(1,number) if i != 1 and i != 13]
print(number_list)


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    row_number = 1
    seat_index = 0
    seat_letters = "ABCD"
    for _ in range(number):
        seat_identifier = f"{row_number}{seat_letters[seat_index]}"
        yield seat_identifier
        seat_index +=1
        if seat_index == 4:
            seat_index = 0
            row_number += 1
        if row_number == 13:
            row_number += 1
            seat_index = 0

seat_number = generate_seats(10)   
print(next(seat_number))
print(next(seat_number))
print(next(seat_number))
print(next(seat_number))
print(next(seat_number))

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    row_number = 1
    seat_index = 0
    letters = 'ABCD'
    seat_assignments = {}
    for passenger in passengers:
        seat_identifier = f"{row_number}{letters[seat_index]}" #combines row number and seat letter into a single string
        seat_assignments[passenger] = seat_identifier #creates key-value pair with seat identifier as value and passenger as key
        
        seat_index += 1
        if seat_index == 4:
            seat_index = 0
            row_number += 1
            if row_number == 13:
                row_number += 1
                
    return seat_assignments
            
print(assign_seats(['Dele','Ayo','Giwa','Moore','Imani','Shelby']))

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket_code = f"{seat}{flight_id}"
        difference = 12 - len(ticket_code)
        ticket_code += '0' * difference
        yield ticket_code #yield is usually the last statement in a for loop when creating a generator 

seat_numbers = ['1A', '17D', '25B','34C']
flight_id = 'CO1234'
ticket_ids = generate_codes(seat_numbers, flight_id) #assign the generator method a variable and to call each iteration, use next

print(next(ticket_ids))
print(next(ticket_ids))
print(next(ticket_ids))
print(next(ticket_ids))
