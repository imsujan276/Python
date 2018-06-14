from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint

baseurl = "http://www.ironmongerydirect.co.uk"
url = 'http://www.ironmongerydirect.co.uk/browse/door-furniture'


# names = []
# years = []
# imdb_ratings = []
# metascores = []
# votes = []

product_urls = []
image_urls = []
product_names = []
product_prices = []
product_types = []
product_reviews = []


response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
products_containers = html_soup.find_all('li', class_ = 'variation3')
# first_product = products_containers[0]
# # print(first_product.div.span.text)
# print(baseurl + first_product.a['href'])
# print(baseurl + first_product.a.img['src'])
# print(first_product.h3.text)
# # print(first_product.div['class=product_rating'].span.text)
# for row in first_product.find_all('div',attrs={"class" : "product_rating"}):
#     print(row.span.text)

# for row in first_product.find_all('div',attrs={"class" : "info"}):
#     print(row.table.th.text)
#     print(row.table.td.text)

# print("************************* First Movie a *********************")
# print(first_product.a)
# print("************************* First Movie h3 *********************")
# print(first_product.h3)
# print("************************* First Movie h3 > a *********************")
# print(first_product.h3.a)
# print("************************* First Movie h3 > a > text *********************")
# print(first_product.h3.a.text)


# Extract data from individual movie container
for container in products_containers:
    # If the movie has Metascore, then extract:
    # if container.find('div', class_ = 'ratings-metascore') is not None:

#     # The name
    product_url  = container.a['href']
    product_urls.append(baseurl + product_url)

    
    image_url = container.a.img['src']
    image_urls.append(image_url)

    
    product_name = container.h3.text
    product_names.append(product_name)

    if container.find('div', class_ = 'product_rating') is not None:
        product_review1 = container.find('div', class_ = 'product_rating')
        product_review = product_review1.find('span', class_ = 'red_txt').text
    else:
        product_review = '(0)'
    product_reviews.append(product_review)


    for row in container.find_all('div',attrs={"class" : "info"}):
        product_types.append(row.table.th.text)
        product_prices.append(row.table.td.text)

df = pd.DataFrame({'product_url': product_urls,
                       'image_url': image_urls,
                       'product_name': product_names,
                       'product_type': product_types,
                       'product_price': product_prices,
                       'product_review': product_reviews})
df.to_csv('products-in-door-furniture.csv', sep='\t', encoding='utf-8')
print(df)
