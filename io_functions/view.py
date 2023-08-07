from rich.console import Console
from rich.markdown import Markdown

console = Console()

def print_md(text: str) -> None:
    console.print(Markdown(text))