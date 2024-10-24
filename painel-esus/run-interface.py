# pylint: disable=W0611, C0103
import sys
from sys import argv

from apscheduler.schedulers.background import BackgroundScheduler
from interface import start_interface
from src.main.composers.schedule_compose import generate_base_scheduled
from src.main.server.server import app

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "config":
        start_interface()
        print(sys.argv[0])
    else:
        if not app.debug:
            scheduler = BackgroundScheduler()
            scheduler.start()
            generate_base_scheduled(scheduler)

        app.run(host="0.0.0.0", port=5001, debug=False)
