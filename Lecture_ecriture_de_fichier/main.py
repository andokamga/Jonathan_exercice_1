#1 : Copier le contenu d'un fichier source vers un fichier destination
def copy_file(source, destination):
    try:
        with open(source, 'r') as src:
            content = src.read()
        with open(destination, 'w') as dest:
            dest.write(content)
        return True
    except Exception as e:
        print(f"Erreur lors de la copie : {e}")
        return False

#2 : Authentification d'un utilisateur via un fichier texte
def authenticate_user(login, password, user_file):
    try:
        with open(user_file, 'r') as file:
            for line in file:
                user_data = line.strip().split(',')
                if user_data[0] == login and user_data[1] == password:
                    print(f"Bienvenue {login}")
                    return True
        print("Erreur d'authentification")
        return False
    except Exception as e:
        print(f"Erreur lors de l'authentification : {e}")
        return False

def create_user_file(user_file, users_data):
    try:
        with open(user_file, 'w') as file:
            for user in users_data:
                file.write(','.join(user) + '\n')
        return True
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier : {e}")
        return False

#3 : Lire un fichier et afficher le nombre de lignes, mots et caractères
def file_statistics(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
        print(f"Nombre de lignes : {num_lines}")
        print(f"Nombre de mots : {num_words}")
        print(f"Nombre de caractères : {num_chars}")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")

#4 : Chercher un mot dans un fichier et retourner les lignes correspondantes
def search_word_in_file(word, file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        result = [line for line in lines if word in line]
        return result
    except Exception as e:
        print(f"Erreur lors de la recherche du mot : {e}")
        return []

#5 : Extraire les données d'un fichier et les stocker dans une liste de dictionnaires
def extract_data_to_dict(file_name):
    data_list = []
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        for line in lines:
            parts = line.strip().split(';')
            data = {}
            for part in parts:
                key, value = part.split(': ')
                data[key] = value
            data_list.append(data)
        return data_list
    except Exception as e:
        print(f"Erreur lors de l'extraction des données : {e}")
        return []

# Fonction principale pour tester les exercices
def main():
    #1 : Copier un fichier
    print("1 - Copier un fichier")
    copy_file('source.txt', 'destination.txt')

    #2 : Authentification
    print("2 - Authentification")
    create_user_file('users.txt', [
        ['login1', 'mdp74578', 'Donalds', 'John', '26'],
        ['login2', 'mXeAd55d', 'Clooney', 'George', '54']
    ])
    login = input("Entrez votre login : ")
    password = input("Entrez votre mot de passe : ")
    authenticate_user(login, password, 'users.txt')

    #3 : Statistiques du fichier
    print("3 - Statistiques du fichier")
    file_statistics('source.txt')

    #4 : Chercher un mot dans un fichier
    print("4 - Chercher un mot dans un fichier")
    result = search_word_in_file('Jean', 'data.txt')
    for line in result:
        print(line)

    #5 : Extraire les données de data.txt
    print("5 - Extraire les données de data.txt")
    data = extract_data_to_dict('data.txt')
    for entry in data:
        print(entry)

if __name__ == "__main__":
    main()