import threading
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from src.data.use_cases.create_bases.create_cache import CreateCacheUseCase
from src.env.conf import env
from src.errors.logging import logging
from src.main.server.cache import cache
from src.presentations.controllers.create_bases.create_base_controller import (
    CreateBasesController,
)

"""Replace '3' with:

- 0 for Monday
- 1 for Tuesday
- 2 for Wednesday
- 3 for Thursday
- 4 for Friday
- 5 for Saturday
- 6 for Sunday"""
DAY_OF_WEEK = 5


def generate_base_scheduled(scheduler: BackgroundScheduler):
    env_time = env.get("RELOAD_BASE_SCHELDULE", "4:00").split(":")
    weekly = env.get("RELOAD_BASE_SCHELDULE_WEEKLY", "False")
    hour = int(env_time[0])
    minute = int(env_time[1])

    def cache_init():
        try:
            cache.clear()
            logging.info("Start cache generator.")
            create_cache = CreateCacheUseCase()
            create_cache.generate_cache()
            logging.info("End cache generator.")
        except Exception:
            logging.info("Server not running yet.")

    def init():

        start_time = datetime.now()
        logging.info("Start base generator.")
        controller = CreateBasesController()
        controller.create_bases()

        end_time = datetime.now()
        text = "Finish base generator. time spent: {}".format(end_time - start_time)
        logging.info(text)
        if "GENERATE_CACHE" in env and env["GENERATE_CACHE"] == "True":
            cache_init()
        else:
            logging.info("skipping base Cache generation.")

    def run_init_in_thread():
        thread = threading.Thread(target=init)
        thread.start()

    if weekly == "True":
        logging.info("Atualizacao semanal agendada.")
        scheduler.add_job(
            run_init_in_thread,
            trigger="cron",
            hour=hour,
            minute=minute,
            day_of_week=DAY_OF_WEEK,
        )
    else:
        logging.info("Atualizacao diária agendada.")
        scheduler.add_job(
            init,
            trigger="cron",
            hour=hour,
            minute=minute,
        )
    run_init_in_thread()
    if "GENERATE_CACHE" in env and env["GENERATE_CACHE"] == "True":
        logging.info("Scheduling chache generator")
        now = datetime.now()
        now_plus_10 = now + timedelta(minutes=10)
        scheduler.add_job(cache_init, "date", run_date=now_plus_10)
