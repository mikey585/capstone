#!/usr/bin/env python3

import os
import json
import urllib.request
import urllib.response
import urllib.error
import random
from nytimesarticle import articleAPI

api = articleAPI("93fc659744f5238f6f95d464865562b8:16:74068039")

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
            page = i)

        for j in articles['response']['docs']:
            if (j["section_name"] in d.keys()):
                if (j["word_count"] and j["web_url"]):
                    d[j["section_name"]].extend([{"name": j["headline"]["main"],
                                        "size": int(j["word_count"]),
                                        "link": j["web_url"]}])
            else:
                d[j["section_name"]] = [{"name": j["headline"]["main"], "size": int(j["word_count"])}]

    for (k, v) in d.items():
        top_node["children"].append({"section_name": k, "children": v})

    json.dump(top_node, temp_file, indent = 2)
    temp_file.close()
    return(news)

def main():
    parse_articles()

if __name__ == "__main__":
    main()
