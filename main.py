import os

import typer
import pandas as pd
from rich.console import Console

app = typer.Typer()
console = Console()
cur_path = os.path.dirname(__file__)

                                                                                 

@app.command()
def main(file: str = typer.Argument(..., help="File to parse"), sheet_number: int = typer.Argument(..., help="Sheet number to parse")):
    """
    """
    try:
        new_path: str = os.path.relpath(file, cur_path)
        
        dataFrame: pd.DataFrame = pd.read_excel(new_path, sheet_name=sheet_number, header=19, usecols="B:D, F, H").dropna()

        console.log(dataFrame)
        
    except IOError:
        console.print("[bold red]File not found[/bold red]")
        

if __name__ == "__main__":
    app()
