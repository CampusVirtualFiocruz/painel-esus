from urllib.request import urlopen

from apscheduler.schedulers.background import BackgroundScheduler
from src.env.conf import getenv
from src.main.composers.schedule_compose import generate_base_scheduled
from src.main.server.server import app

if __name__ == "__main__":
    if not app.debug:
        scheduler = BackgroundScheduler()
        scheduler.start()
        generate_base_scheduled(scheduler)
    port = getenv("PORT", 5001, False)
    host = "0.0.0.0"

    certificate_path =  getenv("CERT_PATH", None, numeric=False)
    if certificate_path is not None:
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
        app.run(
            host=host,
            port=port,
            debug=False
        )
