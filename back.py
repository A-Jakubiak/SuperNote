#!/usr/bin/env python3
# coding: utf-8
"""
Programme de mise en oeuvre ................. :
 - ...............
 - ............... 

Usage:
======
    python main.py 

__authors__ = ("Antoine Jakubiak", "Maxence Fleury")
__version__ = "0.0.1"
__copyright__ = "copyleft"
__date__ = "20221202" 

"""

# Modules externes
# from exemples_ecript import *
# import random

import sqlite3
import os
import datetime
import time
import shutil
import configfile


def creer_table(connection_bdd, nom_table, attributs, cles_etrangeres={}):
    """
    permet de créer une table avec id en clé primaire
    :param (sqlite3.Connection): Connection à la base de données
    :param (str): nom de la table
    :param (dict): dictionnaire contenant les attributs de la table et leurs types
    :param (dict): dictionnaire contenant les clés étrangères
    
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    >>> creer_table(connection_bdd, 'table_test', {'nom': 'text', 'age': 'int'})
    >>> req_sql = 'SELECT * FROM table_test'
    >>> cursor = connection_bdd.execute(req_sql)
    >>> connection_bdd.close()
    >>> names = [description[0] for description in cursor.description]
    >>> sorted(names)
    ['age', 'id', 'nom']
    >>> os.remove('bdd_test.db')
    """
    cursor = connection_bdd.cursor()
    req_sql = f"""CREATE TABLE "{nom_table}" (
"id"	INTEGER NOT NULL UNIQUE, """
    for nom_attributs in attributs:
        req_sql += f'"{nom_attributs}" {attributs[nom_attributs]},'
    req_sql += '	PRIMARY KEY("id" AUTOINCREMENT)'
    for nom_cles_etrangeres in cles_etrangeres:
        req_sql += f'FOREIGN KEY("{nom_cles_etrangeres}") REFERENCES "{cles_etrangeres[nom_cles_etrangeres].split(".")[0]}"("{cles_etrangeres[nom_cles_etrangeres].split(".")[1]}")'
    req_sql += ");"
    cursor.execute(req_sql)


def creer_bdd(nom_bdd):
    """
    créer une base de donnée avec les tables pour l'application
    :param (str): nom de la base de donnée
    
    >>> creer_bdd('bdd_test'.db)
    >>> 'bdd_test.db' in os.listdir()
    True
    >>> os.remove('bdd_test.db')
    """
    connection_bdd = sqlite3.connect(nom_bdd)
    creer_table(connection_bdd, 't_classes', {'nom': 'TEXT', 'annee': 'INTEGER'})
    creer_table(connection_bdd, 't_individus',
                {'photo': 'TEXT', 'nom': 'TEXT', 'prenom': 'TEXT', 'l_classes': 'TEXT', 'est_eleve': 'INTEGER'})
    creer_table(connection_bdd, 't_absences', {'timestamp': 'INTEGER', 'id_individus': 'INTEGER'},
                {'id_individus': 't_individus.id'})
    connection_bdd.commit()
    connection_bdd.close()


def ajouter_classe(connection_bdd, nom_classe, annee=datetime.date.today().year):
    """
    ajoute une classe à la table t_classes
    :param (sqlite3.Connection): Connection à la base de données
    :param (str): nom de la classe
    :param(int): année de la classe
    
    >>> shutil.copy('test_bdd/ajouter_classe.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    >>> ajouter_classe(connection_bdd, 'classe_test')
    >>> req_sql = 'SELECT nom FROM t_classes'
    >>> cursor = connection_bdd.execute(req_sql)
    >>> cursor.fetchone()
    ('classe_test',)
    >>> connection_bdd.close()
    >>> os.remove('bdd_test.db') 
    """
    cursor = connection_bdd.cursor()
    cursor.execute(f"INSERT INTO t_classes (nom, annee) VALUES (?, ?)", (nom_classe, annee))


def ajouter_individu(connection_bdd, photo, nom, prenom, classes, est_eleve):
    """
    ajoute un individu dans la base de données
    :param (sqlite3.Connection): Connection à la base de données
    :param (str): photo, url vers la photo
    :param (str): nom, nom de l'individu
    :param (str): prenom, prénom de l'individu
    :param (list): classes, liste de classe
    :param (bool): si l'individu est un élève.
    
    
    
    >>> shutil.copy('test_bdd/ajouter_individu.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    
    >>> ajouter_individu(connection_bdd, './assets/X.jpeg', 'Doe', 'John', [1], True)
    
    >>> req_sql = 'SELECT * FROM t_individus'
    >>> cursor = connection_bdd.execute(req_sql)
    >>> cursor.fetchone()
    (1, './assets/X.jpeg', 'Doe', 'John', '1', 1)
    >>> connection_bdd.close()
    >>> os.remove('bdd_test.db')
    
    """
    cursor = connection_bdd.cursor()
    cursor.execute(
        f"INSERT INTO t_individus (photo, nom, prenom, l_classes, est_eleve) VALUES (?, ?, ?, ?, ?)",
        (photo, nom, prenom, ', '.join(map(str, classes)), int(est_eleve)))


