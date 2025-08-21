import requests
from .logger import logger


def sauce_text(query: str):
    logger.info("Text sauce lookup: %s", query)
    url = "https://graphql.anilist.co"
    gql = """query($search:String){Media(search:$search,type:ANIME){id title{romaji english native} siteUrl coverImage{large}}}"""
    variables = {"search": query}
    res = requests.post(url, json={"query": gql, "variables": variables})
    return res.json()


def sauce_image(image_bytes):
    logger.info("Image sauce lookup")
    files = {'image': image_bytes}
    res = requests.post('https://api.trace.moe/search', files=files)
    return res.json()
