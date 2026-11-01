class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pass
        '''
        Given: 2 arrays, score ages
        Goal: return maximum score of valid group

        Valid Group Constraints:
            - younger player scores < older player scores
        

        * sort age array from youngest -> oldest
        * ake scores match ages

        (age, score)

        
        1. create sorted tuple (age, score)
        2. array that holds max scores
        3. loop thru ages array:

            a) check if previous age score is <= age
                - temp 1 = score2
                - score2 += age score
            b) greater than:
                - temp = score2
                - scre2 = max(score2, agescore+score1)
                - score1 = temp
        4. return score2

        '''


        players = sorted(zip(ages, scores))
        dp = []


        for i in range(len(players)):
            best = players[i][1]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    best = max(best, dp[j] + players[i][1])
            dp.append(best)
        return max(dp)






