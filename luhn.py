class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if not isinstance(self.card_num, str):
            return False

        cleaned_num = self.card_num.replace(" ", "")
        if len(cleaned_num) <= 1:
            return False
            
        if not cleaned_num.isdigit():
            return False

        number_list = [int(num) for num in cleaned_num]
        for i in range(len(number_list) - 2, -1, -2):
            product = number_list[i] * 2
            if product > 9:
                product -= 9
            number_list[i] = product

        return sum(number_list) % 10 == 0