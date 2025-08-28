import requests
from bs4 import BeautifulSoup
import pprint

num_pages = 2
count = 1

links = []
subtext = []

while count <= num_pages:
    web_link = "https://news.ycombinator.com/"
    
    if count > 1:
        web_link += f"?p={count}"
    
    count += 1

    res = requests.get(web_link)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        links += soup.select('.titleline')
        subtext += soup.select('.subtext')


def create_custom_hn(links, subtext):
    hn = []
    for idx, _ in enumerate(links):
        title = links[idx].getText()
        href = links[idx].select_one("a").get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sorted(hn, key=lambda x: x['votes'], reverse=True)


pprint.pprint(create_custom_hn(links, subtext))