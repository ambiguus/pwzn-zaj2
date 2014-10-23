# -*- coding: utf-8 -*-

import pickle
import pathlib


def load_animals(large_dataset=False):
    """

    :param bool large_dataset: Jeśli wartość to True zwraca 1E6 zwierząt, w
                               przeciwnym razie 1E5. Test będzie odbywał się
                               przy 1E6 zwierząt.

    :return: Lista zwierząt
    """
    file_name = 'animals-small.bin' if not large_dataset else 'animals.bin'
    file = pathlib.Path(__file__).parent / file_name
    with open(str(file), 'rb') as f:
        return pickle.load(f)


def filter_animals(animal_list):
    """
    Jesteś informatykiem w firmie Noe Shipping And Handling. Firma ta zajmuje
    się międzykontynentalnym przewozem zwierząt.
    
    Dostałeś listę zwierząt które są dostępne w pobliskim zoo do transportu.

    Mususz z tej listy wybrać listę zwierząt które zostaną spakowane na statek,

    Lista ta musi spełniać następujące warunki:

    * Docelowa lista zawiera obiekty reprezentujące zwierzęta (tak jak animal_list)
    * Z każdego gatunku zwierząt (z tej listy) musisz wybrać dokładnie dwa
      egzemplarze.
    * Jeden egzemplarz musi być samicą a drugi samcem.
    * Spośród samic i samców wybierasz te o najmniejszej masie.
    * Dane w liście są posortowane względem gatunku a następnie nazwy zwierzęcia

    Wymaganie dla osób aspirujących na ocenę 5:

    * Ilość pamięci zajmowanej przez program musi być stała względem
      ilości elementów w liście zwierząt.
    * Ilość pamięci może rosnąć liniowo z ilością gatunków.

    Nie podaje schematu obiektów w tej liście, musicie radzić sobie sami
    (można podejrzeć zawartość listy w interaktywnej sesji interpretera).

    Do załadowania danych z listy możesz użyć metody `load_animals`.

    :param animal_list:
    """
    statek = {}
    for animal in animals:
        if animal['genus'] in statek:
            if animal['sex'] == 'male':
                if statek[animal['genus']][0] == {}:
                    statek[animal['genus']][0] = animal
                else:
                    statek[animal['genus']][0] = compareAnimals(statek[animal['genus']][0], animal)
            else:
                if statek[animal['genus']][1] == {}:
                    statek[animal['genus']][1] = animal
                else:
                    statek[animal['genus']][1] = compareAnimals(statek[animal['genus']][1], animal)
        else:
            if animal['sex'] == 'male':
                statek[animal['genus']] = [animal, {}]
            else:
                statek[animal['genus']] = [{}, animal]
    lista = []    
    for z in (statek.items()):
        lista.append(z[0])
        lista.append(z[1])
    lista.sort(key=lambda tup: (tup['genus'], tup['name']))
    print(lista)

def compareAnimals(a1, a2):
    if mass_generator(a1['mass']) > mass_generator(a2['mass']):
        return a2
    else:
        return a1

def mass_generator(d): 
        mass, unit = d
        if unit == 'kg': 
            return mass
        if unit == 'g':
            return mass/1000
        if unit == 'mg':
            return mass/1E-6
        if unit == 'Mg': 
            return mass*1000

if __name__ == "__main__":
    animals = load_animals()
    filter_animals(animals)
