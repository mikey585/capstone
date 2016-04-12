#!/usr/bin/env python3
import os
import json
import urllib.request
import urllib.response
import urllib.error
from nytimesarticle import articleAPI

api = articleAPI("93fc659744f5238f6f95d464865562b8:16:74068039")
articles = api.search(begin_date = 20010101,end_date = 20011231)

def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    file_write = open("json_result.txt", "w")
    for i in articles['response']['docs']:
        parent = {}
        children = {}
        # if i['abstract'] is not None:
        #     dic['abstract'] = i['abstract'].encode("utf8")
        # dic['date'] = i['pub_date'][0:10] # cutting time of day.
        # dic['url'] = i['web_url']
        if i["news_desk"] not in parent:
            parent['news_desk'] = i["news_desk"]

        # children['headline'] = i["headline"]['main']
        # children['size'] = i['word_count']
        # parent['children'] = children
        # json.dump(i, file_write, indent = 4)
        news.append(parent)

    file_write.close()
    return(news)

def main():
    for article in parse_articles(articles):
        print(article)

if __name__ == "__main__":
    main()
