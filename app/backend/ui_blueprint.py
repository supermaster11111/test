from flask import Blueprint, send_from_directory
from pathlib import Path

FRONTEND_DIR = Path(__file__).resolve().parent.parent / 'frontend'

ui = Blueprint('ui', __name__)


@ui.route('/')
def index():
    return send_from_directory(FRONTEND_DIR, 'index.html')


@ui.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory(FRONTEND_DIR / 'assets', filename)
