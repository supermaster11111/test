import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .config import DATA_JSON, SECRETS
from .logger import logger


def export_sheets():
    data = json.loads(DATA_JSON.read_text())
    creds_path = 'config/' + SECRETS['google']['service_account_json']
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open('Crunchyroll Media Tracker').sheet1
    header = ["Title", "Type", "PersonalRating", "Favorite", "Downloaded", "Format", "ScreenshotPath"]
    rows = [header]
    for item in data.get('items', []):
        rows.append([
            item.get('title'),
            item.get('type'),
            item.get('personal_rating'),
            'Yes' if item.get('favorite') else 'No',
            'Yes' if item.get('downloaded') else 'No',
            item.get('format'),
            item.get('screenshot')
        ])
    sheet.clear()
    sheet.append_rows(rows)
    logger.info("Google Sheet updated")
    return {"rows": len(rows) - 1}
