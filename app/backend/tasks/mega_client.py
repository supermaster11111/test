from mega import Mega
from .config import SECRETS
from .logger import logger


def create_folders(titles):
    mega = Mega()
    m = mega.login(SECRETS['mega']['email'], SECRETS['mega']['password'])
    root = m.create_folder('CrunchyMedia')
    created = 0
    for title in titles:
        media_folder = m.create_folder(title, parent=root[0])
        for sub in ['Anime', 'Manga', 'Light Novel', 'Web Novel']:
            m.create_folder(sub, parent=media_folder[0])
        created += 1
    logger.info("Created %d MEGA folders", created)
    return {"created": created}
