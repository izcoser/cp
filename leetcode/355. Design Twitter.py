from collections import defaultdict
from typing import List
class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = defaultdict(set)
        self.feed_cache = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        t = Tweet(userId, tweetId)
        self.tweets.append(t)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        last_id = self.tweets[-1].tweetId if len(self.tweets) > 0 else "a"
        key = (userId, last_id)
        if key in self.feed_cache:
            return self.feed_cache[key]

        feed = []
        for t in self.tweets[::-1]:
            by = t.userId
            if by == userId or by in self.follows[userId]:
                feed.append(t.tweetId)
            if len(feed) == 10:
                break

        self.feed_cache[key] = feed
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        for k in self.feed_cache.copy():
            userId, _ = k
            if userId == followerId:
                del self.feed_cache[k]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        for k in self.feed_cache.copy():
            userId, _ = k
            if userId == followerId:
                del self.feed_cache[k]

class Tweet:
    def __init__(self, userId: int, tweetId: int):
        self.userId = userId
        self.tweetId = tweetId

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)