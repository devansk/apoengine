from core.player import Gracz
from core.monsters import Monster
from core.fight import Fight
from core.quests import Quests

import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'misc')))
from log_system import log

def main():
    #gracz1 = Gracz()
    gracz1 = Gracz.load_from_file()
    #print(gracz1.level)
    #gracz1.add_item(0,"healing")  # Example item ID
    #gracz1.show_inventory()  
    # Add more functionality here as needed
    #gracz1.add_experience(150)  # Example of adding experience
    #print(f"Gracz {gracz1.name} ma teraz {gracz1.experience} doświadczenia i jest na poziomie {gracz1.level}.")
    #gracz1.increase_skills(attribute='a', amount=5)  # Increase health by 5
    #print(f"Gracz {gracz1.name} ma teraz {gracz1.get_attack()} ataku.")
    #gracz1.save_to_file()  # Save the player's state to a file

    # Example of creating a monster
    monster = Monster(0)  # Load monster with ID 1

    # Example of starting a fight
    fight = Fight(gracz1, monster)
    winner = fight.start()
    #quest = Quests().get_quest_by_id(quest_id=2,player=gracz1)  # Get quest with ID 1


if __name__ == "__main__":
    main()