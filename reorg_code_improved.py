def check_answer(my_answer, cor_answer):
    """
    Check each answer for correctness.
    """
    if my_answer == cor_answer:
        return True
    else:
        return False

def check_answers(my_answers,correct_ans):
    #1 variable names are not easy to tell apart
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results= []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], correct_ans[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    if count_correct/len(results) > 0.7:
    #8 The pass rate has been hard-coded into the function
        return "Congratulations, you passed the test!"
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass."

print(check_answers([1,2,3,3,4],[1,2,3,3,"dog"]))
