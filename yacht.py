# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    dice_dict = {num: dice.count(num) for num in dice}
            
    if category == 'YACHT':
       return 50 if len(set(dice)) == 1 else 0
            
    if category == 'ONES':
        if 1 in dice_dict.keys():
            return dice.count(1) * 1
        else:
            return 0
                
    if category == 'TWOS':
        if 2 in dice_dict.keys():
            return dice.count(2) * 2
        else:
            return 0

    if category == 'THREES':
       if 3 in dice_dict.keys():
            return dice.count(3) * 3
       else:
            return 0
            
    if category == 'FOURS':
        if 4 in dice_dict.keys():
            return dice.count(4) * 4
        else:
            return 0

    if category == 'FIVES':
        if 5 in dice_dict.keys():
            return dice.count(5) * 5
        else:
            return 0
            
    if category == 'SIXES':
        if 6 in dice_dict.keys():
            return dice.count(6) * 6
        else:
            return 0
                
    if category == 'FULL_HOUSE':
        counts = sorted(dice_dict.values())
        if counts == [2,3]:
            return sum(dice)
        else:
            return 0

    if category == 'FOUR_OF_A_KIND':
        for num, count in dice_dict.items():
            if count >= 4:
                return num * 4
            else:
                return 0

    if category == 'LITTLE_STRAIGHT':
        if 6 not in sorted(dice) and len(set(dice)) == 5:
            return 30
        else:
            return 0
            

    if category == 'BIG_STRAIGHT':
        if 1 not in sorted(dice) and len(set(dice)) == 5:
            return 30
        else:
            return 0

    if category == 'CHOICE':
        return sum(dice)

    return 0 
    
    