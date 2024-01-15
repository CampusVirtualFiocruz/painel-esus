import requests
from src.main.server.decorators.token_required import generate_token
from src.main.routes.city_informations_route import CityInfoPath
from src.main.routes.demographics_info_route import DemographichInfoPath
from src.main.routes.hypertension_routes import HypertensionPath
from src.main.routes.units_route import UnitsPath

import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch(session, url)) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)


def test_o():
    token = generate_token(
        'adm',
        'adm',
        'adm',
        'adm',
        ['adm']
    )
    urls = []

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

    print(urls)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))


if __name__ == '__main__':
    token = generate_token(
        'adm',
        'adm',
        'adm',
        'adm',
        ['adm']
    )
    urls = []

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

    print(urls)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
