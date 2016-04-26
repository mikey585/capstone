#!/usr/bin/env python3

import os
import json
import urllib.request
import urllib.response
import urllib.error
import random
from nytimesarticle import articleAPI

api = articleAPI("93fc659744f5238f6f95d464865562b8:16:74068039")
# articles = api.search(begin_date = 20110101,end_date = 20111231, page = 2)
#
# def get_articles(date):
#     '''
#     This function accepts a year in string format (e.g.'1980')
#     and it will return a list of parsed articles (in dictionaries)
#     for that year.
#     '''
#     all_articles = []
#     for i in range(0,99): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
#         articles = api.search(
#                begin_date = str(date + '0101'),
#                end_date = str(date + '1231'),
#                page = str(i))
#         articles = parse_articles(articles)
#         all_articles = all_articles + articles
#     return(all_articles)

def parse_articles():
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = {"children": []}
    path = "C:\\Users\\Bin\\Desktop\\capstone\\json_data\\"
    d = {}
    date = input("Enter a year: ")

    top_node = {"section_name":"Articles",
    "size":500,
    "children": []}

    file_write = date + ".json"
    temp_file = open(os.path.join(path, file_write), 'w')

    for i in range(0,5):
        articles = api.search(
            begin_date =  int(date + "0101"),
            end_date = int(date + "1231"),
            page = random.randrange(10))

        for i in articles['response']['docs']:
            if (i["section_name"] in d.keys()):
                d[i["section_name"]].extend([{"name": i["headline"]["main"],
                                    "size": int(i["word_count"]),
                                    "link": i["web_url"]}])
            else:
                d[i["section_name"]] = [{"name": i["headline"]["main"], "size": int(i["word_count"])}]

    for (k, v) in d.items():
        top_node["children"].append({"section_name": k, "children": v})

    json.dump(top_node, temp_file, indent = 2)
    temp_file.close()
    return(news)

def main():
    parse_articles()

if __name__ == "__main__":
    main()
