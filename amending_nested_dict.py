elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't


elements.update({})


elements['is_] = 'test'


elements['helium']["is_noble_gas"] = True
elements['hydrogen']["is_noble_gas"] = False

# =============================================================================
# remember key:value pairs
# =============================================================================
aDict = {}
aDict['test_key'] = '1'




monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

def total_takings(self, yearly_record):
    pass # TODO: Implemenent this function
    total = 0
    for key, value in yearly_record.iteritems():
        if isinstance(value, int):
            total += value
        if isinstance(value, dict):
            total += self.findTotal(value)
    return total
    
# =============================================================================
# solution is here
# =============================================================================
def total_takings(yearly_record):
    pass
    total = 0
#    items = []
    for item in monthly_takings.keys():
        total += sum(monthly_takings[item])
    return(total)

For this quiz, write a function total_takings that calculates the sum of takings from every circus in the year

monthly_takings['January']
sum(monthly_takings['January'].values)

# =============================================================================
# sum of the lists within each dict
# extract key's into list
# extract values for each key
# sum totals
# =============================================================================


def most_prolific(album_list):       
    years = []
    for album_title in album_list:
        years.append(Beatles_Discography[album_title])
    return(max(set(years), key=years.count))
    
    
    
    def findTotal(self, dct):
    total = 0
    for key, value in dct.iteritems():
        if isinstance(value, int):
            total += value
        if isinstance(value, dict):
            total += self.findTotal(value)
    return total