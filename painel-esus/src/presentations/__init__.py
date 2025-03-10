import re as r
import socket

from rich import print
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
    ip = socket.gethostbyname(socket.gethostname())
    try:
        ip2 = f"""http://{getIP()}:{port}"""
    except:
        ip2 = ""

    message = f"""
    \033[38;2;0;0;95mO Painel foi iniciado com sucesso e já pode ser acessado pelos endereços abaixo:\033[0m
    {blod_white}HOST:
            http://localhost:{port}{reset}
            http://{host}:{port}
            http://{ip}:{port}
            {ip2}
    {bold_red} MANTENHA ESTA APLICAÇÃO EM EXECUÇÃO. {reset}
    """
    return message


def rich_banner():
    table = Table(
        expand=True,
    )
    progress_table = table.grid(
        expand=True,
    )

    progress_table.add_row(
        Panel.fit(
            Text.from_ansi(banner_message()),
            title="Painel em execução",
            border_style="white",
            # style="on dark_green",
        ),
    )
    print(progress_table)
