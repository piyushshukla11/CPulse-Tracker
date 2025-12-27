import requests

def get_codeforces_data(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    res = requests.get(url).json()

    if res["status"] != "OK":
        return None

    user = res["result"][0]
    return {
        "handle": handle,
        "rating": user.get("rating", 0),
        "max_rating": user.get("maxRating", 0),
        "rank": user.get("rank", "unrated")
    }
