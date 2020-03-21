import bs4, requests


def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.findAll("h2", {"class": "display-price"})

    price = elems[0].text.strip()

    print('The price is ' + price)

getEbayPrice('') # Put the eBay url in here!
