def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError('input out of range')
    if number == 0:
        return 'zero'
    # Define words for ones, teens, and tens
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    # Helper function to convert a number less than 1000
    def three_digit_to_words(number):
        words = ""
        if number >= 100:
            words += ones[number // 100] + " hundred"
            number %= 100
            if number:
                words += " "
        if number >= 20:
            words += tens[number // 10]
            number %= 10
            if number:
                words += "-" + ones[number]
        elif number >= 10:
            words += teens[number - 10]
        elif number > 0:
            words += ones[number]
        return words

    parts = []
    # Process billions
    if number >= 1_000_000_000:
        billions = number // 1_000_000_000
        parts.append(three_digit_to_words(billions) + " billion")
        number %= 1_000_000_000

    # Process millions
    if number >= 1_000_000:
        millions = number // 1_000_000
        parts.append(three_digit_to_words(millions) + " million")
        number %= 1_000_000

    # Process thousands
    if number >= 1_000:
        thousands = number // 1_000
        parts.append(three_digit_to_words(thousands) + " thousand")
        number %= 1_000

    # Process the last three digits
    if number:
        parts.append(three_digit_to_words(number))

    return " ".join(parts)

