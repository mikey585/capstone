from textblob import TextBlob
from selenium import webdriver
from pymongo import MongoClient

client = MongoClient()
db = client.mydb

# open firefox
driver = webdriver.Firefox()

# load start page
start_url = '''http://opinionator.blogs.nytimes.com/2010/01/01/the-homeland-secretarys-job-security/'''
driver.get(start_url)

# find the phone number
xpath = "//div[@class='entry-content']"
body = driver.find_element_by_xpath(xpath)
body_text = body.text

score = 0
index = 0

blob = TextBlob(str(body_text))
for sentence in blob.sentences:
    score += sentence.sentiment.polarity
    index += 1
    print(sentence.sentiment)

polarity = score / index

result = db.mydb.insert(
    {
        "text" : body_text,
        "polarity" : polarity,
        "url" : start_url
    }
)

print("Polarity", score / index)
# print(body_text.encode('unicode_escape').decode('unicode_escape'))
