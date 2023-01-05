import requests

def test_scrapping():
    response = requests.get("http://0.0.0.0:8000/scraping/lifemovie")
    if response.status_code == 200:
        print("API call is successful")

    else:
        print("API call is failed")

test_scrapping()