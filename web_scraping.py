# Part 1 - Web Scraping
import requests
import bs4

r = requests.get('https://news.google.com')
soup = bs4.BeautifulSoup(r.text, 'html.parser')

headlines = soup.select('.esc-lead-article-title')

headline_list = []
# printing out headlines
for headline in headlines:
    headline_list.append(headline.text)
    # print("headline: {}".format(headline.text))
# print(headline_list)

def find_headline_by_keyword(word):
    return [title for title in headline_list if word in title]

# example
# print(find_headline_by_keyword('NASA'))
## right now:
## ['Buzz Aldrin to NASA: Retire the International Space Station ASAP to Reach Mars']


# Part 2 - Web Scraping + File IO
# order, year, winner, winner electoral votes, runner-up, and runner-up electoral votes
# Use commas as the delimiter.
r = requests.get('https://en.wikipedia.org/wiki/United_States_presidential_election')
soup = bs4.BeautifulSoup(r.text, 'html.parser')

info = soup.select('.wikitable')[0]
# print(info)
# add more table selection manipulation/deal with merged cells somehow...

# Part 3 - Server Side Requests
# prompts the user for two pieces of information, the name of an actor/actress and a movie
# Your program should tell the user if that actor or actress was in that
# movie (this will only work for leading actors and actresses). As a
# bonus, add functionality to tell users who the director and writer of a
# movie were.

print("Please enter the following to see if actor/actress was a lead in a movie: ")
actor = input("Name of actor/actress: ")
title = input("Title of movie: ")

r = requests.get('https://www.omdbapi.com/?t=' + title)
JSON_data = r.json()

def check_actor_in_movie(actor, title):
    if actor in JSON_data['Actors']:
        return "Yes, {} is in '{}'".format(actor, title) #True
    return "No, {} is not in '{}'".format(actor, title) #False

print(check_actor_in_movie(actor, title))

# example
# Name of actor/actress: Jennifer Garner
# Title of movie: Alias
# > Yes, Jennifer Garner is in Alias