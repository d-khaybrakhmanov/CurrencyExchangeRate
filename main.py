import requests
from bs4 import BeautifulSoup

DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&client=safari&rls=en&sxsrf=ALiCzsaLePXIctjUXCg9OLfc43CWen2RcA%3A1665001449950&ei=6ec9Y_q1OaLprgTvsYCgBg&ved=0ahUKEwi6zuXf9cn6AhWitIsKHe8YAGQQ4dUDCA0&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&gs_lcp=Cgdnd3Mtd2l6EAxKBAhBGABKBAhGGABQAFgAYABoAHAAeACAAQCIAQCSAQCYAQA&sclient=gws-wiz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'}

full_page = requests.get(DOLLAR_RUB, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb",
                                "data-precision": 2})
print(convert[0].text)
