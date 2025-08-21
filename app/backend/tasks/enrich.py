import json
from urllib.parse import quote
from .config import DATA_JSON
from .logger import logger

SOURCE_TEMPLATES = {
    "AniList": "https://anilist.co/search/anime?search={}",
    "MyAnimeList": "https://myanimelist.net/search/all?q={}",
    "MangaDex": "https://mangadex.org/search?q={}",
    "NovelUpdates": "https://www.novelupdates.com/?s={}",
    "Tapas": "https://tapas.io/search/{}/series",
    "Webnovel": "https://www.webnovel.com/search?keyword={}",
    "KakaoPage": "https://page.kakao.com/search?word={}",
    "Lezhin": "https://www.lezhinus.com/en/search?q={}",
    "Tappytoon": "https://www.tappytoon.com/en/search?query={}",
    "Naver Webtoon": "https://comic.naver.com/search?keyword={}",
    "WEBTOONS": "https://www.webtoons.com/en/search?keyword={}",
    "Bilibili Comics": "https://manga.bilibili.com/search/keyword/{}",
    "Piccoma": "https://piccoma.com/web/search/?key={}",
    "BookWalker": "https://bookwalker.jp/search/?q={}",
    "Comic-Walker": "https://comic-walker.com/search/?q={}",
    "Alphapolis": "https://www.alphapolis.co.jp/search?q={}",
    "Pixiv": "https://www.pixiv.net/tags/{}/artworks",
    "Pixiv Comics": "https://comic.pixiv.net/search?keyword={}",
    "Crunchyroll": "https://www.crunchyroll.com/search?from=&q={}",
    "Novelcool": "https://www.novelcool.com/search/?keywords={}",
    "Alpha Manga": "https://alpha-manga.com/search?q={}",
    "Niadd": "https://www.niadd.com/search/?name={}",
    "Toonclash": "https://toonclash.com/search?keyword={}",
    "Jnovels": "https://jnovels.com/?s={}",
    "Justlightnovels": "https://justlightnovels.com/?s={}",
    "Elscione": "https://www.elscione.com/search/{}/",
    "Novelbin": "https://novelbin.me/search?keyword={}",
    "Syosetu": "https://syosetu.com/search/?word={}",
    "Kakuyomu": "https://kakuyomu.jp/search?q={}",
    "Mechacomic": "https://mechacomic.jp/search?keyword={}",
    "Piccoma(web)": "https://piccoma.com/web/search/?key={}",
    "Bookwalker.jp": "https://bookwalker.jp/search/?q={}",
    "Comic-walker.com": "https://comic-walker.com/search/?q={}",
    "Estar": "https://estar.jp/search?t={}",
    "Mangakakalot": "https://mangakakalot.com/search/story/{}",
    "Mangapark": "https://mangapark.net/search?title={}",
    "Mangasee123": "https://mangasee123.com/search/?name={}",
    "Bato.to": "https://bato.to/search?name={}",
    "Reaper Scans": "https://reaperscans.com/search?q={}",
    "Asura Scans": "https://asurascans.com/?s={}",
    "Flame Scans": "https://flamescans.org/?s={}",
    "Realm Scans": "https://realmscans.com/?s={}",
    "Manhwatop": "https://manhwatop.com/?s={}",
    "Manhuascan": "https://manhuascan.com/search?keyword={}",
    "1stkissmanga": "https://1stkissmanga.me/?s={}",
    "Topmanhua": "https://topmanhua.com/?s={}",
    "Leviatanscans": "https://leviatanscans.com/?s={}",
    "Anime-Planet": "https://www.anime-planet.com/search?name={}"
}


SPECIAL_TITLES = {
    "Farming Life in Another World": "https://isekainonbirinoukachapters.com/",
    "Tales of Wedding Rings": "https://kekkonyubiwamonogatari.com/"
}


def enrich_items():
    data = json.loads(DATA_JSON.read_text())
    for item in data.get('items', []):
        title = item['title']
        links = []
        for source, tmpl in SOURCE_TEMPLATES.items():
            url = tmpl.format(quote(title))
            links.append({"source": source, "url": url})
        if title in SPECIAL_TITLES:
            links.append({"source": "Official", "url": SPECIAL_TITLES[title]})
        links.append({"source": "Google", "url": f"https://www.google.com/search?q={quote(title)}"})
        item['links'] = links
    DATA_JSON.write_text(json.dumps(data, indent=2))
    logger.info("Enrichment complete for %d items", len(data.get('items', [])))
    return {"count": len(data.get('items', []))}
