import random
import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = os.environ.get('STOCK_API')
NEWS_API = os.environ.get('NEW_API')

account_sid = "ACe1bddcb8b1b001e5693d1575bafef782"
auth_token = "w"


# --- STOCK DATA ---

def get_stock_data():

    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol":STOCK_NAME,
        "apikey":"w"
    }

    stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    try:
        stock_response.raise_for_status()
        data = stock_response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def get_dates(data):
    try:
        dates = sorted(data['Time Series (Daily)'].keys(), reverse=True)
        return dates
    except KeyError:
        print("You used 25 request per day")
        return None

def calculate_change(yesterday_close, day_before_yesterday_close):
    return round(((float(yesterday_close) - float(day_before_yesterday_close)) / float(day_before_yesterday_close)) * 100, 2)

# --- NEWS DATA ---

def get_news(dates):
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "from": dates[0],
        "sortBy": "popularity",
        "apiKey": "w"
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    try:
        news_response.raise_for_status()
        news_data = news_response.json()["articles"][:3]
        news_list = [[article.get('title', 'Brak tytułu'), article.get('description', 'Brak opisu')] for article in news_data]

        return news_list
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def main():
    data = get_stock_data()
    dates = get_dates(data)
    if dates:
        yesterday_date = dates[0]
        day_before_yesterday_date = dates[1]
        yesterday_close_price = data['Time Series (Daily)'][yesterday_date]["4. close"]
        day_before_yesterday_close_price = data["Time Series (Daily)"][day_before_yesterday_date]["4. close"]
        change = calculate_change(yesterday_close_price,day_before_yesterday_close_price)

        articles = get_news(dates)
        rand_articles = random.choice(articles)
        rand_news_title = rand_articles[0]
        rand_news_description = rand_articles[1]

        if change > 0.01:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"{COMPANY_NAME}: 🔺{change}%"
                     f"Headline: {rand_news_title}({STOCK_NAME})?. "
                     f"Brief: {rand_news_description}",
                from_="+18573418987",
                to="+w",
            )
            print("Stock raises")
            print(message.status)
        elif change < -0.01:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"{COMPANY_NAME}: 🔻{change}%"
                     f"Headline: {rand_news_title}({STOCK_NAME})?. "
                     f"Brief: {rand_news_description}",
                from_="+18573418987",
                to="+w"
            )
            print("Stock dropped")
            print(message.status)
        else:
            print(f"{change:.2f}%")


main()
