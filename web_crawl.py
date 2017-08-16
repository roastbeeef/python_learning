import requests


response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
print(response.text)
print(type(response.text))


# import beautifulsoup
from bs4 import BeautifulSoup

# create the response
response = requests.get('https://en.wikipedia.org/')

# turn the response into text and assign to the object 'html'
html = response.text

# using beautfulsoup html parser on the html object (defined above) and assigning it to a new soup object
soup = BeautifulSoup(html, 'html.parser')

# returning the title tag from the soup object.  the annotation is object.tag
soup.title
# returning a paragraph
soup.p
# you can drill down further into the child tags... ()
soup.p.b
# and even further... (anchor tags for the hyperlink)
soup.p.b.a
# finds all anchor tags within the page
soup.find_all('a')
# finds a div item
soup.find(id="mw-page-base")

soup.div


 define the function that needs to be run
# contain this function within a while loop
        
        
# =============================================================================
# if the most recent article in the search_history is the target article the search should stop and the function should return False
# If the list is more than 25 urls long, the function should return False
# If the list has a cycle in it, the function should return False
# otherwise the search should continue and the function should return True.
# =============================================================================



from bs4 import BeautifulSoup    
import time
def web_crawl():
    while continue_crawl(article_chain, target_url): 
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds
        time.sleep(2)
        
        
def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    # get the HTML from "url", use the requests library
    # feed the HTML into Beautiful Soup
    # find the first link in the article
    # return the first link as a string, or return None if there is no link 
    article_link = 'a url, or None'

    if article_link:
        return article_link





# =============================================================================
# exploration
# =============================================================================

import time
import urllib
from bs4 import BeautifulSoup
import requests


start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
#   specify the target URL and assign to response object
    response = requests.get(url)
#   create html object as html text output
    html = response.text
#   print html output
#   feed html output into beautifulsoup
    soup = BeautifulSoup(html,'html.parser')

#   use beautifulsoup to scan through the html to find the;
#   div id = mw-content-text
#   sub class = mw-parser-output
#   drill into paragraph
#   drill into anchor
#   get the href (link) from the anchor tag
#   this div contains the articles body
    content_div = soup.find(id='mw-content-text').find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None


# Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    
    if not article_link:
        return 

# Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    
    return first_link

def continue_crawl(search_history, target_url, max_hops=25):
#    first if statement - if the most recent item is the same as the target url, then we've succeeded
    if search_history[-1] == target_url:
#    outcome is to print a message for the user and end the loop
        print('target article found')
        return False
#    second if statement - if the length of the search history object exceeds 25 items, then we'll close the loop
    elif len(search_history) > 25:
#    outcome is to print a message for the user and end the loop
        print('too many hops')
        return False
#    third if statement - if we can find the most recent entry in the search history list within the entire search history list, close the loop
    elif search_history[-1] in search_history[:-1]:
#    outcome is to print a message for the user and end the loop
        print('stuck in a cycle')
        return False
    else:
        return True

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)
    
    time.sleep(2)
            



# =============================================================================
# try it out (manually)
# learn
# design
# write code
# test
# iterate
# =============================================================================
