import pychromecast
import time
import re
from pychromecast.controllers.youtube import YouTubeController

def conectar_chromecast(chromecast_nombre="lautizhin"):
    chromecasts, browser = pychromecast.get_chromecasts()
    time.sleep(2)

    if not chromecasts:
        print("No se encontraron Chromecasts")
        return None

    for cc in chromecasts:
        if cc.name.lower() == chromecast_nombre.lower():
            cc.wait()
            pychromecast.discovery.stop_discovery(browser)
            return cc

    pychromecast.discovery.stop_discovery(browser)
    print(f"No se encontró un Chromecast llamado '{chromecast_nombre}'")
    return None

def extraer_video_id(url):
    patron = r"(?:https?:\/\/)?(?:www\.)?youtu(?:\.be|be\.com)\/(?:watch\?v=|embed\/|v\/|.+\?v=)?([^&\n?#]+)"
    coincidencia = re.search(patron, url)
    return coincidencia.group(1) if coincidencia else None

def abrir_youtube(chromecast, video_url):
    if chromecast is None:
        print("No se pudo conectar al Chromecast.")
        return

    video_id = extraer_video_id(video_url)
    if not video_id:
        print("URL de YouTube no válida.")
        return

    yt = YouTubeController()
    chromecast.register_handler(yt)
    yt.play_video(video_id)
    print(f"Reproduciendo: {video_url}")
