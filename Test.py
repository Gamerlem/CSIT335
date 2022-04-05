from Profile import Profile
from Match import Match

profile1 = Profile(1, "Jc", 22, "Talisay", "Shemale", True)
profile2 = Profile(2, "Secret", 22, "Talisay", "Female", False)

match = Match(profile1, profile2, True)

# pre-condition of second profile
# profile2.addToLikeList(profile1.id)

match.checkValidAccounts()
match.checkPremium()
match.isLikedProfile()
match.isLikeProfile()
match.addToLikeList()
match.addToMatchList()
match.addToRewindList()
match.notifyMatch()
match.allowConnection()

match1 = Match(profile2, profile1, True)

match1.checkValidAccounts()
match1.checkPremium()
match1.isLikedProfile()
match1.isLikeProfile()
match1.addToLikeList()
match1.addToMatchList()
match1.addToRewindList()
match1.notifyMatch()
match1.allowConnection()



print(profile1.rewindList)
print(profile2.rewindList)