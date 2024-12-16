class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.idToEnd = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.idToEnd[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.idToEnd and currentTime < self.idToEnd[tokenId]:
            self.idToEnd[tokenId] = currentTime + self.timeToLive


    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for k, v in self.idToEnd.items():
            if v > currentTime:
                res += 1
        return res

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
