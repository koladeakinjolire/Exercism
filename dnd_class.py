import random

class Character:
    def __init__(self, abilities=None):
        if abilities is None:
            abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

        self.abilities = abilities
        for ability in abilities:
            setattr(self, ability, self.roll_ability_score())

        self.hitpoints = 10 + modifier(self.constitution)
        
        
    def roll_ability_score(self):
            rolls = [random.randint(1, 6) for _ in range(4)]
            return sum(sorted(rolls)[1:])  # Drop the lowest roll

    def ability(self):
           return self.roll_ability_score()
            
        
def modifier(value):
    return (value - 10) // 2

if __name__ == '__main__':
    character = Character()
    print('Abilities:', {ability: getattr(character, ability) for ability in character.abilities})
    print("Hit points:", character.hitpoints)
    print("Constitution modifier:", modifier(character.ability('constitution')))