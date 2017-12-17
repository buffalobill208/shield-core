def score_to_rating_string(av_score):
    """
    Convert the average av_score, which should be between 0 and 5,
    into a string rating.
    """
    if av_score < 1:
        rating = "Terrible"
    elif 1 <= av_score < 2:
        rating = "Bad"
    elif 2 <= av_score < 3:
        rating = "OK"
    elif 3 <= av_score < 4:
        rating = "Good"
    else:           #Using else at the end, every possible case gets caught
        rating = "Excellent"
    return rating

print(score_to_rating_string(3))

def score_to_rating_string(av_score):
    """
    Convert the average score, which should be between 0 and 5,
    into a rating.
    """
    if av_score < 1:
        return "Terrible"
    elif av_score < 2:
        return "Bad"
    elif av_score < 3:
        return "OK"
    elif av_score < 4:
        return "Good"
    else:
        return "Excellent"
