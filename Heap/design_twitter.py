from collections import defaultdict
import heapq as hp
class Twitter:

    def __init__(self):
        self.time = 1
        self.following_map = defaultdict(list)
        self.tweets_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following_map:
            self.following_map[userId] = []

        self.tweets_map[userId].append([-self.time, tweetId])
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], deepcopy(self.tweets_map[userId])
        for users in self.following_map[userId]:
            heap += deepcopy(self.tweets_map[users])
        hp.heapify(heap)
        
        i = 0
        while heap and i < 10:
            res.append(hp.heappop(heap)[1])
            i += 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following_map[followerId]:
            self.following_map[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
