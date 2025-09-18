import os

import typer
from dotenv import dotenv_values
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

env = {
    **dotenv_values(os.path.abspath(".env")),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}

app = typer.Typer()
console = Console()

variables = [
    {
        "section": "Banco de Dados.",
        "values": [
            {"name": "DB_HOST"},
            {"name": "DB_DATABASE"},
            {"name": "DB_USER"},
            {"name": "DB_PASSWORD"},
            {"name": "DB_PORT"},
        ]
    },
    {
        "section": "Configurações locais.",
        "values": [
            {"name":'CIDADE_IBGE'},
            {"name":'ADMIN_USERNAME'},
            {"name":'ADMIN_PASSWORD'},
            {"name":'BRIDGE_LOGIN_URL'},
            {"name":'RELOAD_BASE_SCHEDULE'},
            {"name":'PORT'},
        ]
    },
]


def default_values( env_dict):
    env_dict['PASSWORD_SALT'] ='painel'
    env_dict['ARTEFACT'] = 'instalador'
    env_dict['ENV'] = 'instalador'
    env_dict['SECRET_TOKEN'] = '111111111111111111111'
    env_dict['GENERATE_BASE'] = 'True'
    env_dict['CHUNK_SIZE'] = '50000'
    env_dict['POLARS_SKIP_CPU_CHECK'] = 'True'
    env_dict['LOG_API'] = 'https://painel-logs.painelsaude.info'
    env_dict['APPLICATION_VERSION'] = '0.9.2'

@app.command()
def main():

    env_dict = dict()
    print(
        Panel(
            f"""
            Esta é uma aplicação para a configuração das variáveis de ambiente do Painel e-SUS APS.
            
            Este é o primeiro passo para a instalação do Painel e-SUS APS, após esta etapa você deve executar o arquivo painel-esus com o comando:
            [bold green on grey0]./painel-esus[/]
            """,
            title="Configuração de Variáveis de ambiente",
            style="on dodger_blue2",
        )
    )
    console.rule("[bold red]", align="right")
    for section in variables:
        print(f"[bold bright_magenta]{section['section']}[/bold bright_magenta]")
        print("")
        for value in section["values"]:
            env_dict[value['name']] = Prompt.ask(
                    f"Defina um valor para [blue]{value['name']}[/blue]?",
                    default=f"{env[value['name']]}" if value['name'] in env and env[value['name']] is not None else None,
                )
            env_dict[value["name"]] = f"'{env_dict[value['name']]}'"
        console.rule("[bold red]", align="right")

    default_values(env_dict)
    result = ""
    for value in env_dict.keys():
        result += f"{value}={env_dict[value]}\n"

    with open('.env', 'w') as f:
        f.write(result)
    console.rule("[bold red]", align="right")
    print(
        Panel(
            f"""
            A configuração das variáveis de ambiente foi concluída com sucesso.
            
            Próximo passo é iniciar a execução do Painel e-SUS APS, rodando o comando:
            [bold green on grey0]./painel-esus[/]
            """,
            title="Configuração concluída com sucesso.",
            style="on dodger_blue2",
        )
    )

if __name__ == "__main__":
    app()
