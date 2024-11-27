from apscheduler.schedulers.background import BackgroundScheduler
from src.main.composers.schedule_compose import generate_base_scheduled
from src.main.server.server import app

if __name__ == "__main__":
    if not app.debug:
        scheduler = BackgroundScheduler()
        scheduler.start()
        generate_base_scheduled(scheduler)
        
    app.run(host="0.0.0.0", port=5001, debug=False)
