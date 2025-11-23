from collections import defaultdict
from typing import List
from heapq import heappop, heappush

def append_to_list_maximum_10(lst, item):
    if len(lst) == 10:
        lst.pop(0)
    lst.append(item)

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.followees = defaultdict(set)
        self.feed_cache = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        t = Tweet(userId, tweetId, self.timestamp)
        self.timestamp += 1

        append_to_list_maximum_10(self.tweets[userId], t)

        if userId in self.feed_cache:
            del self.feed_cache[userId]

        # clear the cache of every user who follows him.
        for u in self.followees[userId]:
            if u in self.feed_cache:
                del self.feed_cache[u]

        
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.feed_cache:
            return self.feed_cache[userId]
        
        latest = []
        
        authors = [userId] + list(self.follows[userId])
        for a in authors:
            tweets = self.tweets[a]
            if tweets:
                idx = len(tweets) - 1
                tweet = tweets[idx]
                heappush(latest, (-tweet.timestamp, a, idx))

        feed = []

        while latest and len(feed) < 10:
            _, author, idx = heappop(latest)
            tweet = self.tweets[author][idx]
            feed.append(tweet.tweetId)

            if idx > 0:
                prevTweet = self.tweets[author][idx - 1]
                heappush(latest, (-prevTweet.timestamp, author, idx - 1))

        self.feed_cache[userId] = feed
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        self.followees[followeeId].add(followerId)

        if followerId in self.feed_cache:
            del self.feed_cache[followerId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        self.followees[followeeId].discard(followerId)
        
        if followerId in self.feed_cache:
            del self.feed_cache[followerId]

class Tweet:
    def __init__(self, userId: int, tweetId: int, timestamp: int):
        self.userId = userId
        self.tweetId = tweetId
        self.timestamp = timestamp

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)