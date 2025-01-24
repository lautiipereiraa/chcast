import time
from chromecast_control import conectar_chromecast
from reconocimiento import reconocer_voz


def esperar_conexion(chromecast):
    """Espera hasta que el Chromecast esté completamente conectado y listo."""
    print("Esperando a que el Chromecast esté completamente conectado...")
    while chromecast.status is None:
        print("Esperando la conexión...")
        time.sleep(2)
    print("Chromecast conectado, esperando que esté listo para reproducir...")

    chromecast.start_app('YouTube') 
    time.sleep(5)  

    while not chromecast.status.playing:
        print("Esperando a que el Chromecast comience a reproducir...")
        time.sleep(2)

    print("Chromecast está listo y reproduciendo.")


def ejecutar_comando(command, chromecast):
    if chromecast is None:
        print("No se pudo conectar al Chromecast.")
        return

    esperar_conexion(chromecast)

    if "reproducir" in command:
        print("Reproduciendo contenido...")
        chromecast.media_controller.play()
    elif "pausar" in command:
        print("Pausando contenido...")
        chromecast.media_controller.pause()
    elif "detener" in command:
        print("Deteniendo contenido...")
        chromecast.media_controller.stop()
    else:
        print("Comando no reconocido.")


if __name__ == "__main__":
    chromecast = conectar_chromecast()

    if chromecast is None:
        print("No se pudo conectar al Chromecast.")
    else:
        esperar_conexion(chromecast)
        while True:
            command = reconocer_voz()
            if command:
                ejecutar_comando(command, chromecast)
