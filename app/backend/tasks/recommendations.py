import requests
from .config import SECRETS
from .logger import logger


def recommend(mood: str):
    logger.info("Recommendation request for mood: %s", mood)
    gql = """query($search:String){Page(perPage:5){media(search:$search,type:ANIME,sort:POPULARITY_DESC){title{romaji} siteUrl}}}"""
    res = requests.post('https://graphql.anilist.co', json={"query": gql, "variables": {"search": mood}})
    media = res.json().get('data', {}).get('Page', {}).get('media', [])
    recs = [{"title": m['title']['romaji'], "url": m['siteUrl']} for m in media]
    return {"recommendations": recs}
