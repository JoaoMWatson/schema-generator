import typer
import pandas as pd
from typing import List, Dict
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main(file: str = typer.Argument(..., help="File to parse"), sheet_number: int = typer.Argument(..., help="Sheet number to parse")):
    """
    """
    dataFrame: pd.DataFrame = pd.read_excel(file, sheet_name=sheet_number, header=19, usecols="B:D, F, H")

    console.log(dataFrame)
    # with open(file, "r") as f:
    #     file_content = f.read()
    #     console.log(file_content)


if __name__ == "__main__":
    app()
