import heapq

class Solution:
    def minMeetingRooms(self, intervals: list) -> int:
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x.start)

        # Min heap stores end times
        rooms = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            # Reuse a room if a meeting has ended
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)

            # Assign room to current meeting
            heapq.heappush(rooms, end)

        return len(rooms)