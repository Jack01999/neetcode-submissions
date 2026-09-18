import heapq

class Twitter:

    def __init__(self):
        self.timestamp = 0
        # { userId: tweet[] }
        # Tweet = (timestamp, tweetId)
        self.tweets = defaultdict(list)
        # { followerId: followeeId[] }
        self.followings = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = [] # Popping will give the most recent, max timestamp
        res = []
        fullFeed = []
        fullFeed += self.tweets[userId]
        for followeeId in self.followings[userId]:
            fullFeed += self.tweets[followeeId]
        # print(self.tweets)
        # for feed in fullFeed:
        #     heapq.heappush(minHeap, (feed[0], feed[1]))
        heapq.heapify(fullFeed)
        #print(minHeap)
        while fullFeed and len(res) < 10:
            top = heapq.heappop(fullFeed)
            res.append(top[1])

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)
        
