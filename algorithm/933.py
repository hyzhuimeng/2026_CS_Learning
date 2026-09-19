from collections import deque
class RecentCounter:
    def __init__(self):
        self.queue=deque()
    def ping(self,t:int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)
rec=RecentCounter()
rec.ping(1)
rec.ping(7)
rec.ping(88)
rec.ping(99)
rec.ping(3008)
print(rec.queue)

