length, width, height = 52, 40, 100


def hours2days(input):
    day_length_in_hours = 24
    output = (input // day_length_in_hours, input % day_length_in_hours)
    return(output)
    
# think about readability!!
def hours2days_cleaner(input):
    day_length_in_hours = 24
    days = input // day_length_in_hours
    weeks = input % day_length_in_hours
    output = (days,weeks)
    return(output)
    
    
    type