# Laboratorium z eksploracji danych - problem 3

To zadanie dotyczy problemu klasyfikacji tekstu. Tym razem nie będzie to zwykły tekst, a kod programu. Kod został napisany przez człowieka, albo model sztucznej inteligencji. Waszym zadaniem jest zbudowanie klasyfikatora, który rozpoznaje kto jest twórcą - AI, czy programista. W tym zadaniu wyznaczone są następujące progi punktowe:

| F1 | Punktacja |
| :----:  | :----: |
| 0.6+ | 15 |
| 0.9+ | 20 | 
| 0.95+ | 22.5 |
| 0.99+ | 25 |


Zadanie jest realizowane na podstawie [zadania](https://www.kaggle.com/datasets/daniilor/semeval-2026-task13) 13 z tegorocznej edycji SemEvala (workshopu przy ACL). 

# Instrukcja obsługi

1. Sklonuj repozytorium
2. Utwórz środowisko wirtualne (np. `python -m venv venv`)
3. Pobierz minimalny zestaw bibliotek (`pip install -r requirements.txt`)
4. Pobierz dane (`python data/download.py`)

# Interfejs zadania

Przykładowe, bardzo proste rozwiązanie znajduje się w pliku src/simple_solution.py. Wykorzystaj ten sam schemat rozwiązania. W tym samym pliku znajduje się fragment oznaczony jako ewaluacja. Ten sposób ewaluacji zostanie wykorzystany do oceny rozwiązania.

