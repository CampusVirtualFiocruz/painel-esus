import os
import threading
import webbrowser
from urllib.request import urlopen

from apscheduler.schedulers.background import BackgroundScheduler
from src.env.conf import getenv, is_installed_ok
from src.main.composers.schedule_compose import generate_base_scheduled
from src.main.server.server import app

if __name__ == "__main__":
    if not app.debug:
        scheduler = BackgroundScheduler()
        status, _ = is_installed_ok()
        scheduler.start()
        if status:
            generate_base_scheduled(scheduler)

    port = getenv("PORT", 5001, False)
    host = "0.0.0.0"

    certificate_path =  getenv("CERT_PATH", None, numeric=False)
    if certificate_path is not None and os.path.isfile("local_ssl/tests/pcert.pem"):
        thread = threading.Thread(
            target=lambda : webbrowser.open(f"https://localhost:{port}")
        )
        thread.start()
        app.run(
            host=host,
            port=port,
            debug=False,
            ssl_context=(
                "local_ssl/tests/pcert.pem",
                "local_ssl/tests/private-key.pem",
            ),
        )

    else:
        thread = threading.Thread(
            target=lambda : webbrowser.open(f"http://localhost:{port}")
        )
        thread.start()
        app.run(
            host=host,
            port=port,
            debug=False
        )
