import requests
import re
import argparse
from bs4 import BeautifulSoup

p = argparse.ArgumentParser()
p.add_argument("--seed", type=str, default= 'https://weiglemc.github.io/')
p.add_argument("--uris", type=int, default= 500)

args = p.parse_args()
seed_page = args.seed
seed_count = args.uris

seed_dict = {}
seed_sites = [
        "https://www.sports.yahoo.com/",
        "https://www.linkedin.com/",
        "https://www.stanford.edu/",
        "https://www.harvard.edu/",
        "https://www.vpcc.edu/",
        "https://apnews.com/",
        "https://www.nbcnews.com/culture-matters"
]

def collect_uri(seed_page):
    # Use requests to return HTML
    response = requests.get(seed_page, timeout=5)
    # Parse HTML for <a href=""> tags
    soup = BeautifulSoup(response.text, 'lxml')
    # For each tag found, filter only href that begin with http
    for link in soup.find_all('a', {'href':re.compile('^http')}):
        current_href = link.get('href')
        # Use requests to return HTML from 
        response = requests.get(current_href)
        content_type = response.headers.get('content-type')
        # If tag references an HTML file (text/html), check content length.
        if content_type == "text/html" or content_type == "text/html; charset=utf-8" or content_type == "text/html; charset=UTF-8" :
        # Check size in response.headers before checking content-length
            content_size = response.headers.get('content-length')
            c = type(content_size)
            if c != str:
                continue
            # HTML file size true
            else:
                content_length = response.headers['content-length']
                c = int(content_length)
                # content size exists is > 1000, add to unique list and add to next seed item
                if c > 1000:
                    seed_dict[c] = [current_href]
                else:
                    continue

    for i in seed_dict:
        print(i, seed_dict[i])

for links in seed_sites:
    collect_uri(links)