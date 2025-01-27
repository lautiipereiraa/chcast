from reconocimiento import reconocer_voz
from youtube_search import buscar_en_youtube
from chromecast_control import conectar_chromecast, abrir_youtube

if __name__ == "__main__":
    chromecast = conectar_chromecast()
    
    if chromecast:
        print("🎤 Di el nombre de la canción que quieres buscar:")
        entrada_usuario = reconocer_voz()

        if not entrada_usuario:
            print("❌ No se pudo reconocer la voz.")
            exit()

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
