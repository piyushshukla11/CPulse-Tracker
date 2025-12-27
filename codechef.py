import requests
from bs4 import BeautifulSoup

def get_codechef_data(handle):
    url = f"https://www.codechef.com/users/{handle}"
    r = requests.get(url)

    if r.status_code != 200:
        return None

    soup = BeautifulSoup(r.text, "html.parser")
    rating_tag = soup.find("div", class_="rating-number")

    rating = int(rating_tag.text.strip()) if rating_tag else 0

    return {
        "handle": handle,
        "rating": rating
    }
