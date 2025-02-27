import re as r
import socket
from urllib.request import urlopen

from apscheduler.schedulers.background import BackgroundScheduler
from src.errors.logging import logging
from src.main.composers.schedule_compose import generate_base_scheduled
from src.main.server.server import app


def getIP():
    d = str(urlopen('http://checkip.dyndns.com/').read())
    return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

if __name__ == "__main__":
    if not app.debug:
        scheduler = BackgroundScheduler()
        scheduler.start()
        generate_base_scheduled(scheduler)

    port = 5001
    host = "0.0.0.0"
    ip = socket.gethostbyname(socket.gethostname())
    ip2=getIP()
    logging.info("Geração Terminada.")
    logging.info(f"""Servidor do painel iniciado:
        PORTA: {port}
        HOST:
            http://{host}{port}
            http://{ip}{port}
            http://{ip2}{port}
            http://localhost:{port}
    """)
    app.run(host=host, port=port, debug=False)
