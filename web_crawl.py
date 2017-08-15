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
# you can drill down further into the child tags...
soup.p.b
# and even further...
soup.p.b.a