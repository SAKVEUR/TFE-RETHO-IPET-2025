"""
QUI: Mathis Binnemans
QUAND: 19/03/25
QUOI: Fichier classe "Coffre"
"""

##################################
### Constructeur / Destructeur ###
##################################
class Coffre():
    def __init__(self, para_idCoffre: int, para_contenuCoffre:str = "Bombe", para_symbole:str = "X", para_positionX:int = 0, para_positionY:int = 0, para_idQuete:int = 0):

        self.__idCoffre = para_idCoffre
        self.__contenuCoffre = para_contenuCoffre
        self.__symbole = para_symbole
        self.__positionX = para_positionX
        self.__positionY = para_positionY
        self.__idQuete = para_idQuete
        self.__estOuvert = False
    #####################
    ###    Getters    ###
    #####################

    ### Id de la porte
    @property
    def idCoffre(self) -> int:
        return self.__idCoffre

    ### Contenu du coffre
    @property
    def contenuCoffre(self) -> str:
        return self.__contenuCoffre

    ### Id du coffre
    @property
    def symbole(self) -> str:
        return self.__symbole

    ### Position X du coffre
    @property
    def positionX(self) -> int:
        return self.__positionX

    ### Position Y du coffre
    @property
    def positionY(self) -> int:
        return self.__positionY 

    ### Id de la quete
    @property
    def idQuete(self) -> int:
        return self.__idQuete

    ### Est ouvert
    @property
    def estOuvert(self) -> bool:
        return self.__estOuvert

    #####################
    ###    Setters    ###
    #####################  

    ### Symbole du coffre
    @symbole.setter
    def symbole(self, para_symbole:str):
        self.__symbole = para_symbole

    ### Est ouvert
    @estOuvert.setter
    def estOuvert(self, para_estOuvert:bool):
        self.__estOuvert = para_estOuvert

    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Sacha Fierin
    QUAND: 18/05/25
    QUOI: Méthode ouvrir()
    Permet d'ouvrir la porte et la fait disparaître du plateau
    """
    def ouvrir(self) -> None:
        self.__estOuvert = True
        self.devoilerContenu()
        return None  # Retourne None pour indiquer que le coffre doit être supprimé du plateau



    """
    QUI: Sacha Fierin
    QUAND: 19/03/25
    QUOI: Méthode devoilerContenu()
    Permet d'afficher/dévoiler le contenu du coffre
    """
    def devoilerContenu(self):
        self.__estOuvert = True
        return f"Le coffre contient l'objet {self.contenuCoffre} !"



    """
    QUI: Sacha Fierin
    QUAND: 19/03/25
    QUOI: Méthode __str__()
    Permet d'afficher le symbole du coffre
    """
    def __str__(self):
        return self.symbole
