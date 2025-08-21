from flask import Flask, request, jsonify
from flask_cors import CORS
from .ui_blueprint import ui
from .tasks import scanner, enrich, excel, google_sheets, mega_client, sauce, recommendations, voice
from .tasks.config import DATA_JSON
import json


def create_app():
    app = Flask(__name__, static_folder=None)
    CORS(app)
    app.register_blueprint(ui)

    @app.get('/api/ping')
    def ping():
        return jsonify({'ok': True})

    @app.post('/api/scan/crunchyroll')
    def scan_crunchyroll_endpoint():
        return jsonify(scanner.scan_crunchyroll())

    @app.post('/api/scan/both')
    def scan_both_endpoint():
        return jsonify(scanner.scan_both())

    @app.post('/api/enrich')
    def enrich_endpoint():
        return jsonify(enrich.enrich_items())

    @app.post('/api/export/excel')
    def export_excel_endpoint():
        return jsonify(excel.export_excel())

    @app.post('/api/export/sheets')
    def export_sheets_endpoint():
        return jsonify(google_sheets.export_sheets())

    @app.post('/api/mega/create-folders')
    def mega_folders_endpoint():
        data = json.loads(DATA_JSON.read_text())
        titles = [item['title'] for item in data.get('items', [])]
        return jsonify(mega_client.create_folders(titles))

    @app.post('/api/sauce/text')
    def sauce_text_endpoint():
        q = request.json.get('query', '')
        return jsonify(sauce.sauce_text(q))

    @app.post('/api/sauce/image')
    def sauce_image_endpoint():
        file = request.files['image']
        return jsonify(sauce.sauce_image(file.read()))

    @app.post('/api/recommend')
    def recommend_endpoint():
        mood = request.json.get('mood', '')
        return jsonify(recommendations.recommend(mood))

    voice.start_voice_thread()
    return app
