def recite(start_verse, end_verse):
    verse_dictionary = {
        1: 'and a Partridge in a Pear Tree.',
        2: 'two Turtle Doves, and a Partridge in a Pear Tree.',
        3: 'three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        4: 'four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        5: 'five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        6: 'six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        7: 'seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        8: 'eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        9: 'nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        10: 'ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        11: 'eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
        12: 'twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'
    }

    day_dictionary = {
        1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth',
        7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'
    }

    result = []
    for verse in range(start_verse, end_verse + 1):
        # Build the verse
        verse_text = f"On the {day_dictionary[verse]} day of Christmas my true love gave to me: "
        if verse == 1:
            verse_text += "a Partridge in a Pear Tree."
        else:
            verse_text += verse_dictionary[verse]
        result.append(verse_text)

    return result
print(recite(1, 1))
print(recite(2, 2))
print(recite(3, 3)) 
print(recite(1, 4))
print(recite(2, 5))
print(recite(3, 6))
print(recite(1, 12))