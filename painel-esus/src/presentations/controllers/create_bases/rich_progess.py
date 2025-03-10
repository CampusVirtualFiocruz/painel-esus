from sys import stdout
from time import sleep

from rich import print
from rich.console import Console
from rich.live import Live
from rich.logging import RichHandler
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text
from src.errors.logging import logging

console= Console(stderr=True)

class InstallJobs:
    creation = []
    key_factors = []

    def __init__(self, creation=[], key_factors=[]):
        self.creation = creation
        self.key_factors = key_factors


class StartGeneration:

    def __init__(self, jobs: InstallJobs):
        self.jobs = jobs

    def run(self):
        job_progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        job_progress.add_task(
            "[green]Generate Base",
            total=len(self.jobs.creation),
        )
        job_progress.add_task(
            "[magenta]Calculating key factors",
            total=len(self.jobs.key_factors),
        )

        total = sum(task.total for task in job_progress.tasks)
        overall_progress = Progress()

        overall_task = overall_progress.add_task("Instalando", total=int(total))

        progress_table = Table.grid()
        progress_table.add_row(
            Panel.fit(
                overall_progress,
                title="Overall Progress",
                border_style="green",
                padding=(2, 2),
            ),
            Panel.fit(
                job_progress,
                title="[b]Jobs",
                border_style="yellow",
                padding=(1, 2, 2, 2),
            ),
        )

        with Live(progress_table, refresh_per_second=10):
            while not overall_progress.finished:

                for key, job in enumerate(job_progress.tasks):
                    if not job.finished:
                        if key == 0:
                            for context in self.jobs.creation:
                                context.create_base()
                                job_progress.advance(job.id)
                                # overall_progress.console.log(f"Job [bold blue]{context._base}[/] concluído.")
                                sleep(0.3)
                                completed = sum(task.completed for task in job_progress.tasks)
                                overall_progress.update(overall_task, completed=completed)
                        if key == 1:
                            for context in self.jobs.key_factors:
                                context.create_base()
                                job_progress.advance(job.id)
                                # overall_progress.console.log(f"Job [bold blue]{context._base}[/] concluído.")
                                sleep(0.3)
                                completed = sum(
                                    task.completed for task in job_progress.tasks
                                )
                                overall_progress.update(overall_task, completed=completed)

                #     # completed = sum(task.completed for task in job_progress.tasks)
                #     # overall_progress.update(overall_task, completed=completed)
