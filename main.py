from chromecast_control import conectar_chromecast, abrir_youtube
from youtubesearchpython import VideosSearch

def buscar_en_youtube(query):
    search = VideosSearch(query, limit=5)
    results = search.result()["result"]

    videos = []
    for video in results:
        title = video["title"]
        video_id = video["id"]
        videos.append((title, video_id))
    
    return videos

if __name__ == "__main__":
    chromecast = conectar_chromecast()
    
    if chromecast:
        entrada_usuario = input("🔍 Ingrese la URL de YouTube o el nombre del video: ")
        
        if "youtube.com" in entrada_usuario or "youtu.be" in entrada_usuario:
            video_url = entrada_usuario
        else:
            videos = buscar_en_youtube(entrada_usuario)

            if not videos:
                print("❌ No se encontraron resultados.")
                exit()

            print("\n🎥 Videos encontrados:")
            for i, (title, vid) in enumerate(videos):
                print(f"{i+1}. {title} (ID: {vid})")

            choice = int(input("\n👉 Elige un número: ")) - 1
            video_id = videos[choice][1]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

        abrir_youtube(chromecast, video_url)
