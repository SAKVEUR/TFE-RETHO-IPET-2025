"""
QUI: Mathis Binnemans
QUAND: 19/03/25
QUOI: Classe DesDefense
"""

####################
###    Import    ###
####################
from random import *

##################################
### Constructeur / Destructeur ###
##################################
class DesDefense():
    def __init__(self, para_nombreFaceDesDefense:int = 6, para_nombreFaceDefense:int = 2):

       self.__nombreFaceDesDefense:int = 6
       self.__nombreFaceDefense:int = 2

       self.nombreFaceDesDefense = para_nombreFaceDesDefense
       self.nombreFaceDefense = para_nombreFaceDefense

    #####################
    ###    Getters    ###
    #####################
               
    ### Nombre de face neutres
    @property
    def para_nombreFaceDesDefense(self) -> int:
        return self.__nombreFaceDesDefense

    ### Nombre de face de défense
    @property
    def para_nombreFaceDefense(self) -> int:
        return self.__nombreFaceDefense

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
        resultat = randint(1, self.nombreFaceDesDefense)
        
        # Seuls les nombres 1 et 6 permettent de se défendre
        if resultat in [2,5]:
            return resultat
        else:
            return 0  # Pas de défense
