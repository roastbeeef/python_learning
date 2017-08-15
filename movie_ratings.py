


def convert_to_numeric(score):
    """
    convert the score to a numerical type.
    """
    return(float(score))

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    find the sum of the middle three numbers out of the five given.
    """
    scores = [score1,score2,score3,score4,score5]
    upper = (max(score1,score2,score3,score4,score5))
    lower = (min(score1,score2,score3,score4,score5))
    total = (sum(scores) - upper - lower)
    return(total)
    #return(sum(score1,score2,score3,score4,score5)) - min(score1,score2,score3,score4,score5) - max(score1,score2,score3,score4,score5)
    
def score_to_rating_string(score):
    """
    convert the average score (between 0-5) into a string rating.
    """
    if 0 <= score < 1:
        rating = 'Terrible'
    elif 1 <= score < 2:
        rating = 'Bad'
    elif 2<= score < 3:
        rating = 'OK'
    elif 3 <= score < 4:
        rating = 'Good'
    else:
        rating = 'Excellent'
    return(rating)
        

def scores_to_rating(score1, score2, score3, score4, score5):
    """
    Turns five scores into a rating by averaging the middle three of the five scores and assigning this average to a written rating
    """
    
    # step 1 - convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)    
    
    # step 2 and step 3
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3
        
    # step 4 - turn the average score into a rating
    rating = score_to_rating_string(average_score)
    
    return rating

    