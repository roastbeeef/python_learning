def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    month_number -= 1
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    return(days_in_month[month_number])
# This test case should print 31, the number of days in the eighth month, August


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
q3 = months[6:9]
print(q3)
print(months)



first_half = months[:6]
second_half = months[6:]



eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

# mutability - lists are mutable, strings are immutable. mutability is the technical term for whether an object can be modified.
# strings are immutable objects, therefore you cannot change elements within them, you can only change the full string. lists are mutable, therefore you can change individual elements within the list using square brack notation.

sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

nautical_directions = "\n".join(['fore','aft','starboard','port'])

names = ['Garcia','OKelly','Davis']



def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
#    list_sort = sorted(input_list)
    if len(input_list) > 3:
        new_list = sorted(input_list,reverse=True)
        return(new_list[:3])
    else:
        return(sorted(input_list, reverse=True))
        
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    
    
top_three([2,3,5,6,8,4,2,1]) == [8, 6, 5]


test1 = [1,2,3]
test2 = [1,2,3,4]
test3 = [53, 12, 65, 7, 420, 317, 88]


def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    middle_index = int(len(numbers)/2)
    return numbers[middle_index]

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    if len(numbers) % 2:
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        return('odd numbers')

    
    
    
    
    
    
    
    
    