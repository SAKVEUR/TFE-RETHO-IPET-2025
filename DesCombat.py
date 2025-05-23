"""
QUI: Mathis Binnemans
QUAND: 19/03/25
QUOI: Classe DesCombat
"""

####################
###    Import    ###
####################
from random import *

##################################
### Constructeur / Destructeur ###
##################################
class DesCombat():
    def __init__(self, para_nombreFaceDesCombats:int, para_nombreFaceAttaque:int):

        self.__nombreFaceDesCombats:int = 6
        self.__nombreFaceAttaque:int = 3

        self.nombreFaceDesCombats = para_nombreFaceDesCombats
        self.nombreFaceAttaque = para_nombreFaceAttaque

    #####################
    ###    Getters    ###
    #####################
               
    ### Nombre de face neutres
    @property
    def para_nombreFaceDesCombats(self) -> int:
        return self.__nombreFaceDesCombats

    ### Nombre de face d'attaque
    @property
    def para_nombreFaceAttaque(self) -> int:
        return self.__nombreFaceAttaque

    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Thibaud Masset
    QUAND: 18/04/25
    QUOI: Méthode lancer()
    Lance le dé et retourne un nombre aléatoire entre 1 et le nombre de faces
    """
    def lancer(self) -> int:
        # Lancer le dé pour obtenir un nombre entre 1 et 6
        resultat = randint(1, self.nombreFaceDesCombats)
        
        # Seuls les nombres 1, 3 et 5 permettent d'attaquer
        if resultat in [1, 3, 6]:
            return resultat
        else:
            return 0  # Pas d'attaque
