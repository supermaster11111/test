from openpyxl import Workbook
from .config import DATA_JSON
import json
from pathlib import Path
from .logger import logger

OUTPUT_XLSX = Path('data/outputs/CrunchyTracker.xlsx')


def export_excel():
    data = json.loads(DATA_JSON.read_text())
    wb = Workbook()
    ws = wb.active
    ws.append(["Title", "Type", "PersonalRating", "Favorite", "Downloaded", "Format", "ScreenshotPath"])
    for item in data.get('items', []):
        ws.append([
            item.get('title'),
            item.get('type'),
            item.get('personal_rating'),
            'Yes' if item.get('favorite') else 'No',
            'Yes' if item.get('downloaded') else 'No',
            item.get('format'),
            item.get('screenshot')
        ])
    OUTPUT_XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUTPUT_XLSX)
    logger.info("Excel export complete: %s", OUTPUT_XLSX)
    return {"path": str(OUTPUT_XLSX)}
