from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.time = 0

        # userId -> list of (timestamp, tweetId)
        self.tweets = defaultdict(list)

        # userId -> set of followees
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        # Include the user's own tweets
        users = self.following[userId] | {userId}

        heap = []

        # Put the newest tweet from each user into the heap
        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                timestamp, tweetId = self.tweets[uid][index]

                heapq.heappush(
                    heap,
                    (-timestamp, tweetId, uid, index)
                )

        result = []

        while heap and len(result) < 10:
            _, tweetId, uid, index = heapq.heappop(heap)
            result.append(tweetId)

            # Add the next older tweet from the same user
            if index > 0:
                index -= 1
                timestamp, tweetId = self.tweets[uid][index]

                heapq.heappush(
                    heap,
                    (-timestamp, tweetId, uid, index)
                )

        return result

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)