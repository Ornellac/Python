from datetime import date
import random

class Pythogotchi:
    def __init__(self, nom:str) -> None:
        self.__Nom : str = nom
        self.__DateCreation : date = date.today()
        self.__NiveauFaim : int = 8
        self.__NiveauBonheur : int = 8
        self.__EstSale : bool = True
        self.__PointDeVie : int = 10
        self.__Genre : bool = bool(random.randint(0,1))

    def _get_NiveauFaim(self) -> int:
        return self.__NiveauFaim

    def _set_NiveauFaim(self, value : int):
        if value > 16 : value = 16
        if value < 0 : value = 0
        self.__NiveauFaim = value

    NiveauFaim = property(_get_NiveauFaim)

    @property
    def NiveauBonheur(self) -> int:
        return self.__NiveauBonheur

    def _set_NiveauBonheur(self, value: int):
        if value > 16 : value = 16
        if value < 0 : value = 0
        self.__NiveauBonheur = value

    def _get_EstSale(self) -> bool:
        return self.__EstSale

    EstSale = property(_get_EstSale)

    def _get_Age(self)-> int:
        return (date.today() - self.__DateCreation).days

    Age = property(_get_Age)

    @property
    def Nom(self)-> str:
        return self.__Nom

    def _get_Genre(self)-> str:
        if not self.__Genre  : return "Male"
        return "Female"

    Genre = property(_get_Genre)

    def PasserUnTour(self)-> None:
        self._set_NiveauFaim(self.NiveauFaim - 1)
        self._set_NiveauBonheur(self.NiveauBonheur - 1)
        if not self.EstSale : self.__EstSale = bool(random.randint(0,1))
