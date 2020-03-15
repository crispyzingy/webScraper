import bs4
import requests


def getAmazonPrice(productUrl):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select(
        "#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal"
    )  # selector
    return elems[0].text.strip()


price = getAmazonPrice(
    "https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994"
)
print("The price is " + price)

