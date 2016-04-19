#!/usr/bin/env python3
import os
import json
import urllib.request
import urllib.response
import urllib.error
from nytimesarticle import articleAPI

api = articleAPI("93fc659744f5238f6f95d464865562b8:16:74068039")
articles = api.search(begin_date = 20010101,end_date = 20011231)

def get_articles(date):
    '''
    This function accepts a year in string format (e.g.'1980')
    and a query (e.g.'Amnesty International') and it will
    return a list of parsed articles (in dictionaries)
    for that year.
    '''
    all_articles = []
    for i in range(0,99): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
        articles = api.search(
               begin_date = str(date) + '0101',
               end_date = str(date) + '1231',
               page = str(i))
        articles = parse_articles(articles)
        all_articles = all_articles + articles
    return(all_articles)

def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = {"children": []}
    d = {}
    # date = input("Enter a year: ")

    top_node = {"news_desk":"Articles",
    "size":500,
    "children": []}

    file_write = open("json_result2.json", "w")
    # for i in range(0,99):
    #     articles = api.search(
    #            begin_date = str(date) + "0101",
    #            end_date = str(date) + "1231",
    #            page = i)
    for i in articles['response']['docs']:
        if (i["news_desk"] in d.keys()):
            d[i["news_desk"]].extend([{"name": i["headline"]["main"],
                                "size": int(i["word_count"])}])
        else:
            d[i["news_desk"]] = [{"name": i["headline"]["main"], "size": int(i["word_count"])}]

    for (k, v) in d.items():
        top_node["children"].append({"news_desk": k, "children": v})

    json.dump(top_node, file_write, indent = 2)
    file_write.close()
    return(news)

def main():
    parse_articles(articles)

if __name__ == "__main__":
    main()
