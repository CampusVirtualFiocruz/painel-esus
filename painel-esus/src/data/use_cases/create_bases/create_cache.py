import asyncio
from datetime import datetime, timedelta
from pprint import pprint
from time import perf_counter

import aiohttp
import requests
from src.infra.db.repositories.city_informations_repository import \
    CityInformationsRepository
from src.main.routes.city_informations_route import CityInfoPath
from src.main.routes.demographics_info_route import DemographichInfoPath
from src.main.routes.diabetes_routes import DiabetesPath
from src.main.routes.hypertension_routes import HypertensionPath
from src.main.routes.oral_health import OralHealthPath
from src.main.routes.units_route import UnitsPath
from src.main.server.decorators.token_required import generate_token
from src.errors.logging import logging


class CreateCacheUseCase:

    def __init__(self):
        pass

    async def _get_page(self, session, url):
        async with session.get(url) as r:
            if r.status != 200:
                print(url + "\t", end='')
                pprint(r.text())

    async def _get_all(self, session, urls):
        tasks = []
        for url in urls:
            task = asyncio.create_task(self._get_page(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results

    async def _main(self, urls, token):
        headers = {"Authorization": "Bearer "+token}
        async with aiohttp.ClientSession(headers=headers) as session:
            data = await self._get_all(session, urls)
            return data

    def generate_cache(self):
        start = datetime.now()

        token = generate_token(
            'adm',
            'adm',
            'adm',
            'adm',
            ['adm']
        )
        urls = []
        second_round = []

        city_info = CityInformationsRepository()
        units_list = city_info.get_units().to_dict(orient='records')

        city = CityInfoPath()
        demographic = DemographichInfoPath
        units = UnitsPath()
        root_path = 'http://localhost:5001'

        urls.append(root_path + city.root_path)
        urls.append(root_path + demographic.root_path)
        urls.append(root_path + units.root_path)

        hypertension = HypertensionPath()
        for url in hypertension.urls.values():
            urls.append(root_path + hypertension.root_path + url)
            for cnes in units_list:
                urls.append(root_path + hypertension.root_path +
                            url + f"/{cnes['co_seq_dim_unidade_saude']}")

        diabetes = DiabetesPath()
        for url in diabetes.urls.values():
            urls.append(root_path + diabetes.root_path + url)
            for cnes in units_list:
                urls.append(root_path + hypertension.root_path +
                            url + f"/{cnes['co_seq_dim_unidade_saude']}")

        oral = OralHealthPath()
        for url in oral.urls.values():
            urls.append(root_path + oral.root_path + url)
            for cnes in units_list:
                urls.append(root_path + hypertension.root_path +
                            url + f"/{cnes['co_seq_dim_unidade_saude']}")

        asyncio.run(self._main(urls, token))

        for url in hypertension.urls.values():
            for cnes in units_list:
                second_round.append(root_path + hypertension.root_path +
                                    url + f"/{cnes['co_seq_dim_unidade_saude']}")

        for url in diabetes.urls.values():
            for cnes in units_list:
                second_round.append(root_path + hypertension.root_path +
                                    url + f"/{cnes['co_seq_dim_unidade_saude']}")

        for url in oral.urls.values():
            for cnes in units_list:
                second_round.append(root_path + hypertension.root_path +
                                    url + f"/{cnes['co_seq_dim_unidade_saude']}")
        asyncio.run(self._main(second_round, token))
        stop = datetime.now()
        time_result = stop - start
        logging.info(f"time taken: {time_result}")
