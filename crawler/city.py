import requests
from bs4 import BeautifulSoup

allCities = []


def getCity(step):
    url = f"https://epostcode.post.ir/codeFinder/chooseLocation?state={step}"
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
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'iframe',
        'Referer': 'https://epostcode.post.ir/codefinder/chooseState/',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': '.SESSID=4vfmmnwl2wlh2zmfyhbmgh4b; ST=0QrZf8mz240Rz7oej6O6m6H89EtZ3n'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    cities = []
    
    for link in soup.find_all('a'):
        cities.append(link.get_text()[4:])
        
    allCities.append(cities[1:])

    for index in range(len(allCities)):
        allCities[index].sort()


step = 1

while(step <= 31):
    if(step <= 9):
        step = "0" + str(step)
        getCity(step)

    elif step == 20:
        getCity(24)

    elif step == 21:
        getCity(25)

    elif step == 22:
        getCity(26)

    elif step == 23:
        getCity(27)

    elif step == 24:
        getCity(28)

    elif step == 25:
        getCity(29)

    elif step == 26:
        getCity(30)

    elif step == 27:
        getCity(20)

    elif step == 28:
        getCity(21)

    elif step == 29:
        getCity(22)

    elif step == 30:
        getCity(23)

    else:
        getCity(step)
    step = int(step) + 1
