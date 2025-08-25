import re as r
import socket

from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text
from src.env.conf import getenv

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

grey = "\x1b[38;20m"
yellow = "\x1b[33;20m"
red = "\x1b[31;20m"
green = "\x1b[32;20m"
blue = "\x1b[34;20m"
bold_red = "\x1b[31;1m"

blod_white = "\x1b[37;1m"
reset = "\x1b[0m"

def getIP():
    d = str(urlopen("http://checkip.dyndns.com/").read())
    return r.compile(r"Address: (\d+\.\d+\.\d+\.\d+)").search(d).group(1)


def banner_message():
    port = getenv("PORT", 5001)
    host = "0.0.0.0"
    certificate_path = getenv("CERT_PATH", None, numeric=False)
    app_url = getenv("APPLICATION_URL", None, numeric=False)

    ip = socket.gethostbyname(socket.gethostname())
    try:
        ip2 = f"""{protocol}://{getIP()}:{port}"""
    except:
        ip2 = ""

    protocol = "http"
    app_url_str = ""
    if certificate_path is not None:
        protocol = 'https'
        app_url_str = "" if app_url is None else app_url

    urls = [
        f'{protocol}://localhost:{port}{reset}',
        f'{protocol}://{host}:{port}',
        f'{protocol}://{ip}:{port}',
    ]
    if ip2:
        urls.append(ip2)
    if app_url_str:
        urls.append(app_url_str)

    url_list = "\n\t".join(urls)
    message = f"""
    \033[38;2;0;0;95mO Painel foi iniciado com sucesso e já pode ser acessado pelos endereços abaixo:\033[0m
    {blod_white}HOST:
        {url_list}
    {bold_red} MANTENHA ESTA APLICAÇÃO EM EXECUÇÃO. {reset}
    """
    return message


def rich_banner():
    layout = Layout(
        
    )
    table = Table(
        expand=True,
    )
    progress_table = table.grid(
        expand=True,
    )
    text = Text()
    layout.update(progress_table)
    progress_table.add_row(
        Panel(
            Text.from_ansi(banner_message()),
            title="Painel em execução",
            border_style="white",
            # style="on dark_green",
        )
    )
    with Live(progress_table, refresh_per_second=4) as live:
        live.update(progress_table)
