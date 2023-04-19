import requests

URL = ('https://newsapi.org/v2/top-headlines?')

API_KEY='ad481a47d8504d94b0b84eab6bf5c819'

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []

    for article in articles:
        results.append({"title": article['title'], "url": article['url']})
    
    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

def get_sourcs_by_category(category):
    pass

if __name__ == '__main__':
    pass