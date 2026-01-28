import psutil
import random

def detectar_dispositivos_rede():
    """
    Detecta dispositivos conectados à mesma rede local
    """
    dispositivos = set()

    for conn in psutil.net_connections(kind="inet"):
        if conn.raddr:
            dispositivos.add(conn.raddr.ip)

    return list(dispositivos)

def classificar_proximidade():
    """
    Simula a proximidade do dispositivo móvel em relação à TV
    """
    latencia_ms = random.randint(5, 100)

    if latencia_ms < 20:
        return "muito_proximo"
    elif latencia_ms < 50:
        return "proximo"
    else:
        return "distante"
