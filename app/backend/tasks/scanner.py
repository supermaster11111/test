import json
from pathlib import Path
from PIL import Image, ImageDraw
from .config import SCREENSHOT_DIR, OUTPUT_TITLES, DATA_JSON
from .logger import logger


def _dummy_screenshot(name: str) -> str:
    path = SCREENSHOT_DIR / f"{name}.png"
    img = Image.new('RGB', (800, 600), 'white')
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), name, fill='black')
    img.save(path)
    return str(path)


def scan_crunchyroll():
    logger.info("Starting Crunchyroll scan (placeholder)")
    paths = []
    paths.append(_dummy_screenshot('STEP_001_LoginPage'))
    paths.append(_dummy_screenshot('STEP_002_Watchlist'))
    items = [{
        "title": "Example Title",
        "type": "Anime",
        "personal_rating": 0,
        "favorite": False,
        "downloaded": False,
        "format": "None",
        "screenshot": paths[-1],
        "sauce_code": "",
        "links": [],
        "notes": ""
    }]
    OUTPUT_TITLES.write_text(json.dumps({"items": items}, indent=2))
    DATA_JSON.write_text(json.dumps({"items": items}, indent=2))
    logger.info("Scan complete")
    return {"count": len(items), "screenshot_paths": paths}


def scan_both():
    result = scan_crunchyroll()
    data = json.loads(DATA_JSON.read_text())
    data['items'].append({
        "title": "Crunchylist Sample",
        "type": "Anime",
        "personal_rating": 0,
        "favorite": False,
        "downloaded": False,
        "format": "None",
        "screenshot": result['screenshot_paths'][-1],
        "sauce_code": "",
        "links": [],
        "notes": ""
    })
    DATA_JSON.write_text(json.dumps(data, indent=2))
    OUTPUT_TITLES.write_text(json.dumps(data, indent=2))
    logger.info("scan_both added placeholder item")
    result['count'] = len(data['items'])
    return result
