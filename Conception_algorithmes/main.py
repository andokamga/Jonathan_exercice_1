import random

#1 : Fonction pour générer une liste d'entiers pseudo-aléatoires
def genlist2(a, b, size):
    return [random.randint(a, b) for _ in range(size)]

#2 : Fonction pour générer un tuple de nombres entiers
def gennum():
    return random.randint(1, 100)  # Suppose que gennum génère un nombre entier entre 1 et 100

def gentuple(size):
    return tuple(gennum() for _ in range(size))

#3 : Fonction pour convertir une liste en tuple
def totuple(lst):
    return tuple(lst)

#4 : Fonction pour enlever les doublons d'une liste
def noduplicate(lst):
    return list(set(lst))

#5 : Fonction pour concaténer deux listes et vérifier si le set est vide
def toset(lst1, lst2):
    combined_set = set(lst1 + lst2)
    return bool(combined_set)

#6 : Fonction pour séparer un dictionnaire en deux
def splitdict():
    stud = {
        "stud 1": 14, "stud 2": 13, "stud 3": 9, "stud 4": 12,
        "stud 5": 3, "stud 6": 8, "stud 7": 16, "stud 8": 13,
        "stud 9": 13, "stud 10": 15, "stud 11": 14, "stud 12": 19,
        "stud 13": 10, "stud 14": 10, "stud 15": 13, "stud 16": 7,
        "stud 17": 12, "stud 18": 15, "stud 19": 9, "stud 20": 17,
    }

    studpass = {k: v for k, v in stud.items() if v >= 10}
    studfail = {k: v for k, v in stud.items() if v < 10}

    return studpass, studfail

#7 : Fonction pour générer un dictionnaire en demandant à l'utilisateur d'entrer des valeurs
def gendict(size):
    d = {}
    for _ in range(size):
        key = int(input("Entrez un nombre (clé) : "))
        value = input("Entrez une lettre (valeur) : ")
        d[key] = value
    return d

#8 : Générer un dictionnaire de l'alphabet français et afficher des valeurs par clé
def genascii():
    ascii_dict = {i: chr(i) for i in range(97, 123)}  # Génère a à z en ASCII
    while True:
        key = int(input("Entrez une clé ASCII (ou 0 pour quitter) : "))
        if key == 0:
            break
        elif key in ascii_dict:
            print(f"Valeur pour {key} : {ascii_dict[key]}")
        else:
            print("Valeur non disponible")

#9 : Fonction principale pour appeler toutes les autres
def main():
    print("1 - générer une liste :", genlist2(1, 10, 5))
    print("2 - générer un tuple de nombres entiers :", gentuple(5))
    lst = [1, 2, 2, 3, 4]
    print("3 - convertir une liste en tuple :", totuple(lst))
    print("4 - enlever les doublons d'une liste :", noduplicate(lst))
    print("5 - concaténer deux listes et vérifier si le set est vide:", toset([1, 2, 3], [3, 4, 5]))
    studpass, studfail = splitdict()
    print("6 - student pass :", studpass)
    print("6 - student fail :", studfail)
    dictionnaire = gendict(3)
    print("7 - dictionnaire de taille 3:", dictionnaire)
    genascii()

if __name__ == "__main__":
    main()