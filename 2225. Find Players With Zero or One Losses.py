class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        
        winners = [match[0] for match in matches]
        losers = [match[1] for match in matches]
        
        perfectWinners = list(set(winners)-set(losers))
        
        loser_counter = collections.Counter(losers)
        one_lost = []
        for loser in loser_counter:
            if loser_counter[loser] == 1:
                one_lost.append(loser)
                
        return [sorted(perfectWinners), sorted(one_lost)]
