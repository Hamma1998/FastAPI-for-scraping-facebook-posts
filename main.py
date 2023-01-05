from fastapi import FastAPI
from facebook_scraper import get_posts
import uvicorn
import pymongo



app = FastAPI()
@app.get("/")
def read_root():
    return "Welcome in this scraping service for obtaining Facebook public posts. To view all available requests on Swagger, please include /docs at the end of the above URL."



client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

@app.get("/scraping/{post_main_topic}", summary="Please specify the key topic for which you wish to scrape Facebook posts.")
async def scraping_function(post_main_topic):
    try:
        facebook_posts = list(get_posts(post_main_topic, pages=3)) #if we choose a value less than 2, we risk of not getting data from this code instruction
        for post in facebook_posts:
            mydb = client['Scraping']
            information = mydb.facebookposts

            record = {
                'post_main_topic': post_main_topic,
                'post_text': post['text'],
                'post_likes': post['likes'],
                'post_comments': post['comments'],
                'post_shares' : post['shares']
            }
            information.insert_one(record)
    except:
        return "Please enter a value greater than 2 for the pages attribute to get more data, or check to see whether the size of the likes attribute is more than the size of an integer in a mongodb database. "

    return facebook_posts

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")



