def check_answers(my_answers,answers):
    #1 variable names are not easy to tell apart
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    #2 Code will only work if there are exactly five answers
    results= [None, None, None, None, None]
    #3 Repeated code would be better as a separate function
    if my_answers[0] == answers[0]:
        results[0] = True
    elif my_answers[0] != answers[0]:
        results[0] = False
    #4 if and elif could be clearer with if and else
    if my_answers[1] == answers[1]:
        results[1] = True
    elif my_answers[1] != answers[1]:
        results[1] = False
    if my_answers[2] == answers[2]:
        results[2] = True
    elif my_answers[2] != answers[2]:
        results[2] = False
    if my_answers[3] == answers[3]:
        results[3] = True
    elif my_answers[3] != answers[3]:
        results[3] = False
    if my_answers[4] == answers[4]:
        results[4] = True
    elif my_answers[4] != answers[4]:
        results[4] = False
    #6 this function does several things in one long block
    count_correct = 0
    count_incorrect = 0
    for result in results:
    #7 The code counts both correct and incorrect answers.
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
    #8 The pass rate has been hard-coded into the function
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
