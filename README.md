# ApoEngine One - Silnik gry tekstowej ☢️🧟‍♂️
15.08.2025

## Opis projektu
Projekt "ApoEngine" to silnik gry tekstowej RPG, w którym gracz wciela się w postać przetrwałego w świecie postapokaliptycznym. Silnik obsługuje system gracza, ekwipunku, przedmiotów, potworów, walki, zadań oraz logowania zdarzeń. 

🌍🧑‍🚀 Przetrwaj, rozwijaj postać, walcz z potworami i wykonuj zadania w świecie po zagładzie!

## Stan funkcjonalny

### 👤 Klasa Gracz
- 📝 Obsługa tworzenia, wczytywania i zapisywania stanu gracza
- 🎒 Możliwość dodawania przedmiotów do ekwipunku
- ⬆️ System poziomów i rozwoju statystyk

### 🗡️ Klasa Przedmiot (Items)
- 📦 Wczytywanie przedmiotów z pliku JSON
- 🧪 Obsługa różnych typów przedmiotów (np. broń, mikstury)
- 🔍 Wyszukiwanie przedmiotów po ID i typie
- 🎲 Obsługa dropu przedmiotów i szansy na drop



### 🎒 Klasa Ekwipunek (Inventory)
- 💾 Wczytywanie i zapisywanie stanu ekwipunku do pliku
- 🔢 Obsługa ilości przedmiotów (np. 2x mikstura zdrowia)
- ➕ Dodawanie i zwiększanie ilości przedmiotów
- 👀 Wyświetlanie ekwipunku gracza

### 👹 Klasa Potwór (Monster)
- 🧬 Wczytywanie potworów z pliku JSON
- 🆔 Tworzenie obiektu potwora na podstawie ID
- 🩸 Dostęp do atrybutów potwora przez gettery (np. get_health())
- 🎲 Obsługa dropu przedmiotów i szansy na drop

### ⚔️ Klasa Walka (Fight)
- 🤼‍♂️ Wstępna obsługa walki między graczem a potworem
- 💥 System obrażeń, ataku, obrony
- 🎲 Obsługa dropu przedmiotów i szansy na drop

### 📜 Klasa Zadania (Quests)
- 📂 Wczytywanie i obsługa zadań z pliku JSON
- 🧑‍💼 Przypisywanie zadań do gracza

### 📝 System logowania
- 🗒️ Logowanie zdarzeń do pliku lub konsoli
- 🚦 Różne poziomy logów (informacje, błędy, zmiany stanu)

## 🚧 Plany rozwoju
- 👥 Obsługa wielu postaci gracza (sloty zapisu)
- 🔄 Możliwość wyboru postaci
- 🎒 Dodatkowe ekwipunki dla innych postaci
- 🧟‍♂️ Rozbudowa klasy walka i potwór
- 🗺️ Dodanie klasy mapa, 🛒 sklep
- 🏆 Rozbudowa systemu zadań
- stworzyc mapy/poziomy 
- stworzyc listy potworow przynalzne do danej mapy

## 📁 Struktura katalogów
- `core/` - logika gry (gracz, ekwipunek, przedmioty, potwory, walka, zadania)
- `assets/` - pliki danych (przedmioty, potwory, zadania)
- `saves/` - zapisy gry i ekwipunku
- `misc/` - logowanie i inne narzędzia

## 🚀 Uruchomienie
1. 🐍 Upewnij się, że masz Pythona 3.8+.
2. ▶️ Uruchom plik `main.py`:
   ```bash
   python main.py
   ```

## 👨‍💻 Autor
Projekt stworzony do nauki programowania i rozwoju własnego silnika gry tekstowej.
