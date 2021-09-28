#!/usr/bin/env python
# -*- coding: utf-8 -*-
import statistics

def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input("rentrez une value pls"))
    values.sort()
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        words = [str(input("premier mot")), str(input("deuxieme mot"))]
    if len(words[0]) != len(words[1]):
        return(False)
    for lettre in words[0]:
        if words[0].count(lettre) != words[1].count(lettre):
            return(False)
    return(True)


def contains_doubles(items: list) -> bool:
    for item in items:
        if items.count(item)>1:
            return(True)
    return(False)

def best_grades(student_grades: dict) -> dict:

    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_name = ""
    best_moyenne = 0
    for current_name in list(student_grades):
        current_gradeList = student_grades[current_name]
        current_moyenne = statistics.mean(current_gradeList)
        if current_moyenne > best_moyenne:
            best_moyenne = current_moyenne
            best_name = current_name
    return {best_name:best_moyenne}


def frequence(sentence: str,countAllChars = True) -> dict: ###selon l'énoncé, seule les lettres devraietn etre contées mais les tests demandent de compter tous les characteres.
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY"
    table = {}
    for lettre in sentence:
        if lettre in alphabet or countAllChars:
            table[lettre] = sentence.count(lettre)
    print(sorted(table.items(),key = lambda x:x[1], reverse = True)[0])
    return table


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
