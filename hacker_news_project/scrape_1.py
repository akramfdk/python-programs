import requests
from bs4 import BeautifulSoup

links = []
num_pages = 2  # can change depending on number of pages to scrape

count = 1

while count <= num_pages:
    url = "https://news.ycombinator.com/"
    
    if count > 1:
        url += f"?p={count}"
    count += 1

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        submissions = soup.select(".athing")

        for submission in submissions:
            nxt_sibling = submission.find_next_sibling("tr")
            score_element = nxt_sibling.select_one(".score")
            
            if score_element:
                score = int(score_element.text.split()[0])
                if score > 100:
                    links.append((score,submission.select_one(".titleline").select_one("a")))
    
links.sort(key=lambda x: x[0], reverse=True)

for score, link in links:
    print(f"Score: {score}\nTitle: {link.text}\nLink: {link['href']}\n")