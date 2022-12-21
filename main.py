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
#from exemples_ecript import *
#import random

import sqlite3
import os
import datetime
import time
import shutil

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
    
    >>> creer_bdd('bdd_test')
    >>> 'bdd_test.db' in os.listdir()
    True
    >>> os.remove('bdd_test.db')
    """
    connection_bdd = sqlite3.connect(nom_bdd + '.db')
    creer_table(connection_bdd,'t_classes', {'nom': 'TEXT', 'annee': 'INTEGER'})
    creer_table(connection_bdd,'t_individus', {'photo': 'TEXT', 'nom': 'INTEGER', 'prenom': 'TEXT', 'l_classes': 'TEXT', 'est_eleve': 'INTEGER'})
    creer_table(connection_bdd,'t_absences', {'timestamp': 'INTEGER', 'id_individus': 'INTEGER'}, {'id_individus': 't_individus.id'})
    connection_bdd.commit()
    connection_bdd.close()


def ajouter_classe(connection_bdd, nom_classe, annee = datetime.date.today().year):
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
    cursor.execute( f"INSERT INTO t_classes (nom, annee) VALUES ('{nom_classe}', {annee})")

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
    
    >>> ajouter_individu(connection_bdd, './assets/X.jpeg', 'Doe', 'John', ['classe_test'], True)
    
    >>> req_sql = 'SELECT * FROM t_individus'
    >>> cursor = connection_bdd.execute(req_sql)
    >>> cursor.fetchone()
    (1, './assets/X.jpeg', 'Doe', 'John', 'classe_test', 1)
    >>> connection_bdd.close()
    >>> os.remove('bdd_test.db')
    
    """
    cursor = connection_bdd.cursor()
    cursor.execute( f"INSERT INTO t_individus (photo, nom, prenom, l_classes, est_eleve) VALUES ('{photo}', '{nom}', '{prenom}', '{', '.join(classes)}', {int(est_eleve)})")



def ajouter_absence(connection_bdd, id_individus, timestamp= ( int(time.time()) // (60*60) ) * 60 * 60 ):
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
    cursor.execute( f"INSERT INTO t_absences (timestamp, id_individus) VALUES ({timestamp}, {id_individus})")

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
    (1, './assets/X.jpeg', 'Doe', 'John', 'classe_test', 1)
    
    >>> modifier_individu(connection_bdd, 1, {'photo': './assets/X_R.jpeg', 'est_eleve': False})
    
    >>> cursor = cursor.execute(req_sql)
    >>> cursor.fetchone()
    (1, './assets/X_R.jpeg', 'Doe', 'John', 'classe_test', 0)
    
    
    >>> connection_bdd.close()
    >>> os.remove('bdd_test.db')
    """
    for key in valeurs:
        if isinstance(valeurs[key], bool):
            valeurs[key] = int(valeurs[key])
        if isinstance(valeurs[key], list):
            valeurs[key] = ', '.join(valeurs[key])
        cursor = connection_bdd.cursor()
        cursor.execute( f"UPDATE t_individus SET {key} = '{valeurs[key]}' WHERE id={id_individu}")

def liste_classe(connection_bdd):
    """
    Donne la liste des classes existantes avec leur année.
    :param (sqlite3.Connection): Connection à la base de données
    :return: tuple de tuple contenant les informations sur les classes
    
    >>> shutil.copy('test_bdd/liste_classe.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    
    >>> liste_classe(connection_bdd)
    (('classe_1', 2022), ('classe_2', 2022), ('classe_3', 2022))
    >>> connection_bdd.close()
    
    """
    req_sql = 'SELECT nom, annee FROM t_classes'
    cursor = connection_bdd.execute(req_sql)
    return tuple(cursor.fetchall())

def liste_individus(connection_bdd, classe, est_eleve):
    """
    Donne la liste des individus d'une classe
    :param (sqlite3.Connection): Connection à la base de données
    :param (str): classe, nom de la classe
    :param (bool): est_eleve, booléen qui permet de choisir si on liste les élèves ou non.
    :return: tuple de tuple contenant les informations sur les individus
    
    >>> shutil.copy('test_bdd/liste_individus.db', 'bdd_test.db')
    'bdd_test.db'
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    
    >>> liste_individus(connection_bdd, 'classe_test', True)
    ((None, 'Doe', 'John'), (None, 'Dar Alia', 'Mehdi'))
    
    >>> liste_individus(connection_bdd, 'classe_test2', False)
    ((None, 'Mbappé', 'Kyllian'), (None, 'Ronaldo', 'Cristiano'))
    
    >>> liste_individus(connection_bdd, 'classe_test', False)
    ((None, 'Ronaldo', 'Cristiano'),)
    
    >>> connection_bdd.close()
    """
    req_sql = f"SELECT photo, nom, prenom FROM t_individus WHERE est_eleve = {int(est_eleve)} AND (l_classes LIKE '%, {classe}%' OR l_classes LIKE '%{classe}, %' OR l_classes = '{classe}')"
    cursor = connection_bdd.execute(req_sql)
    return tuple(cursor.fetchall())


def liste_absences(connection_bdd, nom, prenom, classe):
    """
    Donne la liste des absences d'un individu.
    """

# Programme principal
if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    if 'supernote.db' not in os.listdir():
        creer_bdd('supernote')
    


