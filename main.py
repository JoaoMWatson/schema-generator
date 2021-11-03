import os

import json
import typer
import pandas as pd
from rich.console import Console
from src.schema_body import SchemaBody


app = typer.Typer()
console = Console()
cur_path = os.path.dirname(__file__)


@app.command()
def main(file: str = typer.Argument(..., help="File to parse"), sheet_number: int = typer.Argument(..., help="Sheet number to parse"), topic_name: str = typer.Argument(..., help="Topic name to parse")):
    """
    Parse a XLSX file and create a topic in the specified topic name.
    """
    try:
        new_path: str = os.path.relpath(file, cur_path)

        dataFrame: pd.DataFrame = pd.read_excel(
            new_path, sheet_name=sheet_number, header=19, usecols="B:D, F, H").dropna()

        schema_body = SchemaBody(dataFrame)

        body = schema_body.make_body()

        console.log(body)
        # console.print(f"Topic {topic_name} created successfully!")

        with open(f"{topic_name}-value.json", "w", encoding='utf8') as file:
            json.dump(body, file, ensure_ascii=False)

    except IOError:
        console.print("[bold red]File not found[/bold red]")


if __name__ == "__main__":
    app()
