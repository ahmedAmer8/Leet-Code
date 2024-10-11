class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_counts = [0] * n
        available = list(range(n))
        heapify(available)
        used = []

        for st, en in sorted(meetings):
            while used and used[0][0] <= st:
                heappush(available, heappop(used)[1])

            delay = 0
            if not available:
                end, room = heappop(used)
                heappush(available, room)
                delay = end - st
            room = heappop(available)
            room_counts[room] += 1
            heappush(used, (en+delay, room))
        print(room_counts)
        res = 0
        mx = room_counts[0]
        for i in range(1, n):
            if room_counts[i] > mx:
                res = i
                mx = room_counts[i]
        return res
