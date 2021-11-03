import os

import json
import typer
import pandas as pd
from rich.console import Console
from src.schema_body import SchemaBody
from src.schema_structure import SchemaStructure


app = typer.Typer()
console = Console()
cur_path = os.path.dirname(__file__)


@app.command()
def main(file: str = typer.Argument(..., help="File to parse"), 
         sheet_number: int = typer.Argument(..., help="Sheet number to parse"), 
         topic_name: str = typer.Argument(..., help="Topic name to parse"),
         schema_description: str = typer.Argument(..., help="Schema description to parse"),):
    """
    Parse a XLSX file and create a topic in the specified topic name.
    """
    try:
        new_path: str = os.path.relpath(file, cur_path)

        dataFrame: pd.DataFrame = pd.read_excel(
            new_path, sheet_name=sheet_number, header=19, usecols="B:D, F, H").dropna()

        schema_body = SchemaBody(dataFrame)
        schema_structure = SchemaStructure(topic_name, schema_description=schema_description)
        
        header = schema_structure.make_header()
        body = schema_body.make_body()
        footer = schema_structure.make_footer()
        
        full_schema = header | body | footer
    
        
        with open(f"{topic_name}-value.json", "w", encoding='utf8') as file:
            json.dump(full_schema, file, ensure_ascii=False)

    except IOError:
        console.print("[bold red]File not found[/bold red]")


if __name__ == "__main__":
    app()
