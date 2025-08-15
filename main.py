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
    #print(gracz1.level)
    #gracz1.add_item(0,"healing")  # Example item ID
    #gracz1.show_inventory()  
    # Add more functionality here as needed
    #gracz1.add_experience(150)  # Example of adding experience
    #print(f"Gracz {gracz1.name} ma teraz {gracz1.experience} doświadczenia i jest na poziomie {gracz1.level}.")
    #gracz1.increase_skills(attribute='a', amount=5)  # Increase health by 5
    #print(f"Gracz {gracz1.name} ma teraz {gracz1.get_attack()} ataku.")
    #gracz1.save_to_file()  # Save the player's state to a file
    #quest = Quests().get_quest_by_id(quest_id=2,player=gracz1)  # Get quest with ID 1


    gracz1 = Gracz.load_from_file() # Wczytanie danych gracza z pliku
    monster = Monster(0)  # Wczytanie danych przeciwnika o id 0 z pliku
    fight = Fight(gracz1, monster) # Organizowanie walki pomiedzy graczem a przeciwnikiem o id 0
    winner = fight.start() # Rozpoczecie walki i przypisanie wyniku walki do zmiennej winner
    print(winner)



if __name__ == "__main__":
    main()