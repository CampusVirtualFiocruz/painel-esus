from datetime import datetime
from datetime import timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from src.data.use_cases.create_bases.create_cache import CreateCacheUseCase
from src.env.conf import env
from src.errors.logging import logging
from src.presentations.controllers.create_bases.create_base_controller import \
    CreateBasesController


def generate_base_scheduled(scheduler: BackgroundScheduler):
    env_time = env.get('RELOAD_BASE_SCHELDULE', '4:00').split(':')
    hour = int(env_time[0])
    minute = int(env_time[1])

    def cache_init():
        try:
            logging.info('Start cache generator.')
            create_cache = CreateCacheUseCase()
            create_cache.generate_cache()
            logging.info('End cache generator.')
        except Exception:
            logging.info('Server not running yet.')

    def init():

        start_time = datetime.now()
        logging.info('Start base generator.')
        controller = CreateBasesController()
        controller.create_bases()

        end_time = datetime.now()
        text = 'Finish base generator. time spent: {}'.format(
            end_time - start_time)
        logging.info(text)
        if "GENERATE_CACHE" in env and env["GENERATE_CACHE"] == "True":
            cache_init()
        else:
            logging.info("skipping base Cache generation.")

    scheduler.add_job(
        init,
        trigger='cron',
        hour=hour,
        minute=minute,
    )
    init()
    if "GENERATE_CACHE" in env and env["GENERATE_CACHE"] == "True":
        logging.info("Scheduling chache generator")
        now = datetime.now()
        now_plus_10 = now + timedelta(minutes=10)
        scheduler.add_job(cache_init, 'date', run_date=now_plus_10)
