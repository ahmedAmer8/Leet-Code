class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Use two min-heaps, one for storing the leaving times that have already been processed,
        # and one for storing the chairs that are currently unoccupied.

        target_arrival = times[targetFriend][0]
        available_chairs = list(range(0, len(times)))
        heapq.heapify(available_chairs)
        used_chairs = []
        times.sort()
        for ar, lv in times:
            while used_chairs and used_chairs[0][0] <= ar:
                heappush(available_chairs, heappop(used_chairs)[1])
            chair = heappop(available_chairs)
            heappush(used_chairs, (lv, chair))
            if ar == target_arrival:
                return chair
        
