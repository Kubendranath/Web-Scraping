from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
# print(yc_web_page)
soup = BeautifulSoup(yc_web_page,"html.parser")
print(soup)
articles = soup.find_all(name = "span", class_= "titleline")
# print(articles)
article_texts = []
article_links = []
for a_tag in articles:
    article_tag = a_tag.find("a")
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span",class_ = "score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
























#
# with open("website.html") as data:
#     contents = data.read()
# soup = BeautifulSoup(contents,"lxml")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

# print(soup.p)
#
# all_anchor_tags = soup.find_all(name = "a")
# # print(all_anchor_tags)
# # # print(soup.a)
# #
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name = "h1", id = "name")
# print(heading)
#
# section_heading = soup.find(name = "h3",class_ = "heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a") /// this gives the firt tag only
# print(company_url)

# name = soup.select_one("#name")
# print(name)

# headings = soup.select(".heading")    //// this selects all the items with the given selector tag..
# print(headings)







