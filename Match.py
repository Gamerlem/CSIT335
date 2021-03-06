"""

Final Project in CSIT335
Group 18 Members: Lhora Mae Alvarez, Mel Jay Llanos, and Jecee Ryn Obrero

Findrr - Online Dating Application

Findrr is a simple online dating app where users find the romance of their life. 
Users can like or dislike the profiles of other users. 
Findrr also employs a "double opt-in" mechanism, in which both users must match in order to send messages.

"""
from Profile import Profile


class Match():
    profile1: Profile  # main user
    profile2: Profile  # secondary user
    isLike: bool = False

    def __init__(
        self,
        profile1: Profile,
        profile2: Profile,
        isLike: bool = False
    ) -> None:
        self.profile1 = profile1
        self.profile2 = profile2
        self.isLike = isLike

    def _isMatch(self):
        return self.addToMatchList()

    def checkValidAccounts(self):
        return self.profile1.isValid and self.profile2.isValid

    def checkPremium(self):
        return self.profile1.isPremium and self.checkValidAccounts()

    # check if other users like the main user
    def isLikedProfile(self):
        return self.profile1.id in self.profile2.likeList and self.checkValidAccounts()

    # check if main user likes the other user
    def isLikeProfile(self):
        return self.isLike and self.checkValidAccounts()

    def addToLikeList(self):
        if self.checkValidAccounts() and self.isLike and self.checkValidAccounts():
            self.profile1.addToLikeList(self.profile2.id)
            return True
        return False

    def addToMatchList(self):
        if self.isLikedProfile() and self.isLikeProfile() and self.checkValidAccounts():
            self.profile1.addToMatchList(self.profile2.id)
            self.profile2.addToMatchList(self.profile1.id)
            return True
        return False

    def addToRewindList(self):
        if not self.isLikeProfile() and self.checkValidAccounts():
            self.profile1.addToRewindList(self.profile2.id)
            return True
        return False

    def notifyMatch(self):
        if self._isMatch() and self.checkValidAccounts():
            print("It's a Match")
            return True
        return False

    def allowConnection(self):
        if (self._isMatch() or (self.profile1.isPremium and self.isLike)) and self.checkValidAccounts():
            print("You can message now.")
            return True
        return False
