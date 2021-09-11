import random

ABILITIES = {'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma'}

class Character:
    def __init__(self) -> None:
        for ab in ABILITIES:
            setattr(self, ab, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)
    
    def ability(self) -> int:
        return sum(sorted(random.randint(1, 6) for i in range(4))[1:])

def modifier(constitution: int) -> int:
    return (constitution - 10) // 2