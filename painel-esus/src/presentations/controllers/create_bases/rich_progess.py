from datetime import datetime
from time import sleep

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from .instalation_status import InstalationStatus

console= Console(stderr=True)

class InstallJobs:
    creation = []
    key_factors = []

    def __init__(self, creation=[], key_factors=[]):
        self.creation = creation
        self.key_factors = key_factors


class StartGeneration:

    MAX_LINES = 3
    def __init__(self, jobs: InstallJobs):
        self.jobs = jobs
        self.logs = Text()
        self.text_logs = []
        self.total = 0
        self.total_proccess_time = datetime.now()
        self.instalacao_status = InstalationStatus()

    def add_log(self, _text):
        self.logs.set_length(0)

        if len(self.text_logs) > self.MAX_LINES:
            self.text_logs.pop(0)
        self.text_logs.append(_text)

        [self.logs.append_tokens(l) for l in self.text_logs]

    def run(self):

        layout = Layout()
        layout.split(
            Layout(name="header"), 
            Layout(name="logs"),
        )

        job_progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        job_progress.add_task(
            "[green]Gerando Base",
            total=len(self.jobs.creation),
        )
        job_progress.add_task(
            "[magenta]Calculando indicadores",
            total=len(self.jobs.key_factors),
        )

        total = sum(task.total for task in job_progress.tasks)
        self.instalacao_status.set_total(total)
        self.instalacao_status.next()

        overall_progress = Progress()

        overall_task = overall_progress.add_task("Instalando", total=int(total))

        progress_table = Table.grid()

        logs = Text()
        text_logs=[]
        progress_table.add_row(
            Panel.fit(
                overall_progress,
                title="Progresso da instalação",
                border_style="green",
                padding=(2, 2),
            ),
            Panel.fit(
                job_progress,
                title="[b]Jobs",
                border_style="yellow",
                padding=(1, 2, 2, 2),
            )
        )

        layout["header"].update(progress_table)
        log_table = Table()
        log_table.add_column("Tabela")
        log_table.add_column("Status")
        log_table.add_column("Duração")

        layout["logs"].update(
            Panel(
                self.logs,
                title="[b]Logs",
                border_style="yellow",
                padding=(1, 1),
                width=800,
            )
        )

        def start_proccess(context, job_progress, overall_progress, instalacao, key):
            start_time = datetime.now()
            context.create_base()
            end_time = datetime.now()
            job_progress.advance(job.id)
            if self.total == 0:
                self.total = end_time - start_time
            else:
                self.total += end_time - start_time
            self.add_log(
                [
                    (f"{context._base}", "bold blue"),
                    ("\tConcluído.",None),
                    ("\t{}.\n".format(
                            end_time - start_time
                        ),
                        None,
                    ),
                ]
            )
            self.instalacao_status.add_log(str(context._base), (end_time - start_time))
            # sleep(0.3)
            completed = sum(task.completed for task in job_progress.tasks)
            if key == 0:
                instalacao.update_base_progress()
            else:
                instalacao.update_indicators_progress()
            overall_progress.update(overall_task, completed=completed)

        with Live(layout, refresh_per_second=4) as live:
            while not overall_progress.finished:
                for key, job in enumerate(job_progress.tasks):

                    if not job.finished:
                        if key == 0:
                            for context in self.jobs.creation:
                                start_proccess(
                                    context,
                                    job_progress,
                                    overall_progress,
                                    self.instalacao_status,
                                    key
                                )
                        if key == 1:
                            for context in self.jobs.key_factors:
                                start_proccess(
                                    context,
                                    job_progress,
                                    overall_progress,
                                    self.instalacao_status,
                                    key
                                )
            self.add_log(
                [
                    (f"Geração da Base concluída.", "bold blue"),
                    (
                        "\tDuração total {}.\n".format(self.total),
                        "bold red",
                    ),
                ]
            )
            self.add_log(
                [
                    (f"Tempo de processamento.", "bold blue"),
                    (
                        "\tDuração total {}.\n".format((datetime.now() - self.total_proccess_time)),
                        "bold red",
                    ),
                ]
            )
            self.instalacao_status.next()
