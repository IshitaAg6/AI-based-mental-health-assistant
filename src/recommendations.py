def get_coping_strategies(sentiment):

    if sentiment['compound'] >= 0.05:
        return "You seem positive! Keep up the self-care with a walk or some meditation."
    elif sentiment['compound'] <= -0.05:
        return "It seems like you're feeling down. Consider reaching out to a friend or practicing deep breathing."
    else:
        return "You seem neutral. A small act of self-care could be beneficial. Try journaling further."

def get_self_care_recommendations(sentiment):

    if sentiment['compound'] >= 0.05:
        return "How about trying some yoga or mindfulness today?"
    elif sentiment['compound'] <= -0.05:
        return "Consider listening to calming music or engaging in a creative hobby."
    else:
        return "Take some time for yourself with a nice cup of tea or some light reading."
