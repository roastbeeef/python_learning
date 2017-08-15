# Use an import statement at the top
from random import choice

word_list = []
filename = 'words'
ext = '.txt'
location = '/Users/matt/Documents/python_learning/{}{}'.format(filename,ext)


#fill up the word_list
with open(location,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function here
def pass_generator(input_words):
    words = []
    with open(location,'r') as f:
        for line in f:
            line_data = line.split(',')
            line_data = line.strip('\n')
            words.append(line_data)
        print(random.choice(words)+random.choice(words)+random.choice(words))
#        words.append(rnd.word_list)
#        return(rnd.input_words)
            
        
# read input words file
# It should return a string consisting of three random words 
# concatenated together without spaces
        


for x in range(10):
    print('hello')