#dividers


from rich.console import Console
from rich.rule import Rule

from theme_colors import BORDER

console = Console()


def draw_divider(title=None):
    """
    Draw a horizontal divider.

    Example:
        draw_divider()

        draw_divider("System Information")
    """

    console.print(
        Rule(
            title=title,
            style=BORDER
        )
    )
