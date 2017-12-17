def sum_of_middle_three(score1,score2,score3,score4,score5):
      """
      Find the average of the middle three numbers out of the five given.
      """
      max_score = max(score1,score2,score3,score4,score5)
      min_score = min(score1,score2,score3,score4,score5)
      sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
      return sum

print(sum_of_middle_three(2,1,1,1,1))
