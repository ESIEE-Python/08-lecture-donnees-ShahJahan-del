#### Imports et définition des variables globales
'''Imports de random pour l'indice utilisé par get_list_k et csv pour le fichier utilisé'''
import random
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    filename=FILENAME
    l = []
    n=0
    with open(filename, 'r', encoding='utf8') as f:
        s=csv.reader(f,delimiter=';')
        t=list(s)
        l=t
        n=len(l)
    for i in range(n):
        for j in range(len(l[i])):
            l[i][j]=int(l[i][j])
    return l

def get_list_k(data, k):
    '''
    args: liste de listes et indice entier
    returns: liste
    
    '''
    l = []
    n=len(data)
    for i in range(n):
        if i==k:
            l=data[i]
    for index,_ in enumerate(l):
        l[index]=int(l[index])
    return l

def get_first(l):
    """args: liste
    returns: entier
    """
    return int(l[0])

def get_last(l):
    '''
    args:liste
    returns:entier
    '''
    return int(l[-1])

def get_max(l):
    '''
    args:liste
    returns:entier
    '''
    return int(max(l))

def get_min(l):
    '''
    args:liste
    returns:entier
    '''
    return int(min(l))

def get_sum(l):
    '''
    args:liste
    returns:entier
    '''
    s=0
    for elt in l:
        s+=int(elt)
    return s


#### Fonction principale


def main():
    """appels aux fonctions secondaires"""
    print(read_data(FILENAME))
    print(get_list_k(read_data(FILENAME),random.randint(0,99)))
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
