import re
class PhoneNumber:
    def __init__(self, number):
        number = number.strip()
        number = re.sub(r'[+-.()\ ]', "", number)
        if any(char in ',@?!:;' for char in number):
            raise ValueError("punctuations not permitted")
        if any(char.isalpha() for char in number):
            raise ValueError("letters not permitted")
        
        if len(number) > 11:
            raise ValueError('must not be greater than 11 digits')
        if len(number) < 10:
            raise ValueError('must not be fewer than 10 digits')
        if len(number) == 11:
            if number[0] == '1':
                number = number[1:]
            else:
                raise ValueError('11 digits must start with 1')
           
            
            
        
        self.number  = number 
        self.area_code = number[:3]
        if self.area_code[0] == '0':
            raise ValueError("area code cannot start with zero")
        if self.area_code[0] == '1':
            raise ValueError("area code cannot start with one")
            

        self.exchange_code = number[3:6]
        if self.exchange_code[0] == '0':
            raise ValueError("exchange code cannot start with zero")
        if self.exchange_code[0] == '1':
            raise ValueError("exchange code cannot start with one")

        self.local_number = number[3:]
        
    def test_area_code(self):
        return self.area_code

    def pretty(self):
        result = ''
        new_area_code = '(' + self.area_code + ')'
        local_part1 = self.local_number[:3]
        local_part2 = self.local_number[3:]
        result = new_area_code + '-' + local_part1 + '-' + local_part2
        return result