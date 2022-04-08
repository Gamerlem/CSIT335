import unittest
from Profile import Profile
from Match import Match

class TestScenario9To16(unittest.TestCase):
    def setUp(self) -> None:
        profile1 = Profile(1, "", 22, "Talisay", "Male", False)
        profile2 = Profile(2, "Lora", 22, "Talisay", "Female", False)
        # pre-condition: profile2 likes profile1
        profile2.addToLikeList(profile1.id)
        """ 
        Match parameters
        first param : profile1 is Current User
        second param : profile2 is Other User
        third param : isLike whether current user likes the other user
        """
        self.match = Match(profile1 = profile1, profile2 = profile2, isLike = True)
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_checkValidAccounts(self):
        c1 = self.match.checkValidAccounts()
        self.assertEqual(c1, False)
    
    def test_checkPremium(self):
        c2 = self.match.checkPremium()
        self.assertEqual(c2, False)

    def test_isLikedProfile(self):
        c3 = self.match.isLikedProfile()
        self.assertEqual(c3, False)

    def test_isLikeProfile(self):
        c4 = self.match.isLikeProfile()
        self.assertEqual(c4, False)

    def test_act_addToLikeList(self):
        a1 = self.match.addToLikeList()
        self.assertEqual(a1, False)

    def test_act_addToMatchList(self):
        a2 = self. match.addToMatchList()
        self.assertEqual(a2, False)

    def test_act_addToRewindList(self):
        a3 = self.match.addToRewindList()
        self.assertEqual(a3, False)

    def test_act_notifyMatch(self):
        a4 = self.match.notifyMatch()
        self.assertEqual(a4, False)

    def test_act_allowConnection(self):
        a5 = self.match.allowConnection()
        self.assertEqual(a5, False)

if __name__ == '__main__':
    unittest.main()