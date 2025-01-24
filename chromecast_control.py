import pychromecast

CHROMECAST_IP = "192.168.1.39"

def conectar_chromecast():
    chromecasts, browser = pychromecast.get_chromecasts()
    pychromecast.discovery.stop_discovery(browser)

    for cc in chromecasts:
        print(f"Dispositivo encontrado: {cc.name}")
        print(f"IP del dispositivo: {cc.cast_info.host}")

        if cc.cast_info.host == CHROMECAST_IP:
            print(f"Conectado al dispositivo: {cc.name}")
            return cc
    else:
        print("No se encontró un dispositivo con esa IP.")
        return None

if __name__ == "__main__":
    conectar_chromecast()
