import requests
from bs4 import BeautifulSoup


def dolar():
    url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"

    response = requests.get(url)


    soup = BeautifulSoup(response.content, 'html.parser')

    x = soup.find_all("div",class_="kurBox")
    x = list(x)

    result = x[1].text

    

    return result

