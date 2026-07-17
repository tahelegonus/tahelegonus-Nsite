#load up animation


import time

from rich.console import Console
from rich.progress import Progress
from rich.progress import SpinnerColumn
from rich.progress import TextColumn

console = Console()


def show_loading():

    steps = [

        "Loading configuration...",

        "Loading detection rules...",

        "Loading event mappings...",

        "Loading TeddyBear engine...",

        "Initializing interface...",

        "Ready!"
    ]

    with Progress(

        SpinnerColumn("moon"),

        TextColumn("[progress.description]{task.description}")

    ) as progress:

        task = progress.add_task("", total=None)

        for step in steps:

            progress.update(
                task,
                description=step
            )

            time.sleep(0.5)
