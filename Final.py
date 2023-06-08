import requests
from bs4 import BeautifulSoup
def read ( word ):
    url = f'https://www.moedict.tw/{word}'
    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('span', class_='def')
    try:
        return(data.text)
    except:
        return('找不到')
