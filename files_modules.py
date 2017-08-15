test_list = ['cat','dog','sparrow']

def print_list(l, numbered=True, bullet_character='-'):
    """Prints a list on multiple lines, with numbers or bullets
    
    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))







files = []
for i in range(10000):
     files.append(open('/Users/matt/Documents/python_learning/somefile.txt'))
     
     
f = open('/Users/matt/Documents/python_learning/somefile.txt','r')

f.close()

flying_circus_cast.txt

def create_cast_list(filename,ext='.txt'):
    cast_list = []
    file_location = '/Users/matt/Documents/python_learning/{}{}'.format(filename,ext)
    #use with to open the file filename
    with open(file_location) as f:
    #use the for loop syntax to process each line
        for line in f:
            line_data = line.split(',')
    #and add the actor name to cast_list
            cast_list.append(line_data[0])
        return(cast_list)


import math
def common_divisor(input):
    return(math.pow(input,3))
    
    
    
    
from collections import defaultdict

    

