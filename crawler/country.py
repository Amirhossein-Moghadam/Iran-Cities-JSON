import requests
from bs4 import BeautifulSoup

allCountry = []


def getCountry():
    url = "https://epostcode.post.ir/codefinder/chooseState/"

    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'iframe',
        'Referer': 'https://epostcode.post.ir/codefinder',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'ST=b77RG9tAD6MHd2vHHP2uvvthmagv8S; .SESSID=4vfmmnwl2wlh2zmfyhbmgh4b'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        allCountry.append(link.get_text().replace("استان ", ''))


getCountry()
