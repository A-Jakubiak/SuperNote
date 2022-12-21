#!/usr/bin/env python3
# coding: utf-8
"""
Programme de mise en oeuvre ................. :
 - ...............
 - ............... 

Usage:
======
    python nsi_script.py 

    argument1: 
    argument2: 

__authors__ = ("Pascal LUCAS", "Professeur NSI")
__contact__ = ("pascal.lucas@ac-lille.fr")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "202200901"

"""

# Modules externes
#from exemples_ecript import *
#import random

import sqlite3
import os
import datetime

def creer_table(nom_bdd, nom_table, attributs, cles_etrangeres={}):
    """
    permet de créer une table avec id en clé primaire
    :param (str): nom de la base de donnée
    :param (str): nom de la table
    :param (dict): dictionnaire contenant les attributs de la table et leurs types
    :param (dict): dictionnaire contenant les clés étrangères
    
    >>> creer_table('bdd_test', 'table_test', {'nom': 'text', 'age': 'int'})
    >>> connection_bdd = sqlite3.connect('bdd_test.db')
    >>> req_sql = 'SELECT * FROM table_test'
    >>> cursor = connection_bdd.execute(req_sql)
    >>> connection_bdd.close()
    >>> names = [description[0] for description in cursor.description]
    >>> sorted(names)
    ['age', 'id', 'nom']
    >>> os.remove('bdd_test.db')
    """
    connection_bdd = sqlite3.connect(nom_bdd + '.db')
    try:
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
        connection_bdd.commit()
        connection_bdd.close()
    except sqlite3.Error as error:
        connection_bdd.close()
        return "Erreur d'acces à la base de données ", error

def creer_bdd(nom_bdd):
    """
    créer une base de donnée avec les tables pour l'application
    :param (str): nom de la base de donnée
    
    >>> creer_bdd('bdd_test')
    >>> 'bdd_test.db' in os.listdir()
    True
    >>> os.remove('bdd_test.db')
    """
    creer_table(nom_bdd,'t_classes', {'nom': 'TEXT', 'annee': 'INTEGER'})
    creer_table(nom_bdd,'t_individus', {'photo': 'TEXT', 'nom': 'INTEGER', 'prenom': 'TEXT', 'l_classes': 'TEXT', 'est_eleve': 'INTEGER'})
    creer_table(nom_bdd,'t_absences', {'timestamp': 'INTEGER', 'id_individus': 'INTEGER'}, {'id_individus': 't_individus.id'})
    
def ajouter_classe(nom_classe, annee = datetime.date.today().year):
    """
    ajoute une classe à la table t_classes
    :param (str): nom de la classe
    :param(int): année de la classe
    
    >>> creer_bdd('bdd_test')
    >>> ajouter_classe('classe_test')
    >>> req_sql = 'SELECT nom FROM t_classes'
    >>> cursor = connection_bdd.execute(req_sql)
    >>> connection_bdd.close()
    >>> names = [description[0] for description in cursor.description]
    >>> sorted(names)
    ['age', 'id', 'nom']
    >>> os.remove('bdd_test.db') 
    """
    
# Programme principal
if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    if 'supernote.db' not in os.listdir():
        creer_bdd('supernote')
    


