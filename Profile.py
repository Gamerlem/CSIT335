"""

Final Project in CSIT335
Group 18 Members: Lhora Mae Alvarez, Mel Jay Llanos, and Jecee Ryn Obrero

Findrr - Online Dating Application

Findrr is a simple online dating app where users find the romance of their life. 
Users can like or dislike the profiles of other users. 
Findrr also employs a "double opt-in" mechanism, in which both users must match in order to send messages.

"""


class Profile():
    id: int = 0
    name: str = ""
    age: int = 0
    address: str = ""
    gender: str = ""
    isValid: bool = False
    isPremium: bool = False
    likeList: list = []
    matchList: list = []
    rewindList: list = []

    def __init__(
        self,
        id: int = 0,
        name: str = "",
        age: int = 0,
        address: str = "",
        gender: str = "",
        isPremium: bool = False
    ) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.isValidProfile()
        self.isPremium = isPremium
        self.likeList = []
        self.matchList = []
        self.rewindList = []

    def _isBlank(self, string: str):
        return string == ""

    def isValidProfile(self):
        if not self._isBlank(self.name) and not self._isBlank(self.address) and not self._isBlank(self.gender):
            if self.age >= 18:
                self.isValid = True

    def addToLikeList(self, id: int):
        if id not in self.likeList:
            self.likeList.append(id)

    def addToMatchList(self, id: int):
        if id not in self.matchList:
            self.matchList.append(id)

    def addToRewindList(self, id: int):
        if id not in self.rewindList:
            self.rewindList.append(id)
