class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        team_skills = sum(skill)/ (len(skill)/2)
        teams = defaultdict(int)
        res = 0
        for p1 in skill:
            p2 = team_skills - p1
            if p2 in teams:
                teams[p2] -= 1
                if teams[p2] == 0:
                    teams.pop(p2)
            else:
                teams[p1] += 1
            res += p1 * p2
        return int(res//2) if sum(teams.values()) == 0 else -1
