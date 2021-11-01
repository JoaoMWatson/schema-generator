import os

import json
import typer
import pandas as pd
from rich.console import Console
from src.schema import SchemaBody


app = typer.Typer()
console = Console()
cur_path = os.path.dirname(__file__)


@app.command()
def main(file: str = typer.Argument(..., help="File to parse"), sheet_number: int = typer.Argument(..., help="Sheet number to parse"), topic_name: str = typer.Argument(..., help="Topic name to parse")):
    """
    Parse a CSV file and create a topic in the specified topic name.
    """
    try:
        new_path: str = os.path.relpath(file, cur_path)

        dataFrame: pd.DataFrame = pd.read_excel(
            new_path, sheet_name=sheet_number, header=19, usecols="B:D, F, H").dropna()

        schema_body = SchemaBody(dataFrame)

        fields = []
        for index, row in dataFrame.iterrows():
            fields.append(schema_body.create_node(
                type_of=row["Tipo"],
                name=row["Campo"],
                size=row["Tamanho"],
                is_null=row["Aceita"],
                description=row['Comentários'])
            )

        with open(f"{topic_name}-value.json", "w", encoding='utf8') as file:
            json.dump(fields, file, ensure_ascii=False)

        # console.print(f"Topic {topic_name} created successfully!")
        console.log(fields)

    except IOError:
        console.print("[bold red]File not found[/bold red]")


if __name__ == "__main__":
    app()
