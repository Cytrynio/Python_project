from bs4 import BeautifulSoup
import requests


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

anchor_tags = soup.find_all(name="a", class_='storylink')

#
# sorted_upvotes = sorted(upvotes, reverse=True)
#
# higest_upvotes = sorted_upvotes[0]
# print(higest_upvotes)




for tag in anchor_tags:
    title = tag.getText()
    href = tag.get('href')
    score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
    print(f"Link: {href}, Title: {title if title else 'Brak tytułu'}, Score: {score}")

#
#
#
# for tag in anchor_tags:
#     title = tag.getText()
#     href = tag.get('href')
#     score = int(soup.find(name = "span", class_="score").getText().split()[0])
#     print(f"Link: {href}, Title: {title if title else 'Brak tytułu'}, Score: {score}")
#

















































# import lxml

# with open("website.html", "r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
#
# all_anchor_tags = soup.find_all(name="a")
# print(soup.find_all(name="a"))
#
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)


