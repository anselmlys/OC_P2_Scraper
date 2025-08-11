import re

def transform_rating_in_number(rating_in_text):
    rating_in_text = rating_in_text.lower()

    match rating_in_text:
        case "zero":
            review_rating=0
        case "one":
            review_rating=1
        case "two":
            review_rating=2
        case "three":
            review_rating=3
        case "four":
            review_rating=4
        case "five":
            review_rating=5
        case _:
            review_rating="ND"
    
    return review_rating


def transform_availability_in_number(table):
    number_available = re.sub("[^0-9]", "", table['Availability'])
    return number_available