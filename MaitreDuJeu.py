"""
QUI: Mathis Binnemans et Sacha Fierin
QUAND: 26/03/25
QUOI: Classe MaitreDuJeu
"""

####################
###    Import    ###
####################
from Joueur import Joueur
from Monstre import Monstre

##################################
### Constructeur / Destructeur ###
##################################
class MaitreDuJeu(Joueur):
    def __init__(self, para_nomJoueur:str):
        super().__init__(para_nomJoueur,est_maitre_du_jeu=True)

    #####################
    ###    Getters    ###
    #####################

