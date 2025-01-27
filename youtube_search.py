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
