import textstat

def analyze_email(email):

    readability = textstat.flesch_reading_ease(email)

    if readability >= 70:
        level = "Easy to Read"
    elif readability >= 50:
        level = "Moderate"
    else:
        level = "Difficult"

    return {
        "readability_score": readability,
        "reading_level": level
    }