import requests
from bs4 import BeautifulSoup as BS4
#https://realpython.com/beautiful-soup-web-scraper-python/

news_title = []
news_body = [] #this should be a multi array, i cant be fucked

####    Functions   ####

def html_to_plain(item): #this is the module that strips the HTML and turns into string info, IE stuff you see in website
    try:
        print(item.text.strip())
    except:
        pass
def add_list(newstitle,newsbody): #this adds RAW HTML into array, use HTML to plain to print just the text in it, can also use link.strip to get hyper links
    try:
        news_title.append(newstitle)
        news_body.append(newsbody)
        return True
    except:
        print("error appending article")
        return False

def title_checker(first_title,second_title):
    if first_title:
        return first_title
    else:
        return second_title

####    Start   ####

URL = "https://www.stuff.co.nz/national/health/coronavirus" #this is the stuff.co.nz paper, this should work with any stuff.co.nz link
page = requests.get(URL) #gets raw html into string and into pythonobject?

soup = BS4(page.content, "html.parser") #loads the html to plain text module

results = soup.find(id="container") #loads all info in container div
search = "New Covid locations of intrest"

elements = results.find_all("div", class_ = "main_article") #loads all classes that use Main_article into python objects

for item in elements: #for each article preview print the info
    first_title = item.find("h1", class_="first_headline") #if main article itll have this as header
    title = item.find("h3", class_="it-article-headline") #if a smaller article itll print this
    body = item.find("p", class_="intro-content") #this is the body regardless
    #html_to_plain(first_title)
    #html_to_plain(title)
    #html_to_plain(body)#makes a new line between articles
    main_title = title_checker(first_title,title)
    if add_list(main_title,body):
        print("added title")
    else:
        print("error occured, title not added")



x = 0
while x < 5:# is a better way of doing this, suck my dick
    html_to_plain(news_title[x])
    html_to_plain(news_body[x])
    print()
    x += 1