def ajouter_absence(connection_bdd, id_individus, timestamp=(int(time.time()) // (60 * 60)) * 60 * 60):
    """
    ajoute une absence a un individu.
    :param (sqlite3.Connection): Connection à la base de données
    :param (int): id_individus, id de l'individu.
    :param (int): timestamp, timestamp du début de l'heure de l'absence.
    
    >>> shutil.copy('test_bdd/ajouter_absence.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    
    >>> ajouter_absence(connection_bdd, 1, 1669986000)
    
    >>> req_sql = 'SELECT * FROM t_absences'
    >>> cursor = connection_bdd.execute(req_sql)
    >>> cursor.fetchone()
    (1, 1669986000, 1)
    >>> connection_bdd.close()
    >>> os.remove('bdd_test.db')
    """
    cursor = connection_bdd.cursor()
    cursor.execute(f"INSERT INTO t_absences (timestamp, id_individus) VALUES (?, ?)", (timestamp, id_individus))


def modifier_individu(connection_bdd, id_individu, valeurs):
    """
    modifie un individu.
    :param (sqlite3.Connection): Connection à la base de données
    :param (int): id_individus, id de l'individu.
    :param (dict): valeurs, dictionnaire contenant les valeurs a modifier
    
    >>> shutil.copy('test_bdd/modifier_individu.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    
    >>> req_sql = 'SELECT * FROM t_individus'
    >>> cursor = connection_bdd.execute(req_sql)
    >>> cursor.fetchone()
    (1, './assets/X.jpeg', 'Doe', 'John', '1', 1)
    
    >>> modifier_individu(connection_bdd, 1, {'photo': './assets/X_R.jpeg', 'est_eleve': False})
    
    >>> cursor = cursor.execute(req_sql)
    >>> cursor.fetchone()
    (1, './assets/X_R.jpeg', 'Doe', 'John', '1', 0)
    
    
    >>> connection_bdd.close()
    >>> os.remove('bdd_test.db')
    """
    for key in valeurs:
        if isinstance(valeurs[key], bool):
            valeurs[key] = int(valeurs[key])
        if isinstance(valeurs[key], list):
            valeurs[key] = ', '.join(map(str, valeurs[key]))
        cursor = connection_bdd.cursor()
        cursor.execute(f"UPDATE t_individus SET {key} = ? WHERE id=?", (valeurs[key], id_individu))


def liste_classe_nom_et_date(connection_bdd):
    """
    Donne la liste des classes existantes avec leur année.
    :param (sqlite3.Connection): Connection à la base de données
    :return: tuple de tuple contenant les informations sur les classes
    
    >>> shutil.copy('test_bdd/liste_classe.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    
    >>> liste_classe_nom_et_date(connection_bdd)
    (('classe_1', 2022), ('classe_2', 2022), ('classe_3', 2022))
    >>> connection_bdd.close()
    
    """
    req_sql = 'SELECT nom, annee FROM t_classes ORDER BY annee, nom'
    cursor = connection_bdd.execute(req_sql)
    return tuple(cursor.fetchall())


def liste_classe(connection_bdd):
    """
    Donne la liste des classes existantes avec leur année.
    :param (sqlite3.Connection): Connection à la base de données
    :return: tuple de tuple contenant les informations sur les classes

    >>> shutil.copy('test_bdd/liste_classe.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')

    >>> liste_classe(connection_bdd)
    ((1, 'classe_1', 2022), (2, 'classe_2', 2022), (3, 'classe_3', 2022))
    >>> connection_bdd.close()

    """
    req_sql = 'SELECT id, nom, annee FROM t_classes ORDER BY annee, nom'
    cursor = connection_bdd.execute(req_sql)
    return tuple(cursor.fetchall())


def recuperer_id_depuis_nom_date(connection_bdd, nom, annee):
    """
    Donne la liste des classes existantes avec leur année.
    :param (sqlite3.Connection): Connection à la base de données
    :param (str): nom de la classe
    :param (int), année de la classe
    :return: id de la classe

    >>> shutil.copy('test_bdd/recuperer_id_depuis_nom_date.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')

    >>> recuperer_id_depuis_nom_date(connection_bdd, 'classe_1', 2022)
    1

    >>> recuperer_id_depuis_nom_date(connection_bdd, 'classe_2', 2022)
    2

    >>> recuperer_id_depuis_nom_date(connection_bdd, 'classe_3', 2022)
    3

    >>> recuperer_id_depuis_nom_date(connection_bdd, 'classe_3', 2021)

    >>> connection_bdd.close()

    """
    req_sql = f'SELECT id FROM t_classes WHERE nom=? AND annee=?'
    cursor = connection_bdd.execute(req_sql, (nom, annee))
    response = cursor.fetchall()
    if len(response) == 0:
        return None
    return response[0][0]


def recuperer_nom_date_depuis_id(connection_bdd, id):
    """
    Donne la liste des classes existantes avec leur année.
    :param (sqlite3.Connection): Connection à la base de données
    :param (str): nom de la classe
    :param (int), année de la classe
    :return: id de la classe

    >>> shutil.copy('test_bdd/recuperer_nom_date_depuis_id.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')

    >>> recuperer_nom_date_depuis_id(connection_bdd, 1)
    ('classe_1', 2022)

    >>> recuperer_nom_date_depuis_id(connection_bdd, 2)
    ('classe_2', 2022)

    >>> recuperer_nom_date_depuis_id(connection_bdd, 3)
    ('classe_3', 2022)

    >>> recuperer_nom_date_depuis_id(connection_bdd, 4)

    >>> connection_bdd.close()

    """
    req_sql = f'SELECT nom, annee FROM t_classes WHERE id=?'
    cursor = connection_bdd.execute(req_sql, (id,))
    response = cursor.fetchall()
    if len(response) == 0:
        return None
    return response[0]


def liste_individus(connection_bdd, classe, est_eleve=None):
    """
    Donne la liste des individus d'une classe
    :param (sqlite3.Connection): Connection à la base de données
    :param (int): id de la classe
    :param (bool): est_eleve, booléen qui permet de choisir si on liste les élèves ou non.
    :return: tuple de tuple contenant les informations sur les individus
    
    >>> shutil.copy('test_bdd/liste_individus.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    
    >>> liste_individus(connection_bdd, 1, True)
    (('Doe', 'John', (1,), True, None), ('Dar Alia', 'Mehdi', (1,), True, None))
    
    >>> liste_individus(connection_bdd, 2, False)
    (('Mbappé', 'Kyllian', (2,), False, None), ('Ronaldo', 'Cristiano', (1, 2), False, None))
    
    >>> liste_individus(connection_bdd, 1, False)
    (('Ronaldo', 'Cristiano', (1, 2), False, None),)
    
    >>> connection_bdd.close()
    """
    cursor = None
    if est_eleve != None:
        req_sql = f"SELECT nom, prenom, l_classes, est_eleve, photo FROM t_individus WHERE est_eleve = ? AND (l_classes LIKE ? OR l_classes LIKE ? OR l_classes = ?)"
        cursor = connection_bdd.execute(req_sql, (int(est_eleve), f'%, {classe}%', f'%{classe}, %', f'{classe}'))
    else:
        req_sql = f"SELECT nom, prenom, l_classes, est_eleve, photo FROM t_individus WHERE (l_classes LIKE ? OR l_classes LIKE ? OR l_classes = ?)"
        cursor = connection_bdd.execute(req_sql, (f'%, {classe}%', f'%{classe}, %', f'{classe}'))

    return tuple((x[0], x[1], tuple(map(int, x[2].split(', '))) if x[2] else (()), bool(x[3]), x[4]) for x in
                 tuple(cursor.fetchall()))


def liste_individus_avec_id(connection_bdd, classe, est_eleve=None):
    """
    Donne la liste des individus d'une classe
    :param (sqlite3.Connection): Connection à la base de données
    :param (int): id de la classe
    :param (bool): est_eleve, booléen qui permet de choisir si on liste les élèves ou non.
    :return: tuple de tuple contenant les informations sur les individus

    >>> shutil.copy('test_bdd/liste_individus.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')

    >>> liste_individus_avec_id(connection_bdd, 1, True)
    ((1, 'Doe', 'John', (1,), True, None), (4, 'Dar Alia', 'Mehdi', (1,), True, None))

    >>> liste_individus_avec_id(connection_bdd, 2, False)
    ((2, 'Mbappé', 'Kyllian', (2,), False, None), (3, 'Ronaldo', 'Cristiano', (1, 2), False, None))

    >>> liste_individus_avec_id(connection_bdd, 1, False)
    ((3, 'Ronaldo', 'Cristiano', (1, 2), False, None),)

    >>> connection_bdd.close()
    """
    cursor = None
    if est_eleve is not None:
        req_sql = f"SELECT id, nom, prenom, l_classes, est_eleve, photo FROM t_individus WHERE est_eleve = ? AND (l_classes LIKE ? OR l_classes LIKE ? OR l_classes = ?)"
        cursor = connection_bdd.execute(req_sql, (int(est_eleve), f'%, {classe}%', f'%{classe}, %', f'{classe}'))
    else:
        req_sql = f"SELECT id, nom, prenom, l_classes, est_eleve, photo FROM t_individus WHERE (l_classes LIKE ? OR l_classes LIKE ? OR l_classes = ?)"
        cursor = connection_bdd.execute(req_sql, (f'%, {classe}%', f'%{classe}, %', f'{classe}'))
    return tuple(
        (x[0], x[1], x[2], tuple(map(int, x[3].split(', '))) if x[3] else (()), bool(x[4]), x[5]) for x in
        tuple(cursor.fetchall()))


def liste_absences(connection_bdd,id):
    """
    Donne la liste des absences d'un individu.
    :param (sqlite3.Connection): Connection à la base de données
    :param (int): id, id de l'individu
    :return: tuple de tuple contenant les informations sur les individus
    
    >>> shutil.copy('test_bdd/liste_absences.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    
    >>> liste_absences(connection_bdd, 1)
    (1671192000, 1671188400)
    
    >>> connection_bdd.close()
    """
    req_sql = f"SELECT timestamp FROM t_absences INNER JOIN t_individus ON t_absences.id_individus = t_individus.id WHERE t_individus.id = ?"
    cursor = connection_bdd.execute(req_sql, (id, ))
    return tuple([x[0] for x in cursor.fetchall()])


def supp_classe(connection_bdd, id_classe):
    """
    Supprime la classe donnée en paramètre.
    :param connection_bdd: connection à la base de donnée
    :type connection_bdd: sqlite3.connection
    :param id_classe: id de la classe
    :type id_classe: int

    >>> shutil.copy('test_bdd/supp_classe.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')

    >>> supp_classe(connection_bdd, 1)

    >>> liste_classe(connection_bdd)
    ()
    >>> connection_bdd.close()

    """
    for individu in liste_individus_avec_id(connection_bdd, id_classe):
        l_classe = list(individu[3])
        l_classe.remove(id_classe)
        modifier_individu(connection_bdd, individu[0], {'l_classes': ', '.join(l_classe)})
    req_sql = f'DELETE FROM t_classes WHERE id = ?'
    cursor = connection_bdd.execute(req_sql, (id_classe,))
    connection_bdd.commit()


def recherche_individu(connection_bdd, query):
    """
        Recherche un individu.
        :param (sqlite3.Connection): Connection à la base de données
        :param (str): query, partie du nom/prenom de l'individu
        :return: tuple de tuple contenant les informations sur les individus trouvés

        >>> shutil.copy('test_bdd/recherche_individus.db', 'bdd_test.db')
        'bdd_test.db'
        >>> connection_bdd = sqlite3.connect('bdd_test.db')

        >>> recherche_individu(connection_bdd, 'Do')
        ((1, 'Doe', 'John', (1,), True, None), (3, 'Ronaldo', 'Cristiano', (1, 2), False, None))

        >>> connection_bdd.close()
        """
    r_results = []
    results = []
    req_sql = [f'SELECT id, nom, prenom, l_classes, est_eleve, photo FROM t_individus WHERE nom LIKE ? ORDER BY nom',
               f'SELECT id, nom, prenom, l_classes, est_eleve, photo FROM t_individus WHERE prenom LIKE ? ORDER BY prenom']
    for req in req_sql:
        cursor = connection_bdd.cursor()
        cursor = cursor.execute(req, (f'%{query}%',))
        r_results.append(cursor.fetchall())
    connection_bdd.commit()
    for r_result in r_results:
        for result in r_result:
            if result not in results:
                results.append(result)
    return tuple(
        (x[0], x[1], x[2], tuple(map(int, x[3].split(', '))) if x[3] else (()), bool(x[4]), x[5]) for x in results)

def supprimer_absence(connection_bdd, timestamp, id_ind):
    """
    Supprime l'absence d'un individu
    :param connection_bdd: Connection a la base de données
    :type connection_bdd: sqlite3.Connection
    :param timestamp: Timestamp de l'absence
    :type timestamp: int
    :param id_ind: id de l'individu
    :type id_ind: id
    :return: None
    :rtype: None

    >>> shutil.copy('test_bdd/supprimer_absence.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')

    >>> liste_absences(connection_bdd, 1)
    (1677369720,)

    >>> supprimer_absence(connection_bdd, 1677369720, 1)

    >>> liste_absences(connection_bdd, 1)
    ()
    >>> connection_bdd.close()
    """
    req_sql = f"DELETE FROM t_absences WHERE t_absences.timestamp = ? AND t_absences.id_individus = ?"
    cursor = connection_bdd.execute(req_sql, (timestamp, id_ind))

# Programme principal
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    if configfile.bdd_path not in os.listdir():
        creer_bdd(configfile.bdd_path)
