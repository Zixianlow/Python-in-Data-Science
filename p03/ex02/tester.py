from DiamondTrap import King
from S1E9 import Character, Stark
from S1E7 import Baratheon, Lannister
Joffrey = King("Joffrey")
print(Joffrey.__dict__)
print(Joffrey.__doc__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.__dict__)
if(isinstance(Joffrey, King) and issubclass(King, Character)and issubclass(King, Lannister) and issubclass(King, Baratheon)):
    print("OK")
