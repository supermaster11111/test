import yaml
from pathlib import Path

CONFIG_PATH = Path('config/config.yaml')
SECRETS_PATH = Path('config/secrets.yaml')
DEFAULT_SECRETS_PATH = Path('config/secrets.example.yaml')

with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    CONFIG = yaml.safe_load(f)

if SECRETS_PATH.exists():
    with open(SECRETS_PATH, 'r', encoding='utf-8') as f:
        SECRETS = yaml.safe_load(f)
else:
    with open(DEFAULT_SECRETS_PATH, 'r', encoding='utf-8') as f:
        SECRETS = yaml.safe_load(f)

DATA_JSON = Path('app/frontend/assets/data.json')
OUTPUT_TITLES = Path('data/outputs/titles.json')
SCREENSHOT_DIR = Path('data/outputs/screenshots')
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
