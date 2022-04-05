import unittest
from Profile import Profile
from Match import Match


class TestScenario5(unittest.TestCase):
    def setUp(self) -> None:
        profile1 = Profile(1, "Jc", 22, "Talisay", "Shemale", False)
        profile2 = Profile(2, "Secret", 22, "Talisay", "Female", False)
        self.match = Match(profile1, profile2, True)

        # pre-condition: profile2 likes profile1
        profile2.addToLikeList(profile1.id)

        return super().setUp()

    def tearDown(self) -> None:
        # delete all the temporary data created in setUp() method
        return super().tearDown()

    def test_checkValidAccounts(self):
        c1 = self.match.checkValidAccounts()
        self.assertEqual(c1, True)

    def test_checkPremium(self):
        c2 = self.match.checkPremium()
        self.assertEqual(c2, False)

    def test_isLikedProfile(self):
        c3 = self.match.isLikedProfile()
        self.assertEqual(c3, True)

    def test_isLikeProfile(self):
        c4 = self.match.isLikeProfile()
        self.assertEqual(c4, True)

    def test_act_addToLikeList(self):
        a1 = self.match.addToLikeList()
        self.assertEqual(a1, True)

    def test_act_addToMatchList(self):
        a2 = self.match.addToMatchList()
        self.assertEqual(a2, True)

    def test_act_addToRewindList(self):
        a3 = self.match.addToRewindList()
        self.assertEqual(a3, False)

    def test_act_notifyMatch(self):
        a4 = self.match.notifyMatch()
        self.assertEqual(a4, True)

    def test_act_allowConnection(self):
        a5 = self.match.allowConnection()
        self.assertEqual(a5, True)


if __name__ == '__main__':
    unittest.main()
